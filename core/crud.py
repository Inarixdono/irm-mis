from core.security import get_current_user
from core.types import Audit, ModelUpdate
from core.database import SessionDependency, SQLModel
from src.auth.model import TokenData
from typing import Annotated
from datetime import datetime
from fastapi import Depends, HTTPException
from sqlmodel import select


class CRUD:
    def __init__(
        self,
        base_model: SQLModel = SQLModel,
    ):
        self.base_model = base_model

    def __call__(
        self,
        session: SessionDependency,
        current_user: Annotated[TokenData, Depends(get_current_user)],
    ):
        self.session = session
        self.current_user = current_user

    def read(self, id: int) -> SQLModel:
        resource = self.session.get(self.base_model, id)
        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")
        return resource

    def read_all(self) -> list[SQLModel]:
        if issubclass(self.base_model, Audit):
            statement = select(self.base_model).where(self.base_model.is_active)
        else:
            statement = select(self.base_model)
        return self.session.exec(statement).all()

    def create(self, model_create: SQLModel, extra_data: dict = {}) -> SQLModel:
        if issubclass(self.base_model, Audit):
            extra_data.update({"created_by": self.current_user.id})
        resource = self.base_model.model_validate(model_create, update=extra_data)
        return self.__commit(resource)

    def update(self, model_update: ModelUpdate, update_data: dict = {}) -> SQLModel:
        resource = self.read(model_update.id)

        if issubclass(self.base_model, Audit):
            update_data.update(
                {"updated_by": self.current_user.id, "updated_at": datetime.now()}
            )

        resource_data = model_update.model_dump(exclude_unset=True)
        resource.sqlmodel_update(resource_data, update=update_data)
        return self.__commit(resource)

    def delete(self, id: int) -> SQLModel:
        resource = self.read(id)
        if issubclass(self.base_model, Audit):
            self.update(ModelUpdate(id=id), {"is_active": False})
            return resource

        self.session.delete(resource)
        self.session.delete(resource)
        self.session.commit()

    def __commit(self, resource) -> SQLModel:
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
