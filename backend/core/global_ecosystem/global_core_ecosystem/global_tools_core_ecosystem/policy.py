"""Metadata guardrails, not provider authorization."""
SENSITIVE=("ADMIN","DELETE","WRITE","SEND","PUBLISH","BILLING","PAYMENT","IAM","PERMISSION","CAMPAIGN","SPEND")
class ToolsCorePolicyError(PermissionError): pass
class ToolsCorePolicy:
 @staticmethod
 def require_tenant(c):
  if c is None or not callable(getattr(c,"validate",None)): raise ToolsCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  c.validate()
 @staticmethod
 def validate_capability(p,c):
  if not p.get("enabled",True): raise ToolsCorePolicyError("PROVIDER_DISABLED")
  if c not in p.get("capabilities",[]): raise ToolsCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify(c): return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in c.upper() for x in SENSITIVE) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
 @staticmethod
 def safe_summary(x): return {k:v for k,v in x.items() if k.casefold() not in {"token","access_token","refresh_token","client_secret","api_key","secret","password"}}
