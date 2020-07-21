from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.crud import base as crud
from app.models import base as models
from app.schemas import base as schemas
from app.db.base import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    dbase = SessionLocal()
    try:
        yield dbase
    finally:
        dbase.close()


@app.get("/request/", response_model=List[schemas.RequestStorage])
def read_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    requests = crud.get_requests(db, skip=skip, limit=limit)
    return requests


@app.post("/request/", response_model=schemas.RequestStorage)
def read_microservice(
        response_obj: schemas.RequestStorageRequestBase,
        db: Session = Depends(get_db)):
    db_request = crud.get_request_by_key(
        db, key_data=response_obj.key_data)
    if not db_request:
        return {"key_data": "World", "id": 1}
        # call go microservice
        # return crud.create_user(db=db, user=user)
    return {"key_data": "World", "id": 1}
