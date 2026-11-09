"""Canonical category catalog for Adult Relationships & Compatibility."""
CATEGORY_ID = "adult_relationships_compatibility"
CATEGORY_NAME = "Adult Relationships & Compatibility"
SUBDOMAINS = [
    "single adults",
    "consenting adult partnerships",
    "relationship psychology",
    "trust and conflict resolution",
    "LGBTQ+ adult relationship wellness"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
