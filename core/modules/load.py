import pandas as pd
import os

class Load:
    def __init__(self, df):
        self.df = df
    def load_to_csv(self):
        try:
            output_dir = 'db'
            output_file = os.path.join(output_dir, 'resultados.csv')
            self.df.to_csv(output_file, index=False, encoding='utf-8')
            print(f"Archivo guardado en {output_file}")
        except Exception as e:
            print(f"Error en el load.py {e}")    