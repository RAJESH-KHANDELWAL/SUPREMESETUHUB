"""DeepSeek Core metadata and operation guardrails."""
from __future__ import annotations

BLOCKED_OPERATIONS = frozenset({
    "delete_model",
    "change_billing",
    "rotate_provider_key",
    "create_deployment",
    "delete_dataset",
})


class DeepSeekCorePolicyError(PermissionError):
    """Raised when an operation crosses a Core policy boundary."""


def ensure_operation_allowed(operation: str) -> None:
    if not isinstance(operation, str) or not operation.strip():
        raise ValueError("operation must be non-empty")
    if operation.strip().casefold() in BLOCKED_OPERATIONS:
        raise DeepSeekCorePolicyError(
            "operation requires approved API/ENGINE authorization"
        )


def public_provider_metadata(catalog: dict) -> dict:
    """Return public provider metadata without secret-like values."""
    blocked = {
        "token", "access_token", "refresh_token", "client_secret",
        "api_key", "secret", "authorization", "password",
    }
    return {
        key: value for key, value in catalog.items()
        if str(key).casefold() not in blocked
    }
