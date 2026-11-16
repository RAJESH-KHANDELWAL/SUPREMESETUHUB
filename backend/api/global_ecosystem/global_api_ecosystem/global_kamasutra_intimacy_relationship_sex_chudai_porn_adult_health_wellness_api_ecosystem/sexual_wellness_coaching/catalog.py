"""Canonical category catalog for Sexual Wellness Coaching."""
CATEGORY_ID = "sexual_wellness_coaching"
CATEGORY_NAME = "Sexual Wellness Coaching"
SUBDOMAINS = [
    "non-clinical adult education coaching",
    "wellness goal setting",
    "communication skills",
    "coach verification",
    "scope-of-practice boundaries"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
