"""Canonical category catalog for Adult Business Management & Development."""
CATEGORY_ID = "adult_business_management_development"
CATEGORY_NAME = "Adult Business Management & Development"
SUBDOMAINS = [
    "business planning",
    "operations",
    "marketing compliance",
    "partnerships",
    "franchising and licensing"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
