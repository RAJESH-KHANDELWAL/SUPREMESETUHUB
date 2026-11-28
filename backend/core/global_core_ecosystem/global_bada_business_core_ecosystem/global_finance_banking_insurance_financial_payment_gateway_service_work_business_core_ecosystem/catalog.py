"""Canonical commercial-layer catalogue linked to Global Finance CORE and master registry."""
from copy import deepcopy
from .domain_catalog import BUSINESS_DOMAINS, business_domain_summary, validate_mappings
from .product_catalog import FINANCE_BUSINESS_PACKAGES

ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL FINANCE BANKING INSURANCE FINANCIAL PAYMENT GATEWAY SERVICE WORK BUSINESS CORE ECOSYSTEM"
CANONICAL_ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-CORE-ECOSYSTEM"
CANONICAL_SOURCE_PATH = "backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_core_ecosystem"
MASTER_CATALOG_PATH = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_REGISTRY_KEY = "global_finance_banking_insurance_financial_payment_gateway_core_ecosystem"
ECOSYSTEM_PATH = "backend/core/global_ecosystem/global_core_ecosystem/global_bada_business_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_service_work_business_core_ecosystem"

def get_catalog() -> dict:
    summary = business_domain_summary()
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "ecosystem_type": "GLOBAL_BADA_BUSINESS_DOMAIN_CORE",
        "parent_id": "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM",
        "layer": "GLOBAL_BADA_BUSINESS_CORE",
        "repository_path": ECOSYSTEM_PATH,
        "canonical_ecosystem_id": CANONICAL_ECOSYSTEM_ID,
        "canonical_source_path": CANONICAL_SOURCE_PATH,
        "master_catalog_ref": MASTER_CATALOG_PATH,
        "master_implementation_registry_key": MASTER_REGISTRY_KEY,
        "status": "REGISTERED",
        "enabled": True,
        "business_domain_count": summary["domain_count"],
        "canonical_package_count": len(FINANCE_BUSINESS_PACKAGES),
        "service_work_business_capabilities": ["SERVICE", "WORK", "BUSINESS"],
        "delivery_models": sorted({model for item in BUSINESS_DOMAINS for model in item["delivery_models"]}),
        "domains": summary["domains"],
        "children": [deepcopy(item) for item in FINANCE_BUSINESS_PACKAGES],
        "mapping_integrity": validate_mappings()["valid"],
        "mode": "CLASSIFICATION_ONLY",
        "provider_connections_verified": 0,
        "transaction_execution_enabled": False,
    }

def get_finance_business_catalog() -> dict:
    return get_catalog()

def list_finance_business_modules() -> list[dict]:
    return [deepcopy(item) for item in FINANCE_BUSINESS_PACKAGES]
