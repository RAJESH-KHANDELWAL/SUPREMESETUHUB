"""Application-facing read-only service for finance services, work and businesses."""
from .catalog import get_catalog
from .contracts import CoreResult
from .domain_catalog import CLASSIFICATION_TYPES, get_domain, list_domains, search_domains, validate_mappings
from .product_catalog import get_package, list_packages, search_packages
from .policy import FinanceServiceWorkBusinessPolicy

SUPPORTED_TYPES = set(CLASSIFICATION_TYPES) | {"PROJECT", "PRODUCT", "ADVISORY", "EMPLOYMENT", "TRAINING", "RESEARCH"}

class FinanceServiceWorkBusinessService:
    NAME = "GLOBAL FINANCE BANKING INSURANCE FINANCIAL PAYMENT GATEWAY SERVICE WORK BUSINESS CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"

    def status(self) -> dict:
        validation = validate_mappings()
        return {
            "success": validation["valid"],
            "ecosystem_id": self.ECOSYSTEM_ID,
            "name": self.NAME,
            "status": "CORE_CATALOG_AVAILABLE" if validation["valid"] else "MAPPING_VALIDATION_FAILED",
            "business_domain_count": validation["business_domain_count"],
            "canonical_domain_count": validation["canonical_domain_count"],
            "package_count": validation["mapped_package_count"],
            "classification_types": list(CLASSIFICATION_TYPES),
            "provider_connections_verified": 0,
            "execution_enabled": False,
        }

    def overview(self) -> dict:
        return {**self.status(), "catalog": get_catalog(), "domains": list_domains()}

    def classify(self, domain_id: str, classification_type: str, *, business_line: str | None = None,
                 jurisdiction: str | None = None) -> dict:
        item = get_domain(domain_id)
        if item is None:
            return CoreResult(False, self.ECOSYSTEM_ID, "UNKNOWN_BUSINESS_DOMAIN",
                              errors=["UNKNOWN_BUSINESS_DOMAIN"]).to_dict()
        kind = classification_type.strip().upper() if isinstance(classification_type, str) else ""
        if kind not in SUPPORTED_TYPES:
            return CoreResult(False, self.ECOSYSTEM_ID, "UNSUPPORTED_CLASSIFICATION_TYPE",
                              errors=["UNSUPPORTED_CLASSIFICATION_TYPE"]).to_dict()
        if business_line is not None and business_line not in item["business_lines"]:
            return CoreResult(False, self.ECOSYSTEM_ID, "BUSINESS_LINE_NOT_REGISTERED",
                              errors=["BUSINESS_LINE_NOT_REGISTERED"]).to_dict()
        FinanceServiceWorkBusinessPolicy.assert_classification_only("classify")
        data = {
            "domain": item,
            "classification_type": kind,
            "business_line": business_line,
            "jurisdiction": jurisdiction,
            "jurisdictional_review_required": True,
            "authorization_or_license_may_be_required": True,
            "execution_enabled": False,
            "provider_connection_verified": False,
        }
        return CoreResult(True, self.ECOSYSTEM_ID, "CLASSIFICATION_RESOLVED", data=data).to_dict()

    def search(self, keyword: str) -> dict:
        return {
            "success": True,
            "query": keyword,
            "domains": search_domains(keyword),
            "packages": search_packages(keyword),
        }

    def list_packages(self, *, business_domain_id: str | None = None) -> dict:
        items = list_packages(business_domain_id=business_domain_id)
        return {"success": True, "count": len(items), "packages": items}

    def get_package(self, package_name: str) -> dict | None:
        return get_package(package_name)

    def validate(self) -> dict:
        return validate_mappings()

__all__ = ["FinanceServiceWorkBusinessService", "SUPPORTED_TYPES"]
