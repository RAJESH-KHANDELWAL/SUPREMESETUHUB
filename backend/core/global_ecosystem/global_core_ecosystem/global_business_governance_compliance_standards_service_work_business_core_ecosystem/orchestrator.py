"""Coordinates read-only taxonomy, validation and CORE health."""
from .catalog import get_catalog
from .module_service import BusinessGovernanceModuleService
class BusinessGovernanceCoreOrchestrator:
    def __init__(self) -> None: self.modules = BusinessGovernanceModuleService()
    def health(self) -> dict:
        status = self.modules.status()
        return {"success": True, "ecosystem_id": get_catalog()["ecosystem_id"], "status": "HEALTHY_METADATA_LAYER", **status, "external_api_calls": 0}
    def dependency_map(self) -> dict:
        return {"ecosystem_id": get_catalog()["ecosystem_id"], "dependencies": list(get_catalog()["dependencies"]), "dependency_execution_performed": False}
    def inventory(self) -> dict:
        return {"catalog": get_catalog(), "domains": self.modules.list_domains(), "capabilities": self.modules.list_capabilities()}
