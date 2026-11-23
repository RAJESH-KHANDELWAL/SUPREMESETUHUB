"""Business-facing discovery adapter over canonical Transport CORE taxonomy."""
from __future__ import annotations

from typing import Any
from .catalog import get_business_catalog, get_business_capability_group, list_business_capability_groups

class GlobalTransportBusinessCoreService:
    def status(self) -> dict[str, Any]:
        return {"success": True, **get_business_catalog()}

    def list_capability_groups(self) -> dict[str, Any]:
        groups = list_business_capability_groups()
        return {"success": True, "count": len(groups), "capability_groups": groups}

    def get_capability_group(self, group_id: str) -> dict[str, Any] | None:
        return get_business_capability_group(group_id)
