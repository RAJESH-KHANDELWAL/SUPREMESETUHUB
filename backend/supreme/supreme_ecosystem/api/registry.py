"""Central route registry for the SUPREME API ECOSYSTEM.

Existing endpoint implementations remain in their established modules under
backend.api. This registry composes their routers without duplicating business
logic or changing public URL prefixes.
"""
from __future__ import annotations

from collections.abc import Iterable

from fastapi import APIRouter

SYSTEM_NAME = "SUPREME API ECOSYSTEM"
PARENT_SYSTEM = "SUPREME ECOSYSTEM"
ACCESS_POLICY = "PRIVATE_BY_DEFAULT"


def build_api_router(routers: Iterable[APIRouter]) -> APIRouter:
    """Compose existing API routers while preserving their route prefixes."""
    registry = APIRouter()
    for router in routers:
        registry.include_router(router)
    return registry


__all__ = [
    "ACCESS_POLICY",
    "PARENT_SYSTEM",
    "SYSTEM_NAME",
    "build_api_router",
]
