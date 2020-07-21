from sqlalchemy.orm import Session

from app.models import base as models
from app.schemas import base as schemas


def get_request(db: Session, request_id: int):
    return db.query(
        models.RequestStorage).filter(
            models.RequestStorage.id == request_id).first()


def get_request_by_key(db: Session, key_data: int):
    return db.query(
        models.RequestStorage).filter(
            models.RequestStorage.key_data == key_data).first()


def get_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RequestStorage).offset(skip).limit(limit).all()


def create_request(db: Session, request_obj: schemas.RequestStorage):
    db_request = models.RequestStorage(**request_obj.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request
