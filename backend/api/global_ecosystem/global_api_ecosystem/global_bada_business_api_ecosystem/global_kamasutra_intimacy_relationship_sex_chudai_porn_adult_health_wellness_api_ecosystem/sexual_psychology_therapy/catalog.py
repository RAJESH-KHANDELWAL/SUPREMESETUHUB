"""Canonical category catalog for Sexual Psychology & Therapy."""
CATEGORY_ID = "sexual_psychology_therapy"
CATEGORY_NAME = "Sexual Psychology & Therapy"
SUBDOMAINS = [
    "sexual psychology",
    "sex therapy directory",
    "body image and confidence",
    "sexual anxiety support",
    "trauma-informed referrals"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
