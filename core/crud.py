from core.database import SessionDependency, SQLModel
from core.security import get_current_user
from core.types import  Auditable, TableModel, UpdateModel
from src.auth.model import TokenData
from typing import Annotated
from datetime import datetime
from fastapi import Depends, HTTPException
from sqlmodel import select


class CRUD:
    def __init__(
        self,
        base_model: Auditable = Auditable,
    ):
        self.base_model = base_model

    def __call__(
        self,
        session: SessionDependency,
        current_user: Annotated[TokenData, Depends(get_current_user)],
    ):
        self.session = session
        self.current_user = current_user
        return self

    def read(self, id: int) -> TableModel:
        return self.__read_active(id)

    def read_all(self) -> list[TableModel]:
        return self.session.exec(
            select(self.base_model).where(self.base_model.is_active)
        ).all()

    def create(self, model_create: SQLModel, extra_data: dict = {}) -> TableModel:
        resource = self.__validate_model(model_create, extra_data)
        return self.__commit(resource)

    def update(self, model_update: UpdateModel, update_data: dict = {}) -> TableModel:
        resource = self.read(model_update.id)

        update_data.update(
            {"updated_by": self.current_user.id, "updated_at": datetime.now()}
        )

        resource_data = model_update.model_dump(exclude_unset=True)
        resource.sqlmodel_update(resource_data, update=update_data)
        return self.__commit(resource)

    def delete(self, id: int) -> TableModel:
        resource = self.read(id)
        self.update(UpdateModel(id=id), {"is_active": False})
        return resource

    def __read_active(self, id: int) -> TableModel:
        resource = self.session.exec(
            select(self.base_model).where(
                self.base_model.id == id, self.base_model.is_active
            )
        ).first()

        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")

        return resource

    def __validate_model(self, incoming_data: SQLModel, extra_data: dict) -> TableModel:
        extra_data.update({"created_by": self.current_user.id})
        return self.base_model.model_validate(incoming_data, update=extra_data)

    def __commit(self, resource) -> TableModel:
        self.session.add(resource)
        self.session.commit()
        self.session.refresh(resource)
        return resource
