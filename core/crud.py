from core.database import SessionDependency, SQLModel
from core.security import get_current_user
from core.types import Auditable, TableModel, UpdateModel
from src.auth import TokenData
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
        resource = self.__validate(model_create, extra_data)
        return self.__commit(resource)

    def create_all(self, models: list[SQLModel]) -> list[TableModel]:
        resources = [self.__validate(model) for model in models]
        return self.__commit(resources, bulk=True)

    def update(self, model_update: UpdateModel, update_data: dict = {}) -> TableModel:
        resource = self.read(model_update.id)
        update_fields = self.__set_update_data(model_update, update_data)
        resource.sqlmodel_update(update_fields, update=update_data)
        return self.__commit(resource)

    def delete(self, id: int) -> TableModel:
        resource = self.read(id)
        return self.update(resource, {"is_active": False})

    def __read_active(self, id: int) -> TableModel:
        resource = self.session.exec(
            select(self.base_model).where(
                self.base_model.id == id, self.base_model.is_active
            )
        ).first()

        if not resource:
            raise HTTPException(status_code=404, detail="Resource not found")

        return resource

    def __validate(self, model: SQLModel, extra_data: dict = {}) -> TableModel:
        self.__audit_create(extra_data)
        return self.base_model.model_validate(model, update=extra_data)

    def __set_update_data(self, incoming_data: UpdateModel, extra_data: dict) -> dict:
        self.__audit_update(extra_data)
        return incoming_data.model_dump(exclude_unset=True)

    def __audit_create(self, extra_data: dict) -> dict:
        extra_data.update({"created_by": self.current_user.id})

    def __audit_update(self, extra_data: dict) -> dict:
        extra_data.update(
            {"updated_by": self.current_user.id, "updated_at": datetime.now()}
        )

    def __commit(
        self, resource: TableModel | list[TableModel], bulk: bool = False
    ) -> TableModel | list[TableModel]:
        if not bulk:
            self.session.add(resource)
        else:
            self.session.add_all(resource)

        self.session.commit()

        if not bulk:
            self.session.refresh(resource)
        else:
            for r in resource:
                self.session.refresh(r)

        return resource
