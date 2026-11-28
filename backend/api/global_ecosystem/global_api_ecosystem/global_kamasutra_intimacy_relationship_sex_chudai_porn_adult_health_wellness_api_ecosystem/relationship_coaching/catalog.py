"""Canonical category catalog for Relationship Coaching."""
CATEGORY_ID = "relationship_coaching"
CATEGORY_NAME = "Relationship Coaching"
SUBDOMAINS = [
    "relationship skills coaching",
    "dating communication",
    "couple communication",
    "conflict navigation",
    "coach credentials"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
