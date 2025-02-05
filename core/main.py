from modules.extract import extract_from_csv
from config import EXCEL_FILE_PATH,EXTRACTION_MODE

def main():
    df = extract_from_csv(EXCEL_FILE_PATH)
if __name__ == "__main__":
    main()  