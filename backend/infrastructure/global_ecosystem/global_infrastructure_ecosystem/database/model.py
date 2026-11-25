"""Typed result contracts for read-only infrastructure database checks."""
from __future__ import annotations

from typing import Any, TypedDict


class DatabaseCheckResult(TypedDict, total=False):
    success: bool
    status: str
    engine: str
    reason: str
    error_type: str
    details: dict[str, Any]
    connection_attempted: bool
    mutations_performed: bool


class DatabaseHealthReport(TypedDict, total=False):
    success: bool
    service: str
    checks: dict[str, DatabaseCheckResult]
    mutations_performed: bool


__all__ = ["DatabaseCheckResult", "DatabaseHealthReport"]
