"""AWS server integration scaffold; no live connection is configured."""
class AWSServerEcosystem:
 provider_id="aws"
 display_name="AWS Compute"
 capabilities=("cloud-server-management",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
