"""Tenant isolation and fail-closed policies for Bada Business DNS."""
def require_tenant(tenant_id):
    if not isinstance(tenant_id, str) or not tenant_id.strip():
        raise ValueError("authenticated tenant_id is required")


def require_binding(binding, tenant_id, domain):
    if binding is None:
        raise LookupError("BADA_BUSINESS_DOMAIN_DNS_BINDING_NOT_FOUND")
    binding.validate()
    if binding.tenant_id != tenant_id:
        raise PermissionError("BADA_BUSINESS_TENANT_SCOPE_MISMATCH")
    if binding.normalized_domain != domain.strip().lower().rstrip("."):
        raise PermissionError("BADA_BUSINESS_DOMAIN_SCOPE_MISMATCH")
    if not binding.enabled:
        raise PermissionError("BADA_BUSINESS_DOMAIN_DNS_DISABLED")
    return binding
