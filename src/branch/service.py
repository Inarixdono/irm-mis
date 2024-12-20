from .model import Branch as BranchModel
from core.crud import CRUD


class Branch(CRUD):
    def __init__(self):
        super().__init__(BranchModel)