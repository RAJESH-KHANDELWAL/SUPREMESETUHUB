"""Canonical category catalog for Adult Media & Creator Businesses."""
CATEGORY_ID = "adult_media_creators"
CATEGORY_NAME = "Adult Media & Creator Businesses"
SUBDOMAINS = [
    "adult creator platforms",
    "talent management",
    "production services",
    "subscription platforms",
    "copyright and consent workflows"
]
COVERAGE = ("india", "global")
ACCESS_CLASSIFICATION = "18_plus"
STATUS = "taxonomy_scaffold"


def list_subdomains():
    return [{"id": value, "name": value.replace("_", " ").title()} for value in SUBDOMAINS]

ORIENTATION_CONTENT_LABELS = ("STRAIGHT", "GAY", "BISEXUAL", "OTHER", "UNSPECIFIED")
CLASSIFICATION_TAXONOMY_REF = (
    "backend/core/global_ecosystem/global_core_ecosystem/"
    "global_people_life_core_ecosystem/adult_media_pornography_18_plus/classification_taxonomy.json"
)

def get_content_classification_catalog():
    return {
        "taxonomy_ref": CLASSIFICATION_TAXONOMY_REF,
        "orientation_labels": list(ORIENTATION_CONTENT_LABELS),
        "orientation_inference_enabled": False,
        "viewer_orientation_profiling_enabled": False,
        "participant_configuration_is_separate": True,
        "scope": "CONTENT_METADATA_ONLY",
    }
