"""Read-only canonical catalogue for finance ecosystem packages."""

from .domain_catalog import DOMAIN_NAMES, DOMAIN_PACKAGES

FINANCE_ECOSYSTEM_ID = "GLOBAL_FINANCE_BANKING_INSURANCE_FINANCIAL_PAYMENT_CORE_ECOSYSTEM"
FINANCE_ECOSYSTEM_CATALOG = {
    "ecosystem_id": FINANCE_ECOSYSTEM_ID,
    "repository_path": "backend/core/global_ecosystem/global_core_ecosystem/global_finance_banking_insurance_financial_payment_core_ecosystem",
    "domains": {
        domain_id: {
            "name": DOMAIN_NAMES[domain_id],
            "package_names": package_names,
        }
        for domain_id, package_names in DOMAIN_PACKAGES.items()
    },
}
