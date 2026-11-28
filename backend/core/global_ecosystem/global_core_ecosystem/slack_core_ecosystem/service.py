"""Slack Core ecosystem read-only control-plane service."""
from .catalog import get_slack_core_catalog
from .orchestrator import SlackCoreOrchestrator
class SlackCoreEcosystemService:
 NAME="SLACK CORE ECOSYSTEM"
 def __init__(self):self.orchestrator=SlackCoreOrchestrator()
 def status(self):
  c=get_slack_core_catalog();h=self.orchestrator.health()
  return {"success":True,"ecosystem_id":c["ecosystem_id"],"name":self.NAME,"provider":"slack","status":c["status"],"product_count":h["product_count"],"domain_count":h["domain_count"],"capability_count":h["capability_count"],"connected_products":0,"live_connection_verified":False,"api_calls_performed":0,"api_catalog_ref":c["api_catalog_ref"],"health":h}
 def list_products(self):return self.orchestrator.list_products()
 def list_domains(self):return self.orchestrator.domains()
