from .model import Person as PersonModel
from core.crud import CRUD


class Person(CRUD):
    def __init__(self):
        super().__init__(PersonModel)
