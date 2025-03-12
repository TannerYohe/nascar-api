from requests import get
from requests.exceptions import HTTPError
from tenacity import wait_fixed, stop_after_attempt, retry_if_exception_type, retry_if_exception, retry
from json import JSONDecodeError
from typing import Tuple

RETRY_ARGS = {
    "wait": wait_fixed(2),
    "stop": stop_after_attempt(3),
    "reraise": True,
    "retry": (retry_if_exception_type(JSONDecodeError) |
              (retry_if_exception_type(HTTPError) & retry_if_exception(lambda x: x.response.status_code != 403)))
}


class NascarRepo:
    DOMAIN = "https://cf.nascar.com"

    @retry(**RETRY_ARGS)
    def safe_get(self, url: str, timeout: Tuple[int, int]=(5,30)):
        response = get(url, timeout=timeout)
        response.raise_for_status()
        yield response.json()
        response.close()
