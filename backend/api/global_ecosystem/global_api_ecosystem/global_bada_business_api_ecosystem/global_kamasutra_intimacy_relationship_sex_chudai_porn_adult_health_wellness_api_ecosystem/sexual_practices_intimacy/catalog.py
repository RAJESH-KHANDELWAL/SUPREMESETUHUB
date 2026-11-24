"""Canonical category catalog for Sexual Practices & Intimacy."""
CATEGORY_ID = "sexual_practices_intimacy"
CATEGORY_NAME = "Sexual Practices & Intimacy"
SUBDOMAINS = [
    "adult intimacy education",
    "sexual communication",
    "consensual adult practices",
    "intimacy skills",
    "privacy and boundaries"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
