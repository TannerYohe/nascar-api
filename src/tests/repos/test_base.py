from pytest import raises
from json import JSONDecodeError

from requests.exceptions import HTTPError

from nascar_api.repos.base import NascarRepo


def test_safe_get_retry_fail(requests_mock):
    mock_url = "https://test.com"
    requests_mock.get(mock_url, status_code=400, json={"error": "Bad Request"})
    repo = NascarRepo()
    with raises(HTTPError):
        repo.safe_get(mock_url)
    assert len(requests_mock.request_history) == 3

def test_safe_get_retry_success(requests_mock):
    mock_url = "https://test.com"
    count = 0
    def callback(request, context):
        nonlocal count
        count += 1
        if count <= 2:
            context.status_code = 500
            return {"error": "Internal Server Error"}
        else:
            context.status_code = 200
            return {"success": True}

    requests_mock.get(mock_url, json=callback)
    repo = NascarRepo()
    response = repo.safe_get(mock_url)
    assert response == {"success": True}
    assert len(requests_mock.request_history) == 3

def test_safe_get_no_retry_on_403(requests_mock):
    mock_url = "https://test.com"
    requests_mock.get(mock_url, status_code=403, json={"error": "Forbidden"})
    repo = NascarRepo()
    with raises(HTTPError):
        repo.safe_get(mock_url)
    assert len(requests_mock.request_history) == 1

def test_safe_get_json_decode_error(requests_mock):
    mock_url = "https://test.com"
    requests_mock.get(mock_url, text="Invalid JSON")
    repo = NascarRepo()
    with raises(JSONDecodeError):
        repo.safe_get(mock_url)
    assert len(requests_mock.request_history) == 3
