"""Proton VPN adapter scaffold; no live connection configured."""
class ProtonVPNEcosystem:
 provider_id="protonvpn"
 display_name="Proton VPN"
 capabilities=("privacy-vpn-service",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
