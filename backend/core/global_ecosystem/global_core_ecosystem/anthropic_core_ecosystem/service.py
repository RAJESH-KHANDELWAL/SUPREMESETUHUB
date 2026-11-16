"""Anthropic Core Ecosystem read-only control-plane service."""
from __future__ import annotations
from typing import Any
from .catalog import get_anthropic_core_catalog
from .orchestrator import AnthropicCoreOrchestrator

class AnthropicCoreEcosystemService:
    NAME="ANTHROPIC CORE ECOSYSTEM"
    def __init__(self): self.orchestrator=AnthropicCoreOrchestrator()
    def status(self) -> dict[str,Any]:
        c=get_anthropic_core_catalog(); health=self.orchestrator.health()
        return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":self.NAME,
                "provider":"anthropic","status":c["status"],"module_count":len(c["children"]),
                "connected_modules":0,"live_connection_verified":False,"api_calls_performed":0,
                "health":health,"api_catalog_ref":c["api_catalog_ref"],
                "existing_anthropic_core_ref":c["existing_anthropic_core_ref"]}
    def list_modules(self): return self.orchestrator.list_products()
    def get_module(self,ecosystem_id: str): return self.orchestrator.get_product(ecosystem_id)
    def health(self): return self.orchestrator.health()
    def dependency_map(self): return self.orchestrator.dependency_map()
