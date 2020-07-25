import pytest


from fastapi.testclient import TestClient


@pytest.fixture
def mock_request_rust(mocker, expect):
    mocker.patch('app.utils.request_to_rust', return_value=expect)

@pytest.mark.usefixtures('mock_request_rust')
@pytest.mark.parametrize(
    "expect",
    [
        {'result': '103290123901032091'},
        {'result': 'SAUHHUASDUHDSASAUHSADHU'},
        {'result': 'ItsReal'},
        {'result': 'Any Data'},
        {'result': 33},
        {'result': {"weather": "anything"}},
    ],
)
def test_request_rust_success(expect):
    """Test if request to rust success.

    The response need to be a valid type (not null);
    The response need to be a 'result' key inside it;
    """
    from app.utils import request_to_rust
    request = request_to_rust()
    assert request is not None
    assert 'result' in request.keys()


@pytest.mark.usefixtures('mock_request_rust')
@pytest.mark.parametrize(
    "expect",
    [
        None,
        "String",
        333
    ],
)
def test_request_rust_error_instance(expect):
    """Test if request to rust will error.

    In the scenario that request have a error, will be not a dict
    """
    from app.utils import request_to_rust
    request = request_to_rust()
    assert type(request) != dict
