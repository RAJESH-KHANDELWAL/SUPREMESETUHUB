"""Bada Business DNS facade delegating execution to the shared DNS service.

Tenant/domain binding persistence is injected from the owning application.
This module does not own provider credentials, SDKs, or business subscription
rules and does not pretend that a binding proves live DNS connectivity.
"""
from __future__ import annotations
from .catalog import BADA_BUSINESS_DNS_ECOSYSTEM
from .policies import require_tenant, require_binding
from ..service import GlobalDNSService


class BadaBusinessDNSService:
    def __init__(self, binding_repository, dns_service=None):
        if binding_repository is None:
            raise ValueError("binding_repository is required")
        self.binding_repository = binding_repository
        self.dns_service = dns_service or GlobalDNSService()

    def status(self):
        return {
            **BADA_BUSINESS_DNS_ECOSYSTEM,
            "binding_repository_configured": self.binding_repository is not None,
            "dns_service": self.dns_service.status(),
            "live_connection_verified": False,
        }

    def get_domain_binding(self, tenant_id: str, domain: str):
        require_tenant(tenant_id)
        normalized = domain.strip().lower().rstrip(".")
        binding = self.binding_repository.get_binding(tenant_id, normalized)
        return require_binding(binding, tenant_id, normalized)

    def list_records(self, tenant_id: str, domain: str):
        binding = self.get_domain_binding(tenant_id, domain)
        result = self.dns_service.list_records(binding.provider_id, binding.zone_id)
        return {
            "success": True,
            "tenant_id": tenant_id,
            "domain": binding.normalized_domain,
            "provider_id": binding.provider_id,
            "dns_result": result,
            "live_connection_verified": False,
        }

    def apply_change(self, tenant_id: str, domain: str, request):
        binding = self.get_domain_binding(tenant_id, domain)
        if request.provider_id.strip().lower() != binding.provider_id.strip().lower():
            raise PermissionError("DNS_CHANGE_PROVIDER_DOES_NOT_MATCH_DOMAIN_BINDING")
        if request.zone_id != binding.zone_id:
            raise PermissionError("DNS_CHANGE_ZONE_DOES_NOT_MATCH_DOMAIN_BINDING")
        result = self.dns_service.apply_change(request)
        return {
            "success": True,
            "tenant_id": tenant_id,
            "domain": binding.normalized_domain,
            "provider_id": binding.provider_id,
            "dns_result": result,
        }
