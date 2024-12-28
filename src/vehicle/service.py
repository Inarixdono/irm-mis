from .model import (
    Make as MakeModel,
    VehicleModel as VehicleModelTable,
    Vehicle as VehicleTable,
    Request as RequestModel,
    RequestCreateBody,
    VehicleRequest,
    VehicleRequestCreate,
)

from core.crud import CRUD


# Make


class Make(CRUD):
    def __init__(self):
        super().__init__(MakeModel)


# Vehicle Model


class VehicleModel(CRUD):
    def __init__(self):
        super().__init__(VehicleModelTable)


# Vehicle


class Vehicle(CRUD):
    def __init__(self):
        super().__init__(VehicleTable)


# Request


class Request(CRUD):
    def __init__(self):
        super().__init__(RequestModel)

    def create(self, body: RequestCreateBody) -> RequestModel:
        return super().create(body.request, self.__set_detail(body.detail))

    def __set_detail(
        self, detail: list[VehicleRequestCreate]
    ) -> dict[str, list[VehicleRequestCreate]]:
        return {"detail": self.__extract_detail(detail)}

    def __extract_detail(
        self, detail: list[VehicleRequestCreate]
    ) -> list[VehicleRequestCreate]:
        return [VehicleRequest.model_validate(request) for request in detail]
