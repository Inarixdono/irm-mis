from core.database import SessionDependency, SQLModel
from core.types import Model
from sqlmodel import select


class CRUD:
    def __init__(self, session: SessionDependency):
        self.session = session

    def read(self, base_model: Model, id: int):
        statement = select(base_model).where(base_model.id == id)
        return self.session.exec(statement).first()

    def read_all(self, base_model: Model):
        statement = select(base_model)
        return self.session.exec(statement).all()

    def create(self, base_model: Model, model_in: SQLModel):
        resource = base_model(**model_in.model_dump())
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource

    def update(self, base_model: Model, model_in: Model):
        resource = self.session.get(base_model, model_in.id)
        resource_data = model_in.model_dump(exclude_unset=True)
        resource.sqlmodel_update(resource_data)
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
