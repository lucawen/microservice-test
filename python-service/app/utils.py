import requests

from app.core.config import settings


def request_to_rust():
    req = requests.get(settings.microservice_api)
    if req.status_code == 200:
        return req.json()
    return None
