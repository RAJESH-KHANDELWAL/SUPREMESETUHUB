"""Canonical category catalog for Adult Industry Work, Jobs & Careers."""
CATEGORY_ID = "adult_work_jobs_careers"
CATEGORY_NAME = "Adult Industry Work, Jobs & Careers"
SUBDOMAINS = [
    "lawful adult-industry roles",
    "healthcare careers",
    "education careers",
    "media production careers",
    "freelance services"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
