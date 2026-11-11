"""Input validation for planned DeepSeek operations; never handles credentials."""
from __future__ import annotations
from typing import Any

ALLOWED_OPERATIONS = frozenset({"chat_completions", "responses", "search", "fetch"})
_SECRET_KEYS = frozenset({"api_key", "authorization", "token", "secret", "password"})

def validate_request(operation: str, payload: dict[str, Any]) -> dict[str, Any]:
    if operation not in ALLOWED_OPERATIONS:
        raise ValueError(f"Unsupported DeepSeek operation: {operation}")
    if not isinstance(payload, dict):
        raise TypeError("payload must be a dictionary")
    forbidden = sorted(str(key).casefold() for key in payload if str(key).casefold() in _SECRET_KEYS)
    if forbidden:
        raise ValueError("Credentials must be supplied through the server-side secret store, never request payloads")
    if operation in {"chat_completions", "responses"}:
        content = payload.get("messages", payload.get("input", payload.get("prompt")))
        if content is None:
            raise ValueError("chat operation requires messages, input, or prompt")
        if isinstance(content, (str, list)) and len(content) == 0:
            raise ValueError("chat input must not be empty")
    if operation == "search" and not str(payload.get("query", "")).strip():
        raise ValueError("search requires a non-empty query")
    if operation == "fetch" and not str(payload.get("url", "")).strip():
        raise ValueError("fetch requires a non-empty URL")
    return {"valid": True, "operation": operation}

__all__ = ["ALLOWED_OPERATIONS", "validate_request"]
