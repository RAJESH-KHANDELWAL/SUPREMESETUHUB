"""AWS Systems Manager adapter scaffold; no live session configured."""
class AWSSSMSSHEcosystem:
 provider_id="aws-ssm"
 display_name="AWS Systems Manager"
 capabilities=("managed-remote-access",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
