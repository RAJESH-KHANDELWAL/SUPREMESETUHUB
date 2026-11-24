"""Pure validation helpers for Anthropic request intents."""
from collections.abc import Mapping
from typing import Any

_ALLOWED_ROLES = frozenset({"user", "assistant"})
_FORBIDDEN_KEYS = frozenset({"api_key", "authorization", "access_token", "secret", "password"})

def validate_messages_payload(payload: Mapping[str, Any]) -> None:
    if not isinstance(payload, Mapping):
        raise TypeError("payload must be a mapping")
    messages = payload.get("messages")
    if not isinstance(messages, list) or not messages:
        raise ValueError("messages must be a non-empty list")
    for index, message in enumerate(messages):
        if not isinstance(message, Mapping):
            raise TypeError(f"messages[{index}] must be an object")
        if message.get("role") not in _ALLOWED_ROLES:
            raise ValueError(f"messages[{index}].role must be user or assistant")
        if "content" not in message:
            raise ValueError(f"messages[{index}].content is required")
    if not isinstance(payload.get("model"), str) or not payload["model"].strip():
        raise ValueError("model is required")
    if not isinstance(payload.get("max_tokens"), int) or payload["max_tokens"] <= 0:
        raise ValueError("max_tokens must be a positive integer")

def reject_inline_secrets(value: Any, path: str = "payload") -> None:
    """Reject credentials embedded inside domain payloads or metadata."""
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key).strip().lower() in _FORBIDDEN_KEYS:
                raise ValueError(f"secret-like field is not allowed at {path}.{key}")
            reject_inline_secrets(nested, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, nested in enumerate(value):
            reject_inline_secrets(nested, f"{path}[{index}]")
