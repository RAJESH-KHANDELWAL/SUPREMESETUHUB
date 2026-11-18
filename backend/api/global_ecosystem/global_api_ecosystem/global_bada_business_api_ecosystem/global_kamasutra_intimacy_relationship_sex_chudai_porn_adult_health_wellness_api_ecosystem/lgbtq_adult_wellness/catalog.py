"""Canonical category catalog for LGBTQ+ Adult Wellness."""
CATEGORY_ID = "lgbtq_adult_wellness"
CATEGORY_NAME = "LGBTQ+ Adult Wellness"
SUBDOMAINS = [
    "inclusive sexual health education",
    "relationship wellness",
    "affirming professional directories",
    "privacy and safety",
    "country-specific access information"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
