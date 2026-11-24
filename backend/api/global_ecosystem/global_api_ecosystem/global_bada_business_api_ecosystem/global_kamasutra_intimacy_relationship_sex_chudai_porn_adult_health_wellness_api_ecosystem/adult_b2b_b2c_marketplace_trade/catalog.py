"""Canonical category catalog for Adult B2B, B2C, Marketplace & Trade."""
CATEGORY_ID = "adult_b2b_b2c_marketplace_trade"
CATEGORY_NAME = "Adult B2B, B2C, Marketplace & Trade"
SUBDOMAINS = [
    "B2B supplier directory",
    "B2C marketplace taxonomy",
    "wholesale and distribution",
    "import and export",
    "payments and consumer protection"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
