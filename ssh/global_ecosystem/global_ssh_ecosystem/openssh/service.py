"""OpenSSH adapter scaffold; no live session configured."""
class OpenSSHEcosystem:
 provider_id="openssh"
 display_name="OpenSSH"
 capabilities=("secure-shell-session-management",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
