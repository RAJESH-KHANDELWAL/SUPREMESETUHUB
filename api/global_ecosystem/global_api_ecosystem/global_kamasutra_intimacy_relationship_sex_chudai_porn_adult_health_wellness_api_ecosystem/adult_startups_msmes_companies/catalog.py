"""Canonical category catalog for Adult Startups, MSMEs & Companies."""
CATEGORY_ID = "adult_startups_msmes_companies"
CATEGORY_NAME = "Adult Startups, MSMEs & Companies"
SUBDOMAINS = [
    "wellness startups",
    "healthcare companies",
    "product manufacturers",
    "adult media companies",
    "MSME support"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
