"""Hetzner VPS adapter scaffold; no live connection configured."""
class HetznerVPSEcosystem:
 provider_id="hetzner"
 display_name="Hetzner Cloud"
 capabilities=("virtual-private-servers",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
