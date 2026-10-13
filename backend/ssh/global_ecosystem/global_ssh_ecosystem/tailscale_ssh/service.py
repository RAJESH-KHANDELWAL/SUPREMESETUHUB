"""Tailscale SSH adapter scaffold; no live session configured."""
class TailscaleSSHEcosystem:
 provider_id="tailscale-ssh"
 display_name="Tailscale SSH"
 capabilities=("identity-aware-ssh",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
