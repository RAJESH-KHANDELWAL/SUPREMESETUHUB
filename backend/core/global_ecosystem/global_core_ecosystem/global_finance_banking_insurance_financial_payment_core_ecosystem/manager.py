"""Read-only manager for finance ecosystem catalogue discovery."""

from .catalog import FINANCE_ECOSYSTEM_CATALOG
from .domain_catalog import DOMAIN_PACKAGES


class FinanceEcosystemManager:
    def list_domains(self):
        return tuple(FINANCE_ECOSYSTEM_CATALOG["domains"].keys())

    def get_domain(self, domain_id):
        return FINANCE_ECOSYSTEM_CATALOG["domains"].get(domain_id)

    def list_packages(self, domain_id=None):
        if domain_id is not None:
            return tuple(DOMAIN_PACKAGES.get(domain_id, ()))
        return tuple(
            package
            for packages in DOMAIN_PACKAGES.values()
            for package in packages
        )

    def find_package(self, package_name):
        for domain_id, packages in DOMAIN_PACKAGES.items():
            if package_name in packages:
                return {"package_name": package_name, "domain_id": domain_id}
        return None
