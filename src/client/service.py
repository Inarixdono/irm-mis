from .model import Client as ClientModel
from core.crud import CRUD


class Client(CRUD):
    def __init__(self):
        super().__init__(ClientModel)
