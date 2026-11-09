"""Canonical category catalog for Adult Body, Fitness & Intimacy Wellness."""
CATEGORY_ID = "adult_body_fitness_wellness"
CATEGORY_NAME = "Adult Body, Fitness & Intimacy Wellness (18+)"
SUBDOMAINS = [
    "adult body confidence and positive body image",
    "intimacy-related mobility and flexibility education",
    "pelvic-floor wellness education with qualified clinical referral boundaries",
    "adult fitness coaching for general wellbeing and intimacy confidence",
    "consent-first body awareness and non-clinical wellness education",
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
