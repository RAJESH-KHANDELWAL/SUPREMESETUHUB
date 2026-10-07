from __future__ import annotations

from typing import Any

import requests


class ExternalHTTPSConnector:
    """
    Secure HTTPS connector for authorized external APIs.

    External services remain on their own official servers.
    SUPREMESETUHUB only communicates through HTTPS.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 60,
        verify_ssl: bool = True,
    ) -> None:

        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.verify_ssl = verify_ssl

        if not self.base_url:
            raise ValueError(
                "EXTERNAL_API_BASE_URL_REQUIRED"
            )

        if not self.base_url.startswith("https://"):
            raise ValueError(
                "HTTPS_REQUIRED"
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

        if not url.startswith("https://"):
            raise ValueError(
                "HTTPS_REQUIRED_FOR_EXTERNAL_REQUEST"
            )

        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers or {},
            params=params or {},
            json=json,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )

        try:
            data = response.json()
        except ValueError:
            data = {
                "text": response.text,
            }

        return {
            "success": response.ok,
            "http_code": response.status_code,
            "response": data,
            "tls_verified": self.verify_ssl,
        }
