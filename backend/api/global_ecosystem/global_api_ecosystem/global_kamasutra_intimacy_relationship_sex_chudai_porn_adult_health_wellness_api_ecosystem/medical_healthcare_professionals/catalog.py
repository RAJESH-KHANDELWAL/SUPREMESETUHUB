"""Canonical category catalog for Medical & Healthcare Professionals."""
CATEGORY_ID = "medical_healthcare_professionals"
CATEGORY_NAME = "Medical & Healthcare Professionals"
SUBDOMAINS = [
    "urologists",
    "gynaecologists",
    "reproductive specialists",
    "psychiatrists",
    "telehealth providers"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
