from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.crud import base as crud
from app.models import base as models
from app.schemas import base as schemas
from app.db.base import SessionLocal, engine

from app.utils import request_to_rust

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
        content = request_to_rust()
        if content:
            request_obj = schemas.RequestStorage(
                data_service=content, key_data=response_obj.key_data)
            return crud.create_request(db, request_obj=request_obj)
        else:
            raise HTTPException(status_code=500, detail="Error when try to proccess you request")
    return db_request
