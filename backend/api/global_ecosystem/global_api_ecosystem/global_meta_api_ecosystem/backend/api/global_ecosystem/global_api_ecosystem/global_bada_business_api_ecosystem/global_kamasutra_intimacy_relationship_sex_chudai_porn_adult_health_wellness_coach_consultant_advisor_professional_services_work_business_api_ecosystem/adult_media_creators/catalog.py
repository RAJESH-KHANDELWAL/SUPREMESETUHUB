"""Canonical category catalog for Adult Media & Creator Businesses."""
CATEGORY_ID = "adult_media_creators"
CATEGORY_NAME = "Adult Media & Creator Businesses"
SUBDOMAINS = [
    "adult creator platforms",
    "talent management",
    "production services",
    "subscription platforms",
    "copyright and consent workflows"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
