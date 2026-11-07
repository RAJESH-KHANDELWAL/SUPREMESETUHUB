"""Canonical category catalog for Men's Sexual Health."""
CATEGORY_ID = "mens_sexual_health"
CATEGORY_NAME = "Men's Sexual Health"
SUBDOMAINS = [
    "urology",
    "erectile health education",
    "ejaculatory health education",
    "male reproductive health",
    "clinical referral pathways"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
