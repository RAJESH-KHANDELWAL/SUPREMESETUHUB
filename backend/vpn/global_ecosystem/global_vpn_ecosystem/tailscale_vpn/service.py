"""Tailscale VPN adapter scaffold; no live connection configured."""
class TailscaleVPNEcosystem:
 provider_id="tailscale"
 display_name="Tailscale"
 capabilities=("mesh-vpn-management",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
