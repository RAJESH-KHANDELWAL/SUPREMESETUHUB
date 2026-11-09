"""Canonical category catalog for Women's Sexual Health."""
CATEGORY_ID = "womens_sexual_health"
CATEGORY_NAME = "Women's Sexual Health"
SUBDOMAINS = [
    "gynaecology",
    "menstrual health",
    "menopause",
    "female reproductive health",
    "clinical referral pathways"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
