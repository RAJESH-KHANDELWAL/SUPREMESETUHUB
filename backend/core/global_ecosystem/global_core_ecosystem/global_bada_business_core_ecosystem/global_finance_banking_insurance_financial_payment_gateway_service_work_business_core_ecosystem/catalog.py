"""Commercial catalogue linked to the canonical Global Finance CORE."""
from .domain_catalog import list_domains

ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL FINANCE BANKING INSURANCE FINANCIAL PAYMENT GATEWAY SERVICE WORK BUSINESS CORE ECOSYSTEM"
CANONICAL_ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-CORE-ECOSYSTEM"
CANONICAL_SOURCE_PATH = "backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_core_ecosystem"

def get_catalog():
    domains = list_domains()
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "layer": "GLOBAL_BADA_BUSINESS_CORE",
        "canonical_ecosystem_id": CANONICAL_ECOSYSTEM_ID,
        "canonical_source_path": CANONICAL_SOURCE_PATH,
        "business_domain_count": len(domains),
        "service_work_business_capabilities": ["SERVICE", "WORK", "BUSINESS"],
        "mode": "CLASSIFICATION_ONLY",
        "provider_connections_verified": 0,
        "transaction_execution_enabled": False,
    }
