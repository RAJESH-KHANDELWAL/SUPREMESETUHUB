"""Namecheap DNS adapter scaffold; no live connection configured."""
class NamecheapDNSEcosystem:
 provider_id="namecheap"
 display_name="Namecheap DNS"
 capabilities=("domain-and-dns-management",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
