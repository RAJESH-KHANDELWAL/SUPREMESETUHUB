"""Safety governance for lawful adult-only platforms. No sexual content is generated or hosted."""
from dataclasses import dataclass
@dataclass(frozen=True)
class AdultPlatformPolicy:
    age_assurance_enabled: bool
    consent_controls_enabled: bool
    nonconsensual_content_reporting: bool
    takedown_workflow_enabled: bool
    privacy_review_complete: bool
    human_moderation_available: bool
    jurisdiction_review_complete: bool
    orientation_inference_enabled: bool = False
    viewer_orientation_profiling_enabled: bool = False
def validate_adult_platform_policy(policy):
    checks = {
      "age_assurance_required": policy.age_assurance_enabled,
      "consent_controls_required": policy.consent_controls_enabled,
      "reporting_mechanism_required": policy.nonconsensual_content_reporting,
      "takedown_workflow_required": policy.takedown_workflow_enabled,
      "privacy_review_required": policy.privacy_review_complete,
      "human_moderation_required": policy.human_moderation_available,
      "jurisdiction_review_required": policy.jurisdiction_review_complete,
      "orientation_inference_must_remain_disabled": not policy.orientation_inference_enabled,
      "viewer_orientation_profiling_must_remain_disabled": not policy.viewer_orientation_profiling_enabled,
    }
    return tuple(name for name, passed in checks.items() if not passed)

def adult_content_classification_contract():
    return {
        "taxonomy_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/adult_media_pornography_18_plus/classification_taxonomy.json",
        "orientation_labels": ["STRAIGHT", "GAY", "BISEXUAL", "OTHER", "UNSPECIFIED"],
        "orientation_inference_enabled": False,
        "viewer_orientation_profiling_enabled": False,
        "participant_configuration_is_separate": True,
        "scope": "CONTENT_METADATA_ONLY",
    }
