from modules.extract import Extractor
from modules.tranform import Transform
from modules.load import Load
from config import CSV_FILE_PATH

def main():
    try:
        print("Se estan extrayendo los datos del csv..")
        df = Extractor(CSV_FILE_PATH).extract_from_csv()
        print("Se esta transformando el dataframe...")
        df_transform = Transform(df).transform_data()
        print("Se esta carga el dataframe en un csv...")
        Load(df_transform).load_to_csv()
    except Exception as e:
        print(f"Error en el main.py {e}")

if __name__ == "__main__":
    main()  