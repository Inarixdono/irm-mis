from pydantic import BaseModel
from .types import Person


class PublicUser(BaseModel, Person):
    pass