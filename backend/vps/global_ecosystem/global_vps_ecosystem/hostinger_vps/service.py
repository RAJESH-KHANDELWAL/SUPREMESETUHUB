"""Hostinger VPS adapter scaffold; no live connection configured."""
class HostingerVPSEcosystem:
 provider_id="hostinger"
 display_name="Hostinger VPS"
 capabilities=("virtual-private-servers",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
