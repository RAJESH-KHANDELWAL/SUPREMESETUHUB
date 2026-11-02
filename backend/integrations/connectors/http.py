from __future__ import annotations

from typing import Any

import requests


class ExternalHTTPConnector:
    """
    Generic HTTP connector for authorized external APIs.

    This does NOT install or host the external service.
    It only communicates with the provider's official API.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 60,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        if not self.base_url:
            raise ValueError(
                "EXTERNAL_API_BASE_URL_REQUIRED"
            )

    def request(
        self,
        method: str,
        path: str = "",
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        url = (
            f"{self.base_url}/{path.lstrip('/')}"
            if path
            else self.base_url
        )

        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers or {},
            params=params or {},
            json=json,
            timeout=self.timeout,
        )

        try:
            data = response.json()
        except ValueError:
            data = {
                "text": response.text,
            }

        if not response.ok:
            return {
                "success": False,
                "http_code": response.status_code,
                "response": data,
            }

        return {
            "success": True,
            "http_code": response.status_code,
            "response": data,
        }
