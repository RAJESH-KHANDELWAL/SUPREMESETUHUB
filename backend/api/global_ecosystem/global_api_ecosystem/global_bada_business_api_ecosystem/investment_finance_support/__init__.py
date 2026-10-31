"""Finance, Investment & Business Support domain package; classification only, not verified live listings."""
DOMAIN_ID = "investment_finance_support"
DOMAIN_NAME = "Finance, Investment & Business Support"
ADULT_RESTRICTED = false
DEFAULT_DISCOVERY_ENABLED = true
SUBCATEGORY_IDS: tuple[str, ...] = (
    "personal_finance_education",
    "business_finance",
    "loans_credit",
    "banking_services",
    "insurance",
    "tax_services",
    "accounting_audit",
    "investment_education",
    "capital_raising",
    "grants_subsidies",
    "government_schemes",
    "msme_support",
    "export_import_support",
    "business_valuation",
    "risk_management",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
