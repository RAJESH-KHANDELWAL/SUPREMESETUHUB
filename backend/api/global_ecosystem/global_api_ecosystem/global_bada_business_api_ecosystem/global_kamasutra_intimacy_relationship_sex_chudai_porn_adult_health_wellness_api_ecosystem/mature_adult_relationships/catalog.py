"""Canonical category catalog for Mature Adult Relationships."""
CATEGORY_ID = "mature_adult_relationships"
CATEGORY_NAME = "Mature Adult Relationships"
SUBDOMAINS = [
    "mature adult dating",
    "senior adult relationships",
    "widowed and divorced adults",
    "healthy ageing and intimacy",
    "consent and safety"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
