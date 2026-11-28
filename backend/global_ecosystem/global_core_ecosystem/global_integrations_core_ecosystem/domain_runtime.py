"""Shared read-only runtime used by each registered domain package."""
from .catalog import get_integration
from .constants import ECOSYSTEM_ID, STATUS
class IntegrationDomainManager:
    DOMAIN_ID=""
    def __init__(self,domain_id=None):
        key=domain_id or self.DOMAIN_ID
        record=get_integration(key)
        if not record: raise ValueError(f"UNKNOWN_INTEGRATION_DOMAIN: {key}")
        self.DOMAIN_ID=key
        self._record=record
    def status(self):
        r=self._record
        return {"success":True,"ecosystem_id":ECOSYSTEM_ID,"domain_id":self.DOMAIN_ID,
          "name":r["display_name"],"category":r["category"],"sensitivity":r["sensitivity"],
          "status":STATUS,"age_restricted":r["age_restricted"],"consent_required":r["consent_required"],
          "capability_count":len(r["capabilities"]),"live_connection_verified":False,"api_calls_performed":0}
    def describe(self): return dict(self._record)
    def capabilities(self): return list(self._record["capabilities"])
    def dependencies(self):
        return {"domain_id":self.DOMAIN_ID,"delegates_to":["API","ADAPTERS","SECURITY_CONFIGURATION","DATABASE_STORAGE","ENGINE"],"execution_enabled":False}
__all__=["IntegrationDomainManager"]
