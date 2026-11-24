"""Input validation and safe summaries for planned DeepSeek operations."""
from __future__ import annotations
from typing import Any
from urllib.parse import urlparse
from .constants import SUPPORTED_OPERATIONS

ALLOWED_OPERATIONS = SUPPORTED_OPERATIONS
_SECRET_KEYS = frozenset({"api_key", "authorization", "token", "secret", "password", "access_token", "refresh_token"})

def _contains_secret_key(payload: Any) -> bool:
    if isinstance(payload, dict):
        return any(str(k).casefold() in _SECRET_KEYS or _contains_secret_key(v) for k, v in payload.items())
    if isinstance(payload, (list, tuple)):
        return any(_contains_secret_key(item) for item in payload)
    return False

def validate_request(operation: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Validate operation structure; credentials are never accepted in payload."""
    if operation not in ALLOWED_OPERATIONS:
        raise ValueError(f"Unsupported DeepSeek operation: {operation}")
    if not isinstance(payload, dict):
        raise TypeError("payload must be a dictionary")
    if _contains_secret_key(payload):
        raise ValueError("Credentials must come from the server-side secret store, not request payloads")
    if operation in {"chat_completions", "responses"}:
        content = payload.get("messages", payload.get("input", payload.get("prompt")))
        if content is None or content == "" or content == []:
            raise ValueError("chat operation requires non-empty messages, input, or prompt")
    elif operation == "search":
        if not isinstance(payload.get("query"), str) or not payload["query"].strip():
            raise ValueError("search requires a non-empty string query")
    elif operation == "fetch":
        url = payload.get("url")
        if not isinstance(url, str) or not url.strip():
            raise ValueError("fetch requires a non-empty URL")
        parsed = urlparse(url.strip())
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("fetch URL must be an absolute HTTP(S) URL")
    return {"valid": True, "operation": operation}

def safe_input_summary(payload: dict[str, Any]) -> dict[str, Any]:
    """Return field names and coarse metadata only, never user content or secrets."""
    return {
        "input_fields": sorted(str(key) for key in payload),
        "contains_user_content": any(k in payload for k in ("messages", "input", "prompt", "query", "url")),
    }

__all__ = ["ALLOWED_OPERATIONS", "validate_request", "safe_input_summary"]
