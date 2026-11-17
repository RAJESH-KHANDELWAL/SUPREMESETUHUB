"""Read-only orchestration for human-language domains."""

from .catalog import get_catalog, get_domain, get_domains, get_provider_catalog, get_service_tiers
from .constants import ECOSYSTEM_ID, STATUS


class GlobalHumanLanguageCoreOrchestrator:
    def catalog(self):
        return get_catalog()

    def list_domains(self):
        return get_domains("HUMAN")

    def get_domain(self, domain_id):
        return get_domain(domain_id)

    def providers(self):
        return get_provider_catalog()

    def tiers(self):
        return get_service_tiers()

    def health(self):
        catalog = get_catalog()
        return {
            "ecosystem_id": ECOSYSTEM_ID,
            "status": STATUS,
            "divisions": len(catalog["divisions"]),
            "domains": catalog["domain_count"],
            "execution_enabled": False,
        }
