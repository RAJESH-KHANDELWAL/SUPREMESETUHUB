"""Cross-domain governance requirements and lawful adult-only safeguards."""
from .workload_domains import GEOGRAPHIC_SCOPES

BASELINE_CONTROLS = (
    "data_minimization", "encryption_in_transit_and_at_rest",
    "least_privilege_access", "audit_logging", "backup_and_recovery",
    "incident_response", "jurisdictional_privacy_review",
)

ADULT_ONLY_CONTROLS = (
    "effective_age_assurance", "adults_only_access_enforcement",
    "informed_consent_and_performer_rights", "content_moderation",
    "reporting_and_takedown", "non_consensual_content_prevention",
    "anti_trafficking_and_exploitation_controls", "privacy_preserving_records",
    "jurisdiction_specific_legal_review",
)

PROHIBITED_CONTENT_AND_ACTIVITIES = (
    "sexual_content_involving_minors",
    "non_consensual_intimate_imagery",
    "coercion_or_sexual_extortion",
    "trafficking_or_exploitation",
    "hidden_camera_or_stolen_intimate_material",
)

def controls_for_domain(domain_id):
    controls = list(BASELINE_CONTROLS)
    if domain_id == "adult_only_services":
        controls.extend(ADULT_ONLY_CONTROLS)
    return {
        "domain_id": domain_id,
        "controls": controls,
        "prohibited": list(PROHIBITED_CONTENT_AND_ACTIVITIES) if domain_id == "adult_only_services" else [],
        "geographic_review_required": True,
        "supported_geographic_scopes": list(GEOGRAPHIC_SCOPES),
    }

def validate_adult_only_deployment(age_restricted, age_assurance, consent_controls, legal_review):
    errors = []
    if not age_restricted:
        errors.append("adult-only deployment must enforce adults-only access")
    if not age_assurance:
        errors.append("effective age assurance is required")
    if not consent_controls:
        errors.append("consent and performer-rights controls are required")
    if not legal_review:
        errors.append("jurisdiction-specific legal review is required")
    return errors
