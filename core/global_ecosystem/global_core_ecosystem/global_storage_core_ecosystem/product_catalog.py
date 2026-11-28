"""Curated storage product-family registry; catalog presence is not entitlement."""
from __future__ import annotations
from typing import Any
from .catalog import get_storage_core_catalog
def list_storage_products(*,provider_id: str|None=None,domain_id: str|None=None,enabled_only: bool=False) -> list[dict[str,Any]]:
    items=get_storage_core_catalog()["products"]
    if provider_id: items=[x for x in items if x["provider_id"]==provider_id.strip().casefold()]
    if domain_id: items=[x for x in items if x["domain_id"]==domain_id.strip().upper()]
    if enabled_only: items=[x for x in items if x.get("enabled",True)]
    return items
def get_storage_product(product_id: str):
    key=product_id.strip().casefold()
    return next((x for x in list_storage_products() if x["product_id"].casefold()==key or x["ecosystem_id"].casefold()==key),None) if key else None
def storage_product_summary() -> dict[str,Any]:
    items=list_storage_products()
    return {"success":True,"product_count":len(items),"products":items,"installation_verified_count":0,"entitlement_verified_count":0}
