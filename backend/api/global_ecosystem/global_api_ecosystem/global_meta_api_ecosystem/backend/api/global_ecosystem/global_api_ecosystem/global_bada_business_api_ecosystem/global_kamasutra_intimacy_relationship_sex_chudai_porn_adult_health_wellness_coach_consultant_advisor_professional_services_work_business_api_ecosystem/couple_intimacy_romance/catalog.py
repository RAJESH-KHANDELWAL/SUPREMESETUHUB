"""Canonical category catalog for Couple Intimacy & Romance."""
CATEGORY_ID = "couple_intimacy_romance"
CATEGORY_NAME = "Couple Intimacy & Romance"
SUBDOMAINS = [
    "romance and affection",
    "emotional intimacy",
    "physical intimacy education",
    "couple communication",
    "long-distance couples"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
