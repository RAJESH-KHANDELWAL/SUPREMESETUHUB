"""Canonical category catalog for Adult Wellness Products & Commerce."""
CATEGORY_ID = "adult_wellness_products_commerce"
CATEGORY_NAME = "Adult Wellness Products & Commerce"
SUBDOMAINS = [
    "intimate hygiene",
    "condoms and protection",
    "personal lubricants",
    "wellness devices",
    "retail and wholesale"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
