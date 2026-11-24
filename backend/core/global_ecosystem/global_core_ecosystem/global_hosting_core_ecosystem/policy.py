"""Hosting metadata policy; not provider authorization."""
SENSITIVE_MARKERS=("ADMIN","DELETE","WRITE","CREATE","PROVISION","BILLING","PAYMENT","DNS_CHANGE","DEPLOY","SECRET","CREDENTIAL","TRANSFER")
class HostingCorePolicyError(ValueError):pass
class HostingCorePolicy:
 @staticmethod
 def require_tenant_context(context):
  if context is None:raise HostingCorePolicyError("TENANT_CONTEXT_REQUIRED")
  context.validate()
 @staticmethod
 def validate_capability(provider,capability):
  if provider.get("enabled") is False:raise HostingCorePolicyError("PROVIDER_DISABLED")
  if capability not in set(provider.get("capabilities",[])):raise HostingCorePolicyError("CAPABILITY_NOT_REGISTERED")
 @staticmethod
 def classify_capability(capability):return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(x in capability.upper() for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
 @staticmethod
 def safe_summary(record):
  blocked={"token","access_token","refresh_token","client_secret","api_key","secret","password","private_key"}
  return {k:v for k,v in record.items() if k.casefold() not in blocked}
