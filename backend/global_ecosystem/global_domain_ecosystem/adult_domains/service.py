"""Requirements for lawful, consensual, adult-only domains."""
REQUIRED_CONTROLS = (
    "age_assurance", "informed_consent", "performer_release_records",
    "privacy_controls", "content_moderation", "reporting_and_takedown",
    "secure_payments", "jurisdiction_review",
)
EXCLUDED_USE_CASES = (
    "sexual_content_involving_minors", "non_consensual_intimate_imagery",
    "coercion", "trafficking", "sexual_extortion", "hidden_camera_content",
)

def get_adult_domain_requirements() -> dict:
    return {
        "domain_areas": [
            "adult_entertainment_platforms", "adult_creator_profiles",
            "adult_subscriptions", "lawful_content_distribution",
            "sexual_health_education", "consent_management",
            "age_assurance", "privacy_and_security", "moderation_and_takedowns",
        ],
        "required_controls": list(REQUIRED_CONTROLS),
        "excluded_use_cases": list(EXCLUDED_USE_CASES),
        "scope": "ADULTS_ONLY_LAWFUL_CONSENSUAL",
    }

def validate_adult_domain(controls) -> dict:
    supplied = set(controls)
    missing = [item for item in REQUIRED_CONTROLS if item not in supplied]
    return {
        "eligible_for_design_review": not missing,
        "missing_controls": missing,
        "required_controls": list(REQUIRED_CONTROLS),
        "excluded_use_cases": list(EXCLUDED_USE_CASES),
    }

__all__ = ["REQUIRED_CONTROLS", "EXCLUDED_USE_CASES", "get_adult_domain_requirements", "validate_adult_domain"]
