"""Read-only catalog service; no network calls or provider-side mutations."""

from .catalog import get_domain_provider, list_domain_categories, list_domain_providers
from .contracts import DomainReadiness
from .policy import classify_operation, reject_secret_material, require_metadata_only


class GlobalDomainCoreService:
    def list_providers(self):
        return list_domain_providers()

    def get_provider(self, provider_id: str):
        return get_domain_provider(provider_id)

    def categories(self):
        return list_domain_categories()

    def readiness(self, provider_id: str) -> DomainReadiness:
        provider = get_domain_provider(provider_id)
        if provider is None:
            raise LookupError("DOMAIN_PROVIDER_NOT_REGISTERED: " + str(provider_id))
        return DomainReadiness(
            provider_id=provider["id"],
            catalog_registered=True,
            live_connection_verified=False,
            execution_enabled=False,
            readiness="LIVE_VERIFICATION_REQUIRED",
        )

    def plan_metadata_operation(self, *, provider_id: str, operation: str, metadata=None):
        provider = get_domain_provider(provider_id)
        if provider is None:
            raise LookupError("DOMAIN_PROVIDER_NOT_REGISTERED: " + str(provider_id))
        reject_secret_material(metadata or {})
        require_metadata_only(operation)
        return {
            "accepted": True,
            "provider_id": provider["id"],
            "operation": operation.strip().upper(),
            "classification": classify_operation(operation),
            "execution_performed": False,
            "live_connection_verified": False,
        }
