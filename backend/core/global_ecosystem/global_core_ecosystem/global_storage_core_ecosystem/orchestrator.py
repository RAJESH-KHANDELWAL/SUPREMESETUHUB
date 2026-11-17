"""Deterministic metadata orchestration for Global Storage CORE."""
from __future__ import annotations

from .contracts import CoreResult
from .service import get_provider_metadata, list_provider_metadata


def dispatch(action: str, *, provider_id: str | None = None) -> CoreResult:
    if action == "list_providers":
        return list_provider_metadata()
    if action == "get_provider":
        if not provider_id:
            return CoreResult(False, status="INVALID_ARGUMENT", errors=["PROVIDER_ID_REQUIRED"])
        return get_provider_metadata(provider_id)
    return CoreResult(False, status="UNSUPPORTED_ACTION", errors=["ACTION_NOT_SUPPORTED"])


__all__ = ["dispatch"]
