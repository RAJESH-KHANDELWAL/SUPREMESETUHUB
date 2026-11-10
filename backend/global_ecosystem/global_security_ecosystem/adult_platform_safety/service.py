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
def validate_adult_platform_policy(policy):
    checks = {
      "age_assurance_required": policy.age_assurance_enabled,
      "consent_controls_required": policy.consent_controls_enabled,
      "reporting_mechanism_required": policy.nonconsensual_content_reporting,
      "takedown_workflow_required": policy.takedown_workflow_enabled,
      "privacy_review_required": policy.privacy_review_complete,
      "human_moderation_required": policy.human_moderation_available,
      "jurisdiction_review_required": policy.jurisdiction_review_complete,
    }
    return tuple(name for name, passed in checks.items() if not passed)
