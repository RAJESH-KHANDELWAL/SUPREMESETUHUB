"""Provider-owned NSFWInfra API ecosystem catalog.

This is an adult-content AI infrastructure provider. Metadata describes
documented API areas; it does not establish customer connectivity or entitlement.
"""
SERVICE_FAMILIES = [
    "IMAGE_GENERATION",
    "IMAGE_EDITING",
    "ANIME_GENERATION",
    "TEXT_TO_VIDEO",
    "IMAGE_TO_VIDEO",
    "IMAGE_VIDEO_EFFECTS",
    "ASYNC_JOBS",
    "WEBHOOKS",
    "SIGNED_UPLOADS",
    "ACCOUNT_LIMITS",
]

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "nsfwinfra",
    "name": "NSFWINFRA API ECOSYSTEM",
    "vendor": "NSFWInfra",
    "provider_type": "ADULT_AI_INFRASTRUCTURE",
    "families": ["AI", "IMAGE", "VIDEO"],
    "service_families": SERVICE_FAMILIES,
    "service_family_count": len(SERVICE_FAMILIES),
    "base_url": "https://api.nsfwinfra.com",
    "api_version": "v1",
    "authentication": "Bearer API key",
    "required_configuration": ["NSFWINFRA_API_KEY"],
    "runtime_adapter_path": "backend/engine/ai/manager.py",
    "infrastructure_client_path": "backend/infrastructure/nsfwinfra.py",
    "implementation_status": "IMAGE_GENERATION_ADAPTER_PRESENT_UNVERIFIED",
    "live_connection_verified": False,
    "adult_content": True,
    "minimum_user_age": 18,
    "safety_requirements": [
        "Enforce age and jurisdiction eligibility",
        "Prohibit sexual content involving minors or age-ambiguous subjects",
        "Prohibit non-consensual intimate imagery and sexual deepfakes",
        "Require lawful rights and consent for submitted source images",
        "Keep API keys server-side and never expose them to browsers",
    ],
    "important_limitations": [
        "Current project runtime adapter implements image generation only",
        "Documented video, editing, effects, jobs, uploads and webhook APIs are cataloged but not all implemented",
        "A successful API request is not a full account or production-readiness verification",
    ],
}
