"""Canonical Meta Core manager matching the Google Core public contract."""
from __future__ import annotations
from typing import Any
from .catalog import get_meta_core_catalog
from .domain_catalog import get_meta_domain
from .domain_runtime import MetaCoreDomainManager
from .module_service import MetaProductCoreService
from .orchestrator import MetaCoreOrchestrator
from .service import MetaCoreEcosystemService
class MetaCoreManager:
    NAME="META CORE ECOSYSTEM"
    ECOSYSTEM_ID="META-CORE-ECOSYSTEM"
    def __init__(self)->None:
        self._orchestrator=MetaCoreOrchestrator()
        self._service=MetaCoreEcosystemService()
    def status(self)->dict[str,Any]: return self._service.status()
    def health(self)->dict[str,Any]: return self._orchestrator.health()
    def catalog(self)->dict[str,Any]: return self._orchestrator.catalog()
    def list_products(self,*,enabled_only:bool=False)->dict[str,Any]: return self._orchestrator.list_products(enabled_only=enabled_only)
    def get_product(self,product_id:str)->dict[str,Any]|None: return self._orchestrator.get_product(product_id)
    def list_domains(self)->dict[str,Any]: return self._orchestrator.domains()
    def list_domain_inventory(self)->list[dict[str,Any]]: return self._orchestrator.domain_inventory()
    def get_domain_manager(self,domain_id:str)->MetaCoreDomainManager: return MetaCoreDomainManager(domain_id)
    def get_product_manager(self,product_id:str)->MetaProductCoreService: return MetaProductCoreService(product_id)
    def dependency_map(self)->dict[str,Any]: return self._orchestrator.dependency_map()
def get_manager()->MetaCoreManager: return MetaCoreManager()
__all__=["MetaCoreManager","get_manager"]
