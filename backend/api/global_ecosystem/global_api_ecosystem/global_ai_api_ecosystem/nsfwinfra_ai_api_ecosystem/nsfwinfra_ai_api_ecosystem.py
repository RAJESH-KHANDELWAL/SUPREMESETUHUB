"""NSFWInfra AI category routing metadata.

The provider has an image-generation adapter in the runtime registry. This
record does not claim that a customer account has been connected or verified.
"""
PROVIDER_AI_ECOSYSTEM = {
    "provider_id": "nsfwinfra",
    "provider_catalog_path": "backend/api/global_ecosystem/global_api_ecosystem/nsfwinfra_api_ecosystem",
    "category": "AI",
    "capabilities": ["IMAGE_GENERATION", "IMAGE_EDITING", "ANIME_GENERATION"],
    "runtime_adapter_path": "backend/engine/ai/manager.py",
    "status": "RUNTIME_ADAPTER_PRESENT_UNVERIFIED",
    "live_connection_verified": False,
    "adult_content": True,
    "minimum_user_age": 18,
    "safety_requirements": [
        "Enforce age and jurisdiction eligibility before access",
        "Reject sexual content involving minors or age-ambiguous subjects",
        "Reject non-consensual intimate imagery and sexual deepfakes",
        "Require lawful rights and consent for uploaded source images",
    ],
}
