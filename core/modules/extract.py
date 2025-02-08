import pandas as pd

class Extractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_from_csv(self):
        try:
        
            df = pd.read_csv(self.file_path, delimiter=';')
            #print(f"\n{df.to_string()}")
            return df
        
        except Exception as e:
            print(f"Error en el extract.py {e}")