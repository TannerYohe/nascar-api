"""Base repository module for NASCAR API operations.

This module provides the base repository class that handles HTTP requests
to the NASCAR API with automatic retry logic for transient failures.
"""

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
    """Base repository class for NASCAR API operations.

    Provides common functionality for making HTTP requests to the NASCAR API
    with automatic retry logic for transient failures.
    """

    DOMAIN = "https://cf.nascar.com"

    @cached_property
    def logger(self) -> Logger:
        """Get a logger instance for this repository.

        Returns:
            Logger: Configured logger instance for the repository.

        """
        return getLogger(__name__)

    @retry(
        wait=wait_fixed(2),
        stop=stop_after_attempt(3),
        reraise=True,
        retry=(
            retry_if_exception_type(JSONDecodeError)
            | (
                retry_if_exception_type(HTTPError)
                & retry_if_exception(
                    lambda x: isinstance(x, HTTPError) and x.response.status_code != 403
                )
            )
        ),
    )
    def safe_get(self, url: str, timeout: Tuple[int, int] = (5, 30)) -> Any:
        """Make a safe HTTP GET request with automatic retry logic.

        This method handles transient failures by automatically retrying requests
        that fail due to JSON decode errors or HTTP errors (except 403 Forbidden).
        It will retry up to 3 times with a 2-second delay between attempts.

        Args:
            url: The URL to request.
            timeout: Tuple of (connect_timeout, read_timeout) in seconds.
                    Defaults to (5, 30).

        Returns:
            The JSON response from the request.

        Raises:
            HTTPError: If the request fails after all retry attempts.
            JSONDecodeError: If the response cannot be parsed as JSON.

        """
        with get(url, timeout=timeout) as response:
            response.raise_for_status()
            return response.json()
