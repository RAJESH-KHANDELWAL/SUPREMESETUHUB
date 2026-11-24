"""Canonical Slack Core manager."""
from .orchestrator import SlackCoreOrchestrator
from .service import SlackCoreEcosystemService
class SlackCoreManager:
 NAME="SLACK CORE ECOSYSTEM"
 ECOSYSTEM_ID="SLACK-CORE-ECOSYSTEM"
 def __init__(self):self._orchestrator=SlackCoreOrchestrator();self._service=SlackCoreEcosystemService()
 def status(self):return self._service.status()
 def health(self):return self._orchestrator.health()
 def list_products(self,*,enabled_only=False):return self._orchestrator.list_products(enabled_only=enabled_only)
 def get_product(self,identifier):return self._orchestrator.get_product(identifier)
 def list_domains(self):return self._orchestrator.domains()
 def list_domain_inventory(self):return self._orchestrator.domain_inventory()
 def dependency_map(self):return self._orchestrator.dependency_map()
def get_manager():return SlackCoreManager()
__all__=["SlackCoreManager","get_manager"]
