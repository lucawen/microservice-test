import requests

from app.core.config import settings


def request_to_rust():
    """Make a request to microservice

    Returns:
        None: Something goes wrong with request
        dict('result'): The result returned from request
    """
    req = requests.get(settings.microservice_api)
    if req.status_code == 200:
        return req.json()
    return None
