from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_request_create_success():
    response = client.post(
        "/request/",
        json={"key_data": "batman"}
    )
    assert response.status_code == 200
    resp_json = response.json()
    resp_keys = resp_json.keys()
    assert 'key_data' in resp_keys
    assert resp_json.get('key_data') == 'batman'
    assert 'data_service' in resp_keys
    assert 'id' in resp_keys


def test_request_cached_success():

    def validate(response):
        assert response.status_code == 200
        resp_json = response.json()
        resp_keys = resp_json.keys()
        assert 'key_data' in resp_keys
        assert resp_json.get('key_data') == 'superman'
        assert 'data_service' in resp_keys
        assert 'id' in resp_keys

    response = client.post(
        "/request/",
        json={"key_data": "superman"}
    )
    validate(response)
    response = client.post(
        "/request/",
        json={"key_data": "superman"}
    )
    validate(response)
