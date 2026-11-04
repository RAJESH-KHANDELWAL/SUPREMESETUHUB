"""Canonical category catalog for Lawful Adult Entertainment & Porn Media."""
CATEGORY_ID = "adult_entertainment_porn_media"
CATEGORY_NAME = "Lawful Adult Entertainment & Porn Media"
SUBDOMAINS = [
    "lawful adult film production",
    "adult media distribution",
    "adult creator economy",
    "age assurance",
    "content licensing and moderation"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
