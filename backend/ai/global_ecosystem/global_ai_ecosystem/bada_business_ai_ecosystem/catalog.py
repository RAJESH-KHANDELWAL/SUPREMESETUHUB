"""Bada Business AI-domain capability catalog."""
from __future__ import annotations
from typing import Any

AI_ECOSYSTEM_PROFILE = {
    "ecosystem_id": "BADA_BUSINESS_AI_ECOSYSTEM",
    "name": "BADA BUSINESS AI ECOSYSTEM",
    "layer": "AI",
    "parent": "GLOBAL AI ECOSYSTEM",
    "provider_resource_owner": "backend.global_ecosystem.global_bada_business_ecosystem",
    "status": "AI_DOMAIN_FOUNDATION_READY",
    "runtime_status": "NOT_CONFIGURED",
    "description": (
        "AI-domain intelligence for Bada Business resources, programs, "
        "products, events, referrals and business learning content."
    ),
}

AI_CAPABILITIES = (
    {
        "id": "resource_understanding",
        "name": "Resource Understanding",
        "description": "Classify and explain canonical provider resources.",
        "input_domains": ["courses", "events", "links", "products", "programs"],
    },
    {
        "id": "program_comparison",
        "name": "Program Comparison",
        "description": "Compare program metadata, stated outcomes and known limitations.",
        "input_domains": ["programs", "courses", "products"],
    },
    {
        "id": "business_learning",
        "name": "Business Learning Assistant",
        "description": "Explain business learning concepts and connect them to catalog resources.",
        "input_domains": ["courses", "programs", "business_content"],
    },
    {
        "id": "business_research",
        "name": "Business Research",
        "description": "Prepare structured research briefs using supplied and verified evidence.",
        "input_domains": ["events", "programs", "business_content"],
    },
    {
        "id": "resource_recommendation",
        "name": "Resource Recommendation",
        "description": "Match stated user goals to relevant catalog resources without inventing benefits.",
        "input_domains": ["courses", "events", "products", "programs"],
    },
    {
        "id": "lead_qualification_support",
        "name": "Lead Qualification Support",
        "description": "Structure consent-based lead context and qualification questions.",
        "input_domains": ["registration", "referrals", "programs"],
    },
    {
        "id": "business_content_analysis",
        "name": "Business Content Analysis",
        "description": "Summarize and classify business articles, stories and learning material.",
        "input_domains": ["business_content", "events"],
    },
    {
        "id": "performance_insights",
        "name": "Performance Insights",
        "description": "Analyze supplied campaign or business metrics; no metrics are assumed.",
        "input_domains": ["referrals", "products", "programs"],
    },
)


def get_ai_catalog() -> dict[str, Any]:
    """Return AI-domain metadata; provider resources remain in their owner package."""
    return {
        "ecosystem": dict(AI_ECOSYSTEM_PROFILE),
        "capabilities": [dict(item) for item in AI_CAPABILITIES],
        "capability_count": len(AI_CAPABILITIES),
        "resource_source": "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog",
        "runtime_configured": False,
    }
