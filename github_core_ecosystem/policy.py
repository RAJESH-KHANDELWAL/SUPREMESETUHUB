"""GitHub CORE policy metadata checks; not GitHub authorization."""
SENSITIVE=("WRITE","DELETE","MERGE","DISPATCH","ADMIN","BILLING","PERMISSION","SECRET","SECURITY","PUBLISH","REVOKE")
class GitHubCorePolicyError(PermissionError): pass
class GitHubCorePolicy:
 @staticmethod
 def require_tenant_context(context):
  if context is None or not callable(getattr(context,"validate",None)): raise GitHubCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  context.validate()
 @staticmethod
 def validate_capability(module,capability):
  if not module.get("enabled",True): raise GitHubCorePolicyError("FAMILY_DISABLED")
  if capability not in set(module.get("capabilities",[])): raise GitHubCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability): return "SENSITIVE_REQUIRES_EXPLICIT_PROVIDER_AUTHORIZATION_AND_AUDIT" if any(x in capability.upper() for x in SENSITIVE) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
 @staticmethod
 def safe_summary(module):
  blocked={"token","access_token","refresh_token","authorization","api_key","client_secret","private_key","webhook_secret","password","secret"}
  return {k:v for k,v in module.items() if k.casefold() not in blocked}
