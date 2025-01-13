from .model import Make as MakeModel
from .model import VehicleCreate
from .model import VehicleModel as VehicleModelTable
from .model import Vehicle as VehicleTable
from .model import Request as RequestModel
from .model import RequestCreateBody
from .model import VehicleRequest
from .model import VehicleRequestCreate
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

    def create(self, body: VehicleCreate) -> VehicleTable:
        extra_data = {"branch_id": self.current_user.branch_id}
        return super().create(body, extra_data)


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
