"""Canonical category catalog for Adult Training, Certification & Professional Development."""
CATEGORY_ID = "adult_training_certification_development"
CATEGORY_NAME = "Adult Training, Certification & Professional Development"
SUBDOMAINS = [
    "professional training",
    "continuing education",
    "credential directories",
    "workplace safety",
    "ethics and safeguarding"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
