"""Small synchronous Stripe REST client with bounded network behavior."""
from __future__ import annotations

from typing import Any, Mapping
from urllib.parse import urljoin

import httpx

from .config import StripeConfig


class StripeAPIError(RuntimeError):
    def __init__(self, message: str, *, status_code: int | None = None, request_id: str | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.request_id = request_id


class StripeClient:
    def __init__(self, config: StripeConfig, transport: httpx.BaseTransport | None = None):
        self.config = config
        self._client = httpx.Client(
            base_url=f"{config.api_base_url}/",
            headers=config.headers(),
            timeout=httpx.Timeout(config.read_timeout, connect=config.connect_timeout),
            transport=transport,
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        data: Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> dict[str, Any]:
        normalized = path.lstrip("/")
        if normalized.startswith("http:") or normalized.startswith("https:") or ".." in normalized.split("/"):
            raise ValueError("Only relative Stripe API paths are accepted")
        headers = {}
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key
        try:
            response = self._client.request(method.upper(), normalized, params=params, data=data, headers=headers)
        except httpx.HTTPError as exc:
            raise StripeAPIError(f"Stripe transport error: {type(exc).__name__}") from exc
        request_id = response.headers.get("Request-Id")
        try:
            payload = response.json()
        except ValueError as exc:
            raise StripeAPIError("Stripe returned a non-JSON response", status_code=response.status_code, request_id=request_id) from exc
        if response.is_error:
            error = payload.get("error", {}) if isinstance(payload, dict) else {}
            message = error.get("message", "Stripe API request failed") if isinstance(error, dict) else "Stripe API request failed"
            raise StripeAPIError(message, status_code=response.status_code, request_id=request_id)
        if not isinstance(payload, dict):
            raise StripeAPIError("Stripe response shape was not an object", status_code=response.status_code, request_id=request_id)
        return payload

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "StripeClient":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
