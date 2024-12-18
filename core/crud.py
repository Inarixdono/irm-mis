from core.types import Audit, ModelUpdate
from core.database import SessionDependency, SQLModel
from datetime import datetime
from fastapi import HTTPException
from sqlmodel import select


class CRUD:
    def __init__(self, session: SessionDependency):
        self.session = session

    def read(self, base_model: SQLModel, id: int):
        resource = self.session.get(base_model, id)
        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")
        return resource

    def read_all(self, base_model: SQLModel):
        statement = select(base_model)
        return self.session.exec(statement).all()

    def create(self, base_model: SQLModel, model_create: SQLModel, extra_data=None):
        print(model_create)
        resource = base_model.model_validate(model_create, update=extra_data)
        return self.__commit(resource)

    def update(
        self, base_model: SQLModel, model_update: ModelUpdate, extra_data: dict = {}
    ):
        resource: SQLModel = self.session.get(base_model, model_update.id)

        if issubclass(base_model, Audit):
            extra_data.update({"updated_at": datetime.now()})

        resource_data = model_update.model_dump(exclude_unset=True)
        resource.sqlmodel_update(resource_data, update=extra_data)
        return self.__commit(resource)

    def __commit(self, resource):
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
