"""Canonical category catalog for Family, Parenting & Reproductive Wellness."""
CATEGORY_ID = "family_parenting_reproductive_wellness"
CATEGORY_NAME = "Family, Parenting & Reproductive Wellness"
SUBDOMAINS = [
    "adult family relationship education",
    "family planning",
    "preconception education",
    "pregnancy planning",
    "postpartum relationship wellness",
    "responsible parenting education",
    "co-parenting communication",
    "adult family relationship counselling referrals"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
