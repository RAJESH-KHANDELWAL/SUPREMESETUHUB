"""Mandatory governance boundaries for adult wellness metadata."""
POLICY = {
    "adult_only": True,
    "minimum_age": 18,
    "age_assurance_required": True,
    "informed_consent_required": True,
    "rights_verification_required": True,
    "non_consensual_intimate_content_prohibited": True,
    "minors_and_child_sexual_abuse_material_prohibited": True,
    "exploitation_trafficking_and_coercion_prohibited": True,
    "privacy_by_design_required": True,
    "sensitive_health_data_prohibited_in_core_catalog": True,
    "clinical_services_require_licensed_professionals": True,
    "catalog_registration_is_not_provider_approval": True,
}
def get_policy() -> dict[str, object]:
    return dict(POLICY)
__all__ = ["POLICY", "get_policy"]
