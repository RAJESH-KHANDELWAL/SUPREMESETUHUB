"""Provider-wide secret and operation security boundaries."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ..policy import ensure_operation_allowed

SECRET_FIELD_NAMES = frozenset({
    "api_key", "apikey", "token", "access_token", "refresh_token",
    "secret", "client_secret", "password", "authorization",
    "credential", "credential_value", "private_key",
})


def assert_no_secret_fields(value: Any) -> None:
    """Reject secret-like keys recursively in mappings and nested sequences."""
    if isinstance(value, Mapping):
        found = SECRET_FIELD_NAMES.intersection(
            str(key).strip().casefold() for key in value
        )
        if found:
            raise ValueError(
                "Secret material must be referenced through a secure runtime secret manager, not request metadata"
            )
        for nested in value.values():
            assert_no_secret_fields(nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            assert_no_secret_fields(nested)


__all__ = ["SECRET_FIELD_NAMES", "assert_no_secret_fields", "ensure_operation_allowed"]
