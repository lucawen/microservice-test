from sqlalchemy import Column, Integer, String, JSON

from app.db.base import Base


class RequestStorage(Base):
    __tablename__ = "request_storage"

    id = Column(Integer, primary_key=True, index=True)
    key_data = Column(String, unique=True, index=True)
    data_service = Column(JSON)
