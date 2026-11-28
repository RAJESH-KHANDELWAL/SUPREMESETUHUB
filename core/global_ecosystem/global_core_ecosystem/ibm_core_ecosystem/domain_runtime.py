"""Shared read-only IBM domain manager."""
from __future__ import annotations
from typing import Any
from .domain_catalog import get_domain
class IBMCoreDomainManager:
    def __init__(self, domain_id: str) -> None:
        self._domain=get_domain(domain_id)
        if self._domain is None: raise ValueError(f"UNKNOWN_IBM_CORE_DOMAIN: {domain_id}")
    def describe(self) -> dict[str,Any]:
        return {"success":True,"ecosystem_id":"IBM-CORE-ECOSYSTEM","domain":dict(self._domain),"status":"CORE_CATALOG_ONLY","api_calls_performed":0}
