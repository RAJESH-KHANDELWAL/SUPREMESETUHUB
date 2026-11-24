"""WireGuard VPN adapter scaffold; no live connection configured."""
class WireGuardVPNEcosystem:
 provider_id="wireguard"
 display_name="WireGuard"
 capabilities=("vpn-tunnel-management",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
