from typing import Generator
from typing import Any
from pandas import read_csv
from fastapi import UploadFile


class CSVReader:
    def get_content(self, file: UploadFile) -> Generator[Any, None, None]:
        df = read_csv(file, delimiter=";")
        for row in df.itertuples(index=False):
            yield row
