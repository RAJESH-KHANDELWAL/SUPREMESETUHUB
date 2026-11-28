"""Canonical category catalog for Bharat Adult Wellness Ecosystem."""
CATEGORY_ID = "bharat_adult_wellness_ecosystem"
CATEGORY_NAME = "Bharat Adult Wellness Ecosystem"
SUBDOMAINS = [
    "India market taxonomy",
    "Indian healthcare pathways",
    "Indian business directory schema",
    "Indian legal review references",
    "regional language education"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
