from pandas import read_csv
from fastapi import UploadFile


class CSVReader:
    def get_content(self, file: UploadFile):
        content = read_csv(file, delimiter=";")
        return content.to_dict(orient="records")