"""Canonical category catalog for Consultants, Advisors & Professional Services."""
CATEGORY_ID = "consultants_advisors_professional_services"
CATEGORY_NAME = "Consultants, Advisors & Professional Services"
SUBDOMAINS = [
    "sexual wellness consultants",
    "healthcare business advisors",
    "legal advisors",
    "privacy consultants",
    "compliance professionals"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
