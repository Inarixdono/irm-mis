from typing import Iterable
from typing import Any
from pandas import read_csv
from fastapi import UploadFile


class CSVReader:
    def get_content(self, file: UploadFile) -> Iterable[Any]:
        df = read_csv(file, delimiter=";")
        for row in df.itertuples(index=False):
            yield row
