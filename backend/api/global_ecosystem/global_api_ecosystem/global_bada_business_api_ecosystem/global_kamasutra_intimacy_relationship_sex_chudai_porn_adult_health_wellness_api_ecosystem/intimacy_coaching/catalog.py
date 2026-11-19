"""Canonical category catalog for Intimacy Coaching."""
CATEGORY_ID = "intimacy_coaching"
CATEGORY_NAME = "Intimacy Coaching"
SUBDOMAINS = [
    "intimacy education",
    "emotional connection",
    "couple exercises for adults",
    "professional boundaries",
    "referral protocols"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
