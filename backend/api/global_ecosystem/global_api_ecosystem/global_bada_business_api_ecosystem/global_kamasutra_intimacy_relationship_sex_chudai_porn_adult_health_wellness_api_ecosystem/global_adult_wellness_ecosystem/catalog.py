"""Canonical category catalog for Global Adult Wellness Ecosystem."""
CATEGORY_ID = "global_adult_wellness_ecosystem"
CATEGORY_NAME = "Global Adult Wellness Ecosystem"
SUBDOMAINS = [
    "country and jurisdiction taxonomy",
    "international provider schemas",
    "cross-border trade classification",
    "localisation",
    "global compliance references"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
