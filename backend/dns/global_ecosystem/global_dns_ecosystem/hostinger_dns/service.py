"""Hostinger DNS adapter scaffold; no live connection configured."""
class HostingerDNSEcosystem:
 provider_id="hostinger"
 display_name="Hostinger DNS"
 capabilities=("dns-record-management",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
