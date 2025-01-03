import csv
from fastapi import UploadFile


class CSVReader:
    async def get_content(self, file: UploadFile):
        self.file = file
        reader = await self.__read()
        return [line for line in reader]

    async def __read(self):
        return csv.reader(await self.__decode(), delimiter=";")

    async def __decode(self):
        file = await self.file.read()
        return file.decode("utf-8").splitlines()
