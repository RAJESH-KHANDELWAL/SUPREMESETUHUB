"""Canonical category catalog for Global Partnerships & Business Networking."""
CATEGORY_ID = "global_partnerships_networking"
CATEGORY_NAME = "Global Partnerships & Business Networking"
SUBDOMAINS = [
    "provider partnerships",
    "industry associations",
    "research collaborations",
    "business networking",
    "international events"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
