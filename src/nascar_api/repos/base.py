from functools import cached_property
from json import JSONDecodeError
from logging import Logger, getLogger
from typing import Any, Tuple

from requests import get
from requests.exceptions import HTTPError
from tenacity import (
    retry,
    retry_if_exception,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)


class NascarRepo:
    DOMAIN = "https://cf.nascar.com"

    @cached_property
    def logger(self) -> Logger:
        return getLogger(__name__)

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3), reraise=True, retry= (retry_if_exception_type(JSONDecodeError) |
              (retry_if_exception_type(HTTPError) & retry_if_exception(lambda x: isinstance(x, HTTPError) and x.response.status_code != 403))))
    def safe_get(self, url: str, timeout: Tuple[int, int]=(5,30)) -> Any:
        with get(url, timeout=timeout) as response:
            response.raise_for_status()
            return response.json()
