"""Bharat-to-global AI scope taxonomy and implementation maturity.

This is a scope/roadmap registry, not a claim that every listed capability is
implemented, connected to a live provider, or production-ready.
"""
from __future__ import annotations

from typing import Any


AI_MATURITY_LEVELS: tuple[dict[str, str], ...] = (
    {"id": "basic_task_ai", "name": "Basic / Task AI", "status": "ROADMAP"},
    {"id": "assistant_ai", "name": "Smart Assistant AI", "status": "ROADMAP"},
    {"id": "generative_ai", "name": "Generative AI", "status": "CATALOGED"},
    {"id": "reasoning_ai", "name": "Reasoning AI", "status": "CATALOGED"},
    {"id": "multimodal_ai", "name": "Multimodal AI", "status": "CATALOGED"},
    {"id": "agentic_ai", "name": "Agentic AI", "status": "CATALOGED"},
    {"id": "multi_agent_ai", "name": "Multi-Agent AI", "status": "ROADMAP"},
    {"id": "autonomous_ai", "name": "Autonomous AI", "status": "ROADMAP"},
    {"id": "advanced_research_ai", "name": "Advanced Research AI", "status": "RESEARCH"},
    {
        "id": "supreme_intelligence",
        "name": "Supreme Intelligence",
        "status": "LONG_TERM_RESEARCH_ONLY",
    },
)

AI_SCOPE_DOMAINS: tuple[dict[str, Any], ...] = (
    {
        "id": "bharat_india_ai",
        "name": "Bharat / India AI",
        "description": "Indian languages, local contexts, public services, businesses and research.",
        "status": "SCOPE_DEFINED",
        "examples": ["indic_languages", "bharat_datasets", "localization", "digital_public_services"],
    },
    {
        "id": "global_world_ai",
        "name": "Global / World AI",
        "description": "Cross-border AI capabilities, providers, standards and localization.",
        "status": "SCOPE_DEFINED",
        "examples": ["multilingual_ai", "global_provider_interoperability", "regional_compliance"],
    },
    {
        "id": "digital_infrastructure_ai",
        "name": "Digital Infrastructure AI",
        "description": "AI capabilities for servers, operating systems, networks, software and platforms.",
        "status": "SCOPE_DEFINED",
        "examples": ["server_operations", "system_observability", "software_assistance", "cybersecurity"],
        "implementation_boundary": "Infrastructure and runtime implementations remain in their canonical layers.",
    },
    {
        "id": "web_website_app_ai",
        "name": "Web, Website and App AI",
        "description": "AI-assisted creation, testing, accessibility, personalization and support.",
        "status": "SCOPE_DEFINED",
        "examples": ["website_building", "app_assistance", "web_search", "quality_testing"],
        "implementation_boundary": "Website, application and web execution remain in their own ecosystems.",
    },
    {
        "id": "business_economy_ai",
        "name": "Business, Commerce and Economy AI",
        "description": "Business operations, entrepreneurship, finance support and marketplace intelligence.",
        "status": "SCOPE_DEFINED",
        "examples": ["business_advisory", "sales_support", "market_research", "workflow_automation"],
    },
    {
        "id": "education_research_knowledge_ai",
        "name": "Education, Research and Knowledge AI",
        "description": "Learning, evidence-grounded research, knowledge discovery and scientific support.",
        "status": "SCOPE_DEFINED",
        "examples": ["tutoring", "research_assistance", "knowledge_retrieval", "translation"],
    },
    {
        "id": "media_creative_ai",
        "name": "Media and Creative AI",
        "description": "Text, image, audio, video, design, animation and 3D workflows.",
        "status": "SCOPE_DEFINED",
        "examples": ["content_generation", "image_tools", "speech_tools", "video_tools", "3d_assets"],
    },
    {
        "id": "health_wellness_relationship_ai",
        "name": "Health, Wellness and Relationship AI",
        "description": "Wellness information, relationship education and sexual-health education with appropriate safeguards.",
        "status": "SCOPE_DEFINED",
        "examples": ["wellness_education", "relationship_education", "sexual_health_information"],
        "safeguards": ["privacy", "age_appropriate_access", "professional_scope_limits", "consent"],
    },
    {
        "id": "lawful_adult_content_ai",
        "name": "Lawful Adult-Content Platform AI",
        "description": "Governance and moderation support for lawful, age-restricted adult platforms.",
        "status": "POLICY_GATED_SCOPE",
        "examples": ["age_assurance", "consent_and_rights_checks", "content_moderation", "privacy_controls"],
        "safeguards": [
            "adults_only",
            "informed_consent",
            "verified_content_rights",
            "no_minors_or_minor_appearing_content",
            "no_nonconsensual_intimate_imagery",
            "applicable_law_and_platform_policy",
        ],
    },
    {
        "id": "ai_infrastructure_platforms",
        "name": "AI Servers, Models, Runtime and Platform Infrastructure",
        "description": "Model lifecycle, inference, evaluation, deployment and integration capabilities.",
        "status": "SCOPE_DEFINED",
        "examples": ["model_registry", "inference_routing", "evaluation", "deployment_observability"],
        "implementation_boundary": "AI orchestration remains in ENGINE; persistence, files and cloud operations remain in their respective layers.",
    },
)


def get_scope_catalog() -> dict[str, list[dict[str, Any]]]:
    """Return a defensive, JSON-serializable copy of the scope taxonomy."""
    return {
        "maturity_levels": [dict(item) for item in AI_MATURITY_LEVELS],
        "domains": [
            {
                **item,
                "examples": list(item.get("examples", [])),
                "safeguards": list(item.get("safeguards", [])),
            }
            for item in AI_SCOPE_DOMAINS
        ],
    }
