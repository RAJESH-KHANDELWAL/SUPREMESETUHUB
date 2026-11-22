"""Stable product/provider inventory facade."""
from __future__ import annotations
from typing import Any
from .manager import get_global_developer_core_catalog

def list_developer_modules() -> list[dict[str,Any]]:
    return get_global_developer_core_catalog()["children"]
def developer_inventory_summary() -> dict[str,Any]:
    items=list_developer_modules()
    return {"module_count":len(items),"provider_module_count":sum(x["ecosystem_type"]=="PROVIDER_CORE_SERVICE" for x in items),"domain_module_count":sum(x["ecosystem_type"]=="DEVELOPER_DOMAIN_CORE" for x in items),"live_connections_verified":0}
