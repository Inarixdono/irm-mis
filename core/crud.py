from core.database import SessionDependency, SQLModel
from core.types import Model
from fastapi import HTTPException
from sqlmodel import select


class CRUD:
    def __init__(self, session: SessionDependency):
        self.session = session

    def read(self, base_model: Model, id: int):
        resource = self.session.get(base_model, id)
        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")
        return resource

    def read_all(self, base_model: SQLModel):
        statement = select(base_model)
        return self.session.exec(statement).all()

    def create(self, base_model: SQLModel, model_create: SQLModel):
        resource = base_model.model_validate(model_create)
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource

    def update(self, base_model: SQLModel, model_update: Model):
        resource = self.session.get(base_model, model_update.id)
        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")
        resource_data = model_update.model_dump(exclude_unset=True)
        resource.sqlmodel_update(resource_data)
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
