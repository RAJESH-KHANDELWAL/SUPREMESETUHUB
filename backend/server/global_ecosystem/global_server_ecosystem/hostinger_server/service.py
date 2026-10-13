"""Hostinger server integration scaffold; no live connection is configured."""
class HostingerServerEcosystem:
 provider_id="hostinger"
 display_name="Hostinger Servers"
 capabilities=("server-management",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
