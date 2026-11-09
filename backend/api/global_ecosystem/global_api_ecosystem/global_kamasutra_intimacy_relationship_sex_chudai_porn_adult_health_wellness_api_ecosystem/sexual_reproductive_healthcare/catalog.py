"""Canonical category catalog for Sexual & Reproductive Healthcare."""
CATEGORY_ID = "sexual_reproductive_healthcare"
CATEGORY_NAME = "Sexual & Reproductive Healthcare"
SUBDOMAINS = [
    "sexual health education",
    "reproductive health",
    "fertility and conception",
    "STI information and clinical referrals",
    "diagnostics and telehealth"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
