"""Canonical Python manager for Stripe Core Ecosystem."""
from .orchestrator import StripeCoreOrchestrator
from .service import StripeCoreEcosystemService
class StripeCoreManager:
 NAME="STRIPE CORE ECOSYSTEM"
 ECOSYSTEM_ID="STRIPE-CORE-ECOSYSTEM"
 def __init__(self):self._orchestrator=StripeCoreOrchestrator();self._service=StripeCoreEcosystemService()
 def status(self):return self._service.status()
 def health(self):return self._orchestrator.health()
 def list_products(self,*,enabled_only=False):return self._orchestrator.list_products(enabled_only=enabled_only)
 def get_product(self,identifier):return self._orchestrator.get_product(identifier)
 def list_domains(self):return self._orchestrator.domains()
 def list_offerings(self):return self._orchestrator.offerings()
 def dependency_map(self):return self._orchestrator.dependency_map()
def get_manager():return StripeCoreManager()
__all__=["StripeCoreManager","get_manager"]
