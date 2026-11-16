"""Provider-wide secret and operation security boundaries."""
from __future__ import annotations

from collections.abc import Mapping

from ..policies import ensure_operation_allowed

SECRET_FIELD_NAMES = frozenset({
    "api_key", "apikey", "token", "access_token", "refresh_token",
    "secret", "client_secret", "password", "authorization",
})


def assert_no_secret_fields(mapping: Mapping) -> None:
    if not isinstance(mapping, Mapping):
        raise ValueError("request metadata must be a mapping")
    found = SECRET_FIELD_NAMES.intersection(
        str(key).strip().casefold() for key in mapping
    )
    if found:
        raise ValueError(
            "Secret material must be referenced through a secure runtime secret manager, not request metadata"
        )


__all__ = ["SECRET_FIELD_NAMES", "assert_no_secret_fields", "ensure_operation_allowed"]
