"""GitHub Actions SSH deployment adapter scaffold; no live connection configured."""
class GitHubActionsSSHEcosystem:
 provider_id="github-actions-ssh"
 display_name="GitHub Actions SSH Deployment"
 capabilities=("authorized-ci-deployment",)
 def describe(self): return {"provider_id":self.provider_id,"display_name":self.display_name,"capabilities":list(self.capabilities),"connection_status":"not_configured"}
