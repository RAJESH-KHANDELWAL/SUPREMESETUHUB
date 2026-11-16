"""Global AI CORE policy metadata; not provider authorization."""
SENSITIVE=("WRITE","DELETE","PUBLISH","BILLING","TRAIN","FINE_TUNE","UPLOAD","ADMIN","TOOL","EXECUTE")
class GlobalAICorePolicyError(PermissionError): pass
class GlobalAICorePolicy:
 @staticmethod
 def require_tenant_context(context):
  if context is None or not callable(getattr(context,"validate",None)): raise GlobalAICorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  context.validate()
 @staticmethod
 def classify_capability(capability):
  key=str(capability).upper()
  return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_AND_AUDIT" if any(x in key for x in SENSITIVE) else "STANDARD_REQUIRES_TENANT_AND_PROVIDER_AUTHORIZATION"
 @staticmethod
 def execution_status(): return {"runtime_execution_enabled":False,"live_provider_connections_verified":False,"credentials_in_core_allowed":False}
