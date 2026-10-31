"""Services, Platforms & Technology Integrations domain package; classification only, not verified live listings."""
DOMAIN_ID = "services_platforms_integrations"
DOMAIN_NAME = "Services, Platforms & Technology Integrations"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "cloud_hosting",
    "domains_dns",
    "website_platforms",
    "payments",
    "banking_fintech",
    "identity_verification",
    "communications",
    "crm_sales",
    "accounting_erp",
    "hr_payroll",
    "marketplaces",
    "booking_reservations",
    "delivery_logistics",
    "analytics_reporting",
    "automation_workflows",
    "developer_apis",
    "security_compliance",
    "customer_support",
    "document_signature",
    "ecommerce_integrations",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
