"""Canonical category catalog for Adult Law, Safety & Compliance."""
CATEGORY_ID = "adult_law_safety_compliance"
CATEGORY_NAME = "Adult Law, Safety & Compliance"
SUBDOMAINS = [
    "adult-only access controls",
    "informed consent",
    "privacy and data protection",
    "content legality review",
    "anti-trafficking safeguards",
    "child safety"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
