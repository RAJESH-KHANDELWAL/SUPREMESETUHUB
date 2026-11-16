"""Global AI Core metadata policy; API authorization remains external."""
SENSITIVE=("ADMIN","DELETE","WRITE","PUBLISH","BILLING","TRAIN","FINE_TUNE","UPLOAD","TOOL","EXECUTE","SEND")
class GlobalAICorePolicyError(PermissionError): pass
class GlobalAICorePolicy:
 @staticmethod
 def require_tenant_context(context):
  if context is None or not callable(getattr(context,"validate",None)): raise GlobalAICorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  context.validate()
 @staticmethod
 def validate_capability(provider,capability):
  if provider.get("disabled") is True: raise GlobalAICorePolicyError("PROVIDER_DISABLED")
  allowed=set(provider.get("capabilities",[]))
  if allowed and capability not in allowed: raise GlobalAICorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability):
  return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_AND_AUDIT" if any(x in capability.upper() for x in SENSITIVE) else "STANDARD_REQUIRES_TENANT_AND_PROVIDER_AUTHORIZATION"
 @staticmethod
 def safe_provider_summary(provider):
  blocked={"token","access_token","refresh_token","client_secret","api_key","secret","authorization","password","credential_value"}
  return {k:v for k,v in provider.items() if k.casefold() not in blocked}
