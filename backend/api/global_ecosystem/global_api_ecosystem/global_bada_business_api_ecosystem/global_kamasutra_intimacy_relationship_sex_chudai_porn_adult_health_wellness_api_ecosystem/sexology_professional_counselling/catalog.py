"""Canonical category catalog for Sexology & Professional Counselling."""
CATEGORY_ID = "sexology_professional_counselling"
CATEGORY_NAME = "Sexology & Professional Counselling"
SUBDOMAINS = [
    "sexologists",
    "certified sex therapists",
    "clinical psychologists",
    "counselling directories",
    "credential verification"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
