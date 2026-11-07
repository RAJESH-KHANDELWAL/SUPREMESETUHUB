"""Canonical category catalog for Marriage & Married Life."""
CATEGORY_ID = "marriage_married_life"
CATEGORY_NAME = "Marriage & Married Life"
SUBDOMAINS = [
    "newly married couples",
    "marital communication",
    "marriage enrichment",
    "marital counselling referrals"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
