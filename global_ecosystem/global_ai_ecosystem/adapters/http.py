"""Small standard-library JSON HTTP transport with secret-safe errors."""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

from .errors import (
    ProviderAuthenticationError, ProviderRateLimitError,
    ProviderRequestError, ProviderTransportError,
)
from .retry import RetryPolicy


class JsonHttpClient:
    RETRYABLE_STATUS = {429, 500, 502, 503, 504}

    def __init__(self, *, timeout_seconds: float = 30.0, retry_policy: RetryPolicy | None = None):
        if timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be positive.")
        self.timeout_seconds = timeout_seconds
        self.retry_policy = retry_policy or RetryPolicy()

    def post_json(
        self, url: str, *, headers: dict[str, str], payload: dict[str, Any],
        idempotency_key: str | None = None,
    ) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8")
        safe_headers = {**headers, "Content-Type": "application/json", "Accept": "application/json"}
        if idempotency_key:
            safe_headers["Idempotency-Key"] = idempotency_key
        attempts = self.retry_policy.max_attempts if idempotency_key else 1
        for attempt in range(1, attempts + 1):
            request = urllib.request.Request(url, data=body, headers=safe_headers, method="POST")
            try:
                with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                    parsed = json.loads(response.read().decode("utf-8"))
                    if not isinstance(parsed, dict):
                        raise ProviderRequestError("Provider returned a non-object JSON response.")
                    return parsed
            except urllib.error.HTTPError as exc:
                status = exc.code
                if status in self.RETRYABLE_STATUS and attempt < attempts:
                    retry_after = None
                    try:
                        retry_after = float(exc.headers.get("Retry-After", ""))
                    except (TypeError, ValueError):
                        pass
                    self.retry_policy.wait(attempt, retry_after)
                    continue
                if status in (401, 403):
                    raise ProviderAuthenticationError(f"Provider authentication failed (HTTP {status}).") from None
                if status == 429:
                    raise ProviderRateLimitError("Provider rate limit reached (HTTP 429).") from None
                raise ProviderRequestError(f"Provider request failed (HTTP {status}).") from None
            except (urllib.error.URLError, TimeoutError, OSError):
                raise ProviderTransportError("Provider network request failed or timed out.") from None
            except json.JSONDecodeError:
                raise ProviderRequestError("Provider returned invalid JSON.") from None
        raise ProviderTransportError("Provider request exhausted its retry policy.")
