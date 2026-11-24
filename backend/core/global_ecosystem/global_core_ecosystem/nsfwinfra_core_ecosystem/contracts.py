"""Shared result envelope for metadata-only NSF Winfra Core managers."""
from __future__ import annotations
from typing import Any
def result(*, success: bool, ecosystem_id: str, status: str, data: Any = None, error: str | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {"success": bool(success), "ecosystem_id": ecosystem_id, "status": status, "live_connection_verified": False, "execution_performed": False}
    if data is not None: payload["data"] = data
    if error: payload["error"] = error
    return payload
