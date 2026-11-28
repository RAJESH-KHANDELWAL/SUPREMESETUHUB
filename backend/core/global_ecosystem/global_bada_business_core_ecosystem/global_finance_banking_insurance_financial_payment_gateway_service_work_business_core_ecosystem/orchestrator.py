"""Google-Core-style discovery and orchestration for finance commercial metadata."""
from .catalog import get_catalog
from .domain_catalog import business_domain_summary, get_domain, list_domains, search_domains, validate_mappings
from .product_catalog import get_package, list_packages, package_summary, search_packages
from .policy import FinanceServiceWorkBusinessPolicy

class FinanceServiceWorkBusinessOrchestrator:
    def catalog(self) -> dict:
        return get_catalog()

    def domains(self) -> dict:
        return business_domain_summary()

    def domain_inventory(self) -> list[dict]:
        return list_domains()

    def get_domain(self, domain_id: str) -> dict | None:
        return get_domain(domain_id)

    def packages(self, *, business_domain_id: str | None = None) -> dict:
        items = list_packages(business_domain_id=business_domain_id)
        return {"success": True, "count": len(items), "packages": items}

    def get_package(self, package_name: str) -> dict | None:
        item = get_package(package_name)
        return FinanceServiceWorkBusinessPolicy.safe_public_summary(item) if item else None

    def search(self, keyword: str) -> dict:
        domains = search_domains(keyword)
        packages = search_packages(keyword)
        return {
            "success": True,
            "query": keyword,
            "domain_count": len(domains),
            "package_count": len(packages),
            "domains": domains,
            "packages": packages,
        }

    def health(self) -> dict:
        catalog = self.catalog()
        mapping = validate_mappings()
        package_status = package_summary()
        return {
            "success": mapping["valid"],
            "ecosystem_id": catalog["ecosystem_id"],
            "status": "HEALTHY_CATALOGUE" if mapping["valid"] else "MAPPING_VALIDATION_FAILED",
            "business_domain_count": mapping["business_domain_count"],
            "canonical_domain_count": mapping["canonical_domain_count"],
            "canonical_package_count": package_status["package_count"],
            "mapped_package_count": mapping["mapped_package_count"],
            "mapping_integrity": mapping["valid"],
            "provider_connections_verified": 0,
            "transaction_execution_enabled": False,
            "warning": "Catalogue readiness does not prove licensed operations, provider connectivity or live transaction capability.",
        }

    def dependency_map(self) -> dict:
        return {
            "success": True,
            "edges": [
                {"from": "GLOBAL_SUPREME_ECOSYSTEM_CATALOG", "to": "GLOBAL_FINANCE_CORE", "relationship": "MASTER_TAXONOMY_AND_IMPLEMENTATION_REGISTRY_REFERENCE"},
                {"from": "GLOBAL_FINANCE_CORE", "to": "FINANCE_SERVICE_WORK_BUSINESS_CORE", "relationship": "READ_ONLY_CANONICAL_DOMAIN_AND_PACKAGE_DEPENDENCY"},
                {"from": "FINANCE_SERVICE_WORK_BUSINESS_CORE", "to": "APPLICATION_AND_API_LAYERS", "relationship": "CLASSIFICATION_METADATA_CONSUMPTION_ONLY"},
            ],
            "master_catalog_path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
            "canonical_core_path": "backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_core_ecosystem",
            "master_catalog_modified_by_this_module": False,
        }
