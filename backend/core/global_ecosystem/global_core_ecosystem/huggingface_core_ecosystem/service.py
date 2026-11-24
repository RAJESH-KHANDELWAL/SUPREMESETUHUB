"""Public Hugging Face CORE status service."""
from .catalog import get_catalog
from .orchestrator import HuggingFaceCoreOrchestrator
class HuggingFaceCoreEcosystemService:
    def __init__(self): self.orchestrator = HuggingFaceCoreOrchestrator()
    def status(self) -> dict:
        c = get_catalog()
        return {"success": True, "ecosystem_id": c["ecosystem_id"], "name": c["name"],
                "status": c["status"], "product_count": c["product_count"], "domain_count": c["domain_count"],
                "live_connection_verified": False, "connected": False, "api_calls_performed": 0}
    def catalog(self) -> dict: return self.orchestrator.catalog()
    def health(self) -> dict: return self.orchestrator.health()
    def dependency_map(self) -> dict: return self.orchestrator.dependency_map()
