"""Canonical category catalog for Adult Technology, Software & APIs."""
CATEGORY_ID = "adult_technology_software_apis"
CATEGORY_NAME = "Adult Technology, Software & APIs"
SUBDOMAINS = [
    "age assurance integrations",
    "consent management",
    "privacy systems",
    "content moderation",
    "secure platform APIs"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
