"""Canonical Global AI CORE registry; metadata only."""
from copy import deepcopy
AI_PROVIDERS=[
    {
        "provider_id": "openai",
        "provider_name": "OpenAI",
        "provider_type": "model_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/openai_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/openai_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "anthropic",
        "provider_name": "Anthropic",
        "provider_type": "model_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/anthropic_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "google",
        "provider_name": "Google AI",
        "provider_type": "model_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "aws",
        "provider_name": "AWS AI",
        "provider_type": "cloud_ai_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/aws_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "microsoft",
        "provider_name": "Microsoft AI",
        "provider_type": "cloud_ai_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/microsoft_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/microsoft_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "ibm",
        "provider_name": "IBM watsonx",
        "provider_type": "enterprise_ai_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/ibm_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/ibm_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "meta",
        "provider_name": "Meta AI",
        "provider_type": "model_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/meta_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/meta_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "apple",
        "provider_name": "Apple Intelligence",
        "provider_type": "on_device_ai_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/apple_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "nvidia",
        "provider_name": "NVIDIA AI",
        "provider_type": "ai_infrastructure_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/nvidia_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/nvidia_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "cohere",
        "provider_name": "Cohere",
        "provider_type": "model_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/cohere_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "mistral",
        "provider_name": "Mistral AI",
        "provider_type": "model_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/mistral_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/mistral_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "deepseek",
        "provider_name": "DeepSeek",
        "provider_type": "model_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/deepseek_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/deepseek_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "huggingface",
        "provider_name": "Hugging Face",
        "provider_type": "model_hub_and_inference",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/huggingface_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/huggingface_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "oracle",
        "provider_name": "Oracle AI",
        "provider_type": "enterprise_ai_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/oracle_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/oracle_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "adobe",
        "provider_name": "Adobe Firefly",
        "provider_type": "creative_ai_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/adobe_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/adobe_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "cloudflare",
        "provider_name": "Cloudflare AI",
        "provider_type": "edge_ai_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/global_cloudflare_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/cloudflare_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    },
    {
        "provider_id": "nsfwinfra",
        "provider_name": "NSFWInfra",
        "provider_type": "specialized_generation_platform",
        "core_package": "backend/core/global_ecosystem/global_core_ecosystem/nsfwinfra_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/nsfwinfra_ai_api_ecosystem",
        "integration_status": "NOT_CONFIGURED",
        "facade_status": "REGISTERED_NOT_LIVE_VERIFIED",
        "live_connection_verified": False,
        "capability_coverage_verified": False
    }
]
ADJACENT_INTEGRATIONS=[
    {
        "partner_id": "abelohost",
        "partner_name": "AbeloHost",
        "classification": "adult_friendly_hosting",
        "description": "Adult-friendly hosting and infrastructure",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/abelohost_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_hosting_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/abelohost_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "bangbros",
        "partner_name": "BangBros",
        "classification": "content_publisher",
        "description": "Adult entertainment studio and content brand",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/bangbros_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/bangbros_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "brazzers",
        "partner_name": "Brazzers",
        "classification": "content_publisher",
        "description": "Adult entertainment studio and content brand",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/brazzers_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/brazzers_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "ccbill",
        "partner_name": "CCBill",
        "classification": "payment_processing",
        "description": "Specialist payment processing",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/ccbill_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_payment_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/ccbill_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": False,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "clips4sale",
        "partner_name": "Clips4Sale",
        "classification": "creator_marketplace",
        "description": "Clip store and creator marketplace",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/clips4sale_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_platforms_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/clips4sale_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "crakrevenue",
        "partner_name": "CrakRevenue",
        "classification": "affiliate_advertising",
        "description": "Adult affiliate marketing network",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/crakrevenue_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_integrations_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/crakrevenue_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "epoch",
        "partner_name": "Epoch",
        "classification": "payment_processing",
        "description": "Online payment processing and billing",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/epoch_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_payment_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/epoch_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": False,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "evilangel",
        "partner_name": "Evil Angel",
        "classification": "content_publisher",
        "description": "Adult entertainment studio and content distributor",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/evilangel_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/evilangel_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "exoclick",
        "partner_name": "ExoClick",
        "classification": "advertising_network",
        "description": "Digital advertising and affiliate network",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/exoclick_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_integrations_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/exoclick_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "fansly",
        "partner_name": "Fansly",
        "classification": "creator_subscriptions",
        "description": "Creator subscriptions and paid-content platform",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/fansly_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_platforms_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/fansly_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "faphouse",
        "partner_name": "FapHouse",
        "classification": "creator_marketplace",
        "description": "Adult video and clip platform",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/faphouse_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_platforms_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/faphouse_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "loyalfans",
        "partner_name": "LoyalFans",
        "classification": "creator_subscriptions",
        "description": "Creator subscriptions and monetization platform",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/loyalfans_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_platforms_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/loyalfans_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "manyvids",
        "partner_name": "ManyVids",
        "classification": "creator_marketplace",
        "description": "Creator marketplace and paid video platform",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/manyvids_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_platforms_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/manyvids_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "naughtyamerica",
        "partner_name": "Naughty America",
        "classification": "content_publisher",
        "description": "Adult entertainment studio and content distributor",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/naughtyamerica_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/naughtyamerica_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "onlyfans",
        "partner_name": "OnlyFans",
        "classification": "creator_subscriptions",
        "description": "Creator subscriptions and paid-content platform",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/onlyfans_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_platforms_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/onlyfans_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "paxum",
        "partner_name": "Paxum",
        "classification": "payments_and_payouts",
        "description": "Digital payments and payouts",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/paxum_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_payment_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/paxum_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": False,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "pornhub",
        "partner_name": "Pornhub",
        "classification": "video_platform",
        "description": "Adult video-sharing platform",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/pornhub_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/pornhub_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "realitykings",
        "partner_name": "Reality Kings",
        "classification": "content_publisher",
        "description": "Adult entertainment studio and content brand",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/realitykings_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/realitykings_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "segpay",
        "partner_name": "Segpay",
        "classification": "payment_processing",
        "description": "Specialist payment processing and recurring billing",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/segpay_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_payment_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/segpay_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": False,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "trafficjunky",
        "partner_name": "TrafficJunky",
        "classification": "advertising_network",
        "description": "Adult-focused advertising network",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/trafficjunky_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_integrations_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/trafficjunky_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "verotel",
        "partner_name": "Verotel",
        "classification": "payment_processing",
        "description": "Specialist online payments and billing",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/verotel_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_payment_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/verotel_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": False,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "vicetemple",
        "partner_name": "ViceTemple",
        "classification": "adult_focused_hosting",
        "description": "Adult-focused hosting and website infrastructure",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/vicetemple_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_hosting_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/vicetemple_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "xhamster",
        "partner_name": "xHamster",
        "classification": "video_platform",
        "description": "Adult video platform and content distribution",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/xhamster_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/xhamster_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    },
    {
        "partner_id": "xvideos",
        "partner_name": "XVideos",
        "classification": "video_platform",
        "description": "Adult video-sharing platform",
        "legacy_package": "backend/core/global_ecosystem/global_core_ecosystem/global_ai_core_ecosystem/xvideos_ai_core_ecosystem",
        "canonical_domain_core_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_video_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/xvideos_ai_api_ecosystem",
        "status": "ADJACENT_INTEGRATION_CATALOG_ONLY",
        "is_ai_model_provider": False,
        "age_restricted_or_adult_industry": True,
        "api_documentation_verified": False,
        "live_connection_verified": False
    }
]
CAPABILITIES=[
    {
        "capability_id": "text_generation",
        "name": "Text generation",
        "modality": "text",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "reasoning",
        "name": "Reasoning",
        "modality": "text",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "vision",
        "name": "Image and visual understanding",
        "modality": "image",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "image_generation",
        "name": "Image generation and editing",
        "modality": "image",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "audio_input",
        "name": "Audio understanding and transcription",
        "modality": "audio",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "audio_output",
        "name": "Speech and audio generation",
        "modality": "audio",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "video",
        "name": "Video understanding and generation",
        "modality": "video",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "embeddings",
        "name": "Embeddings",
        "modality": "vector",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "reranking",
        "name": "Semantic reranking",
        "modality": "vector",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "code",
        "name": "Code generation and analysis",
        "modality": "code",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "document_intelligence",
        "name": "Document intelligence",
        "modality": "document",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "agents",
        "name": "Agent and tool orchestration",
        "modality": "workflow",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "moderation",
        "name": "Safety moderation",
        "modality": "safety",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "fine_tuning",
        "name": "Model fine-tuning",
        "modality": "training",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    },
    {
        "capability_id": "evaluation",
        "name": "Model evaluation",
        "modality": "quality",
        "status": "CATALOG_CONTRACT_ONLY",
        "provider_support_verified": False
    }
]
SERVICES=[
    {
        "service_id": "inference",
        "name": "Model inference",
        "description": "Provider-neutral text and multimodal inference contract.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "embeddings",
        "name": "Embedding service",
        "description": "Vector generation contract for semantic retrieval.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "reranking",
        "name": "Reranking service",
        "description": "Relevance scoring contract for retrieved results.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "image-generation",
        "name": "Image generation",
        "description": "Image generation and editing capability boundary.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "audio",
        "name": "Audio service",
        "description": "Speech input, transcription and audio output boundary.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "video",
        "name": "Video service",
        "description": "Video understanding and generation boundary.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "document-ai",
        "name": "Document intelligence",
        "description": "Document parsing, extraction and Q&A boundary.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "agent-orchestration",
        "name": "Agent orchestration",
        "description": "Tool-using agent workflow contract; runtime disabled.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "model-evaluation",
        "name": "Model evaluation",
        "description": "Quality and performance evaluation contract.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    },
    {
        "service_id": "moderation",
        "name": "Safety moderation",
        "description": "Input and output policy screening contract.",
        "status": "CONTRACT_DEFINED_NOT_EXECUTABLE"
    }
]
TOOLS=[
    {
        "tool_id": "structured-output",
        "name": "Structured output",
        "purpose": "Validate model responses against schemas.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "function-calling",
        "name": "Function calling",
        "purpose": "Represent typed tool calls and validated arguments.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "prompt-templates",
        "name": "Prompt templates",
        "purpose": "Version system and task prompts.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "retrieval",
        "name": "Retrieval",
        "purpose": "Connect model workflows to indexed knowledge.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "file-processing",
        "name": "File processing",
        "purpose": "Prepare documents and media for model input.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "web-search",
        "name": "Web search",
        "purpose": "Controlled external information retrieval interface.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "code-execution",
        "name": "Code execution",
        "purpose": "Sandbox boundary for code workflows.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "safety-guardrails",
        "name": "Safety guardrails",
        "purpose": "Apply input, output and tool-use policy checks.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    },
    {
        "tool_id": "token-usage",
        "name": "Token and usage accounting",
        "purpose": "Normalize provider usage and cost metadata.",
        "status": "SPECIFIED_NOT_EXECUTABLE"
    }
]
INTEGRATIONS=[
    {
        "integration_id": "provider-adapters",
        "name": "AI provider adapters",
        "target": "Registered AI model and cloud providers",
        "status": "PLANNED_NOT_CONNECTED"
    },
    {
        "integration_id": "vector-databases",
        "name": "Vector databases",
        "target": "Vector storage and retrieval backends",
        "status": "PLANNED_NOT_CONNECTED"
    },
    {
        "integration_id": "object-storage",
        "name": "Object storage",
        "target": "Document and media assets",
        "status": "PLANNED_NOT_CONNECTED"
    },
    {
        "integration_id": "secrets-management",
        "name": "Secrets management",
        "target": "Environment and managed secrets",
        "status": "PLANNED_NOT_CONNECTED"
    },
    {
        "integration_id": "observability",
        "name": "AI observability",
        "target": "Logs, traces, latency, tokens and cost telemetry",
        "status": "PLANNED_NOT_CONNECTED"
    },
    {
        "integration_id": "workflow-runtime",
        "name": "Workflow runtime",
        "target": "Asynchronous jobs and agent workflows",
        "status": "PLANNED_NOT_CONNECTED"
    }
]
def _copy(items): return deepcopy(items)
def list_ai_providers(): return _copy(AI_PROVIDERS)
def get_ai_provider(provider_id):
 key=str(provider_id).strip().casefold()
 return next((x for x in _copy(AI_PROVIDERS) if x["provider_id"]==key),None)
def list_adjacent_integrations(): return _copy(ADJACENT_INTEGRATIONS)
def get_adjacent_integration(partner_id):
 key=str(partner_id).strip().casefold()
 return next((x for x in _copy(ADJACENT_INTEGRATIONS) if x["partner_id"]==key),None)
