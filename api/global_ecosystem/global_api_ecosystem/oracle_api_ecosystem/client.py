"""Small OCI REST client using request-signature authentication."""
from __future__ import annotations

import json
from typing import Any
from urllib.parse import urljoin

import httpx

from .auth import sign_request
from .config import OCIConfig


class OCIClient:
    """OCI REST client; endpoints are explicit to respect region and realm."""

    def __init__(
        self,
        config: OCIConfig | None = None,
        base_url: str | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.config = config or OCIConfig.from_env()
        self.base_url = (base_url or self.config.base_url or "").rstrip("/") + "/"
        if not self.base_url.strip("/"):
            raise ValueError("Provide OCI_BASE_URL or an explicit service base_url")
        if not self.base_url.startswith("https://"):
            raise ValueError("OCI base URL must use HTTPS")
        self.timeout = timeout

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any = None,
    ) -> Any:
        url = urljoin(self.base_url, path.lstrip("/"))
        if params:
            url += ("&" if "?" in url else "?") + str(
                httpx.QueryParams(params)
            )
        body = (
            json.dumps(json_body, separators=(",", ":")).encode("utf-8")
            if json_body is not None else None
        )
        headers = sign_request(self.config, method, url, body)
        response = httpx.request(
            method.upper(),
            url,
            content=body,
            headers=headers,
            timeout=self.timeout,
        )
        response.raise_for_status()
        if not response.content:
            return None
        return response.json()
