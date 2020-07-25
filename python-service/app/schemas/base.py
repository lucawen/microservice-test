from typing import Optional, Any

from pydantic import BaseModel


class RequestStorageRequestBase(BaseModel):
    key_data: str


class RequestStorageBase(BaseModel):
    data_service: Any
    key_data: str


class RequestStorageCreate(RequestStorageBase):
    pass


class RequestStorage(RequestStorageBase):
    id: int

    class Config:
        orm_mode = True
