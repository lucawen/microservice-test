from typing import Optional

from pydantic import BaseModel, Json


class RequestStorageRequestBase(BaseModel):
    key_data: str


class RequestStorageBase(BaseModel):
    data_service: Json
    key_data: str


class RequestStorageCreate(RequestStorageBase):
    pass


class RequestStorage(RequestStorageBase):
    id: int

    class Config:
        orm_mode = True
