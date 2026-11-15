"""Canonical category catalog for Adult Dating & GF-BF Relationships."""
CATEGORY_ID = "dating_gf_bf_relationships"
CATEGORY_NAME = "Adult Dating & GF-BF Relationships"
SUBDOMAINS = [
    "adult dating",
    "boyfriend-girlfriend relationships",
    "partner compatibility",
    "dating safety",
    "relationship expectations"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
