"""Canonical Global Finance, Banking, Insurance and Payment Gateway catalogue."""
from copy import deepcopy
from .domain_catalog import DOMAIN_DEFINITIONS, DOMAIN_PACKAGES
from .product_catalog import FINANCE_PACKAGES
FINANCE_ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-CORE-ECOSYSTEM"
FINANCE_ECOSYSTEM_NAME = "GLOBAL FINANCE BANKING INSURANCE FINANCIAL PAYMENT GATEWAY CORE ECOSYSTEM"
FINANCE_ECOSYSTEM_PATH = "backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_gateway_core_ecosystem"
FINANCE_ECOSYSTEM_CATALOG = {
 "ecosystem_id": FINANCE_ECOSYSTEM_ID, "name": FINANCE_ECOSYSTEM_NAME,
 "ecosystem_type": "GLOBAL_DOMAIN_CORE", "parent_id": "GLOBAL-CORE-ECOSYSTEM",
 "repository_path": FINANCE_ECOSYSTEM_PATH, "status": "REGISTERED", "enabled": True,
 "transaction_execution_enabled": False, "provider_connections_verified": False,
 "domain_count": len(DOMAIN_DEFINITIONS), "package_count": len(FINANCE_PACKAGES),
 "capabilities": ["BANKING","INSURANCE","CAPITAL_MARKETS","LENDING_AND_CREDIT","ACCOUNTING_AND_TAX",
 "TREASURY","RISK_AND_COMPLIANCE","FINTECH_AND_OPEN_FINANCE","PAYMENT_GATEWAYS_AND_ACQUIRING",
 "PAYMENT_RAILS_AND_WALLETS","BILLING_SETTLEMENT_AND_PAYOUTS","INTERNATIONAL_FINANCE","PUBLIC_FINANCE"],
 "domains": [{"domain_id": k, "name": v["name"], "purpose": v["purpose"],
 "package_names": list(DOMAIN_PACKAGES[k]), "status": "CORE_CATALOG_ONLY"} for k,v in DOMAIN_DEFINITIONS.items()],
 "children": [dict(x) for x in FINANCE_PACKAGES],
}
def get_finance_core_catalog() -> dict:
    return deepcopy(FINANCE_ECOSYSTEM_CATALOG)
def list_finance_core_modules() -> list[dict]:
    return [dict(x) for x in FINANCE_PACKAGES]
