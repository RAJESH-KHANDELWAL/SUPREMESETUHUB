"""Canonical category catalog for Kamasutra & Ancient Knowledge."""
CATEGORY_ID = "kamasutra_ancient_knowledge"
CATEGORY_NAME = "Kamasutra & Ancient Knowledge"
SUBDOMAINS = [
    "Vatsyayana literature",
    "ancient Indian intimacy knowledge",
    "historical texts and commentary",
    "cross-cultural historical research"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]
