"""Pure validation for Atlassian domain request intents."""
from collections.abc import Mapping
from typing import Any

_SECRET_KEYS = frozenset({
    "authorization", "api_key", "client_secret", "access_token",
    "refresh_token", "password", "secret",
})
_ALLOWED_OPERATIONS = frozenset({"list", "get", "create", "update", "delete", "archive", "revoke", "disable", "remove", "transfer"})

def validate_request(operation: str, resource: str, payload: Mapping[str, Any] | None = None) -> None:
    if not isinstance(operation, str) or operation.strip().lower() not in _ALLOWED_OPERATIONS:
        raise ValueError("unsupported or missing operation")
    if not isinstance(resource, str) or not resource.strip():
        raise ValueError("resource is required")
    if payload is not None and not isinstance(payload, Mapping):
        raise TypeError("payload must be a mapping")
    reject_inline_secrets(payload or {})

def reject_inline_secrets(value: Any, path: str = "payload") -> None:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key).strip().lower() in _SECRET_KEYS:
                raise ValueError(f"credential-like field is not allowed at {path}.{key}")
            reject_inline_secrets(nested, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for index, nested in enumerate(value):
            reject_inline_secrets(nested, f"{path}[{index}]")
