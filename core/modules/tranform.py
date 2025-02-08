import pandas as pd

from datetime import datetime

class Transform:
    def __init__(self, df):
        self.df = df

    # True if t2-t1 is smaller than 2 days
    def inRecallTimeWindow(self,t1,t2):
        timeWindowDays = 2.0
        dt1 = datetime.strptime(t1,"%Y/%m/%d %H:%M:%S")
        dt2 = datetime.strptime(t2,"%Y/%m/%d %H:%M:%S")
        delta = dt2 - dt1
        days = int(delta.total_seconds ()/86400.0)
        return days<timeWindowDays, delta

    def transform_data(self):
        try:
            df_sorted = self.df.sort_values(by=['customer_id','call_ts'], ascending=[True, True])
            #print(f"\n{df_sorted.head(35)}")

            # Crear una nueva columna 'is_precursor' con valores por defecto 'N'
            df_sorted['is_precursor'] = 'N'
            # Crear una nueva columna 'is_recall' con valores por defecto 'N'
            df_sorted['is_recall'] = 'N'
            # Crear una nueva columna 'precursor_call_id' con valores por defecto None
            df_sorted['precursor_call_id'] = None
            # Crear una nueva columna 'precursor_call_id' con valores por defecto None
            df_sorted['hours_from_first_call'] = None

            prev_calls = {}  # Diccionario para almacenar la última llamada de cada cliente

            #print(f"\n{df_sorted.head(60)}")

            for index, row in df_sorted.iterrows():
                customer_id = row['customer_id']
                call_ts = row['call_ts']
                call_id = row['call_id']
                
                # if para ver si el cliente ya llamo alguna ves.
                if customer_id in prev_calls:
                    prev_index, prev_call_ts, prev_call_id = prev_calls[customer_id]# obtiene la ultima llamada del cliente
                    
                    # Evaluar si está dentro de la ventana de 48 horas
                    is_recall, hours = self.inRecallTimeWindow(prev_call_ts, call_ts)

                    # si is_recall es True (dentro de la ventana de 48 horas)
                    if is_recall:
                        df_sorted.at[prev_index, 'is_precursor'] = 'Y'  
                        df_sorted.at[index, 'is_recall'] = 'Y'
                        df_sorted.at[index, 'precursor_call_id'] = prev_call_id
                        df_sorted.at[index, 'hours_from_first_call'] = hours

                # Si nunca a llamado se registra la llamada en el diccionario
                else:
                    prev_calls[customer_id] = (index, call_ts, call_id)
            
            # eliminar columnas no necesarias
            df_result= df_sorted.drop('customer_id', axis=1)
            df_result= df_result.drop('call_ts', axis=1)

            print(df_result.head(60))
            return df_result
        
        except Exception as e:
            print(f"Error en el transform.py {e}")    