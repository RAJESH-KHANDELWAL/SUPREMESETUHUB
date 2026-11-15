"""Canonical category catalog for Adult Sexual Education."""
CATEGORY_ID = "adult_sexual_education"
CATEGORY_NAME = "Adult Sexual Education"
SUBDOMAINS = [
    "adult human sexuality education",
    "anatomy and physiology",
    "consent and boundaries",
    "sexual literacy",
    "safer-sex education"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
