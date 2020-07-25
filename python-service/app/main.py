import json 

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
    """Return a list of requests cached on database

    Args:
        skip (int, optional): Skips the page. Defaults to 0.
        limit (int, optional): Limit per page. Defaults to 100.
        db (Session, optional): Database instance. Defaults to Depends(get_db).

    Returns:
        list[RequestStorage]: List with multiple RequestStorage schemas
    """
    requests = crud.get_requests(db, skip=skip, limit=limit)
    return requests


@app.post("/request/", response_model=schemas.RequestStorage)
def read_microservice(
        response_obj: schemas.RequestStorageRequestBase,
        db: Session = Depends(get_db)):
    """Make a request for proccess into a microservice

    If request 'key_data' already exists in database, its will return this data,
    otherwise will make a request to microservice and return the data

    Args:
        response_obj (schemas.RequestStorageRequestBase): Request data
        db (Session, optional): Database instance. Defaults to Depends(get_db).

    Raises:
        HTTPException: If any error happened, will raise a error

    Returns:
        RequestStorageRequestBase: The data informations from request 'key_data'
    """
    db_request = crud.get_request_by_key(
        db, key_data=response_obj.key_data)
    if not db_request:
        content = request_to_rust()
        if content:
            content_str = json.dumps(content)
            request_obj = schemas.RequestStorageBase(
                data_service=content_str, key_data=response_obj.key_data)
            crud_response = crud.create_request(db, request_obj=request_obj)
            return crud_response
        raise HTTPException(status_code=500, detail="Error when try to proccess you request")
    return db_request
