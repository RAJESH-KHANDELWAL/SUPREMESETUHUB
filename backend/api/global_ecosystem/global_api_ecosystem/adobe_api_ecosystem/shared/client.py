"""Small HTTPS JSON transport. Endpoint paths and hosts must come from official API docs."""
from __future__ import annotations
import json
import time
from typing import Any, Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener
from .auth import AccessTokenProvider
from .errors import AdobeAuthenticationError, AdobeRateLimitError, AdobeResponseError, AdobeTransportError
from .retry import RetryPolicy

class _RejectRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

class AdobeApiClient:
    def __init__(self, *, base_url: str, token_provider: AccessTokenProvider, timeout: float = 20.0, retry_policy: RetryPolicy | None = None) -> None:
        parsed = urlparse(base_url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("Adobe API base_url must be an absolute HTTPS URL")
        self.base_url = base_url.rstrip("/") + "/"
        self.token_provider = token_provider
        self.timeout = timeout
        self.retry_policy = retry_policy or RetryPolicy()
        self._opener = build_opener(_RejectRedirects())

    def request(self, method: str, path: str, *, params: Mapping[str, str] | None = None, json_body: Any = None, headers: Mapping[str, str] | None = None) -> Any:
        method = method.upper()
        if not path or path.startswith(("/", "\\")) or "://" in path or any(part == ".." for part in path.split("/")):
            raise ValueError("path must be a safe relative API path")
        url = urljoin(self.base_url, path)
        if urlparse(url).netloc != urlparse(self.base_url).netloc or urlparse(url).scheme != "https":
            raise ValueError("API path cannot change host or protocol")
        if params:
            from urllib.parse import urlencode
            url += ("&" if "?" in url else "?") + urlencode(params)
        token = self.token_provider.get_access_token()
        request_headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        if json_body is not None:
            request_headers["Content-Type"] = "application/json"
        if headers:
            if any(key.lower() == "authorization" for key in headers):
                raise ValueError("Authorization header is managed by the token provider")
            request_headers.update(headers)
        body = None if json_body is None else json.dumps(json_body).encode("utf-8")
        idempotent = method in {"GET", "HEAD", "OPTIONS", "PUT", "DELETE"}
        attempts = self.retry_policy.max_attempts if idempotent else 1
        for attempt in range(attempts):
            req = Request(url, data=body, headers=request_headers, method=method)
            try:
                with self._opener.open(req, timeout=self.timeout) as response:
                    raw = response.read()
                    if not raw:
                        return None
                    content_type = response.headers.get("Content-Type", "")
                    return json.loads(raw.decode("utf-8")) if "json" in content_type.lower() else raw.decode("utf-8")
            except HTTPError as exc:
                status = exc.code
                if status in (401, 403):
                    raise AdobeAuthenticationError("Adobe API authorization failed", status_code=status) from None
                if status == 429:
                    if attempt + 1 < attempts:
                        time.sleep(self.retry_policy.backoff_seconds * (2 ** attempt))
                        continue
                    raise AdobeRateLimitError("Adobe API rate limit reached", status_code=status, retryable=True) from None
                if status in self.retry_policy.retry_statuses and attempt + 1 < attempts:
                    time.sleep(self.retry_policy.backoff_seconds * (2 ** attempt))
                    continue
                raise AdobeResponseError(f"Adobe API returned HTTP {status}", status_code=status, retryable=status in self.retry_policy.retry_statuses) from None
            except (URLError, TimeoutError) as exc:
                if attempt + 1 < attempts:
                    time.sleep(self.retry_policy.backoff_seconds * (2 ** attempt))
                    continue
                raise AdobeTransportError("Adobe API transport failed", retryable=True) from None
        raise AdobeTransportError("Adobe API request exhausted retries", retryable=True)
