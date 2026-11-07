"""Canonical category catalog for Sexual Health Research & Innovation."""
CATEGORY_ID = "sexual_health_research_innovation"
CATEGORY_NAME = "Sexual Health Research & Innovation"
SUBDOMAINS = [
    "sexual health research",
    "reproductive science",
    "medical technology",
    "evidence review",
    "research ethics"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
