"""Read-only shared domain runtime for Developer Core."""
from __future__ import annotations
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS, developer_domain_summary, list_developer_domain_inventory

class DeveloperCoreDomainManager:
    def __init__(self, domain_id: str):
        self.domain_id=domain_id.strip().upper()
        if self.domain_id not in DOMAIN_DEFINITIONS: raise ValueError(f"UNKNOWN_DEVELOPER_CORE_DOMAIN: {self.domain_id}")
        self.definition=DOMAIN_DEFINITIONS[self.domain_id]
    def status(self) -> dict[str,Any]:
        return {"success":True,"domain_id":self.domain_id,"name":self.definition["name"],"purpose":self.definition["purpose"],"status":"CORE_DOMAIN_AVAILABLE","live_connections_verified":0,"api_calls_performed":0}
    def list_modules(self) -> dict[str,Any]:
        from .manager import get_global_developer_core_catalog
        items=[x for x in get_global_developer_core_catalog()["children"] if x["domain_id"]==self.domain_id]
        return {"success":True,"domain_id":self.domain_id,"count":len(items),"modules":items}
