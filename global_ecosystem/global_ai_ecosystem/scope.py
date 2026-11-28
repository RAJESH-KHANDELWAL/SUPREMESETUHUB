"""Bharat-to-global AI scope taxonomy and capability maturity.

This module is a catalog/roadmap only. It does not execute models, call
providers, expose HTTP routes, or own CORE, ENGINE, API, or DATABASE logic.
A catalog entry is not evidence that a capability is implemented or live.
"""
from __future__ import annotations

from typing import Any


AI_MATURITY_LEVELS: tuple[dict[str, str], ...] = (
    {"id": "foundational_ai", "name": "Foundational / Basic AI", "status": "SCOPE_DEFINED"},
    {"id": "task_specific_ai", "name": "Task-Specific / Narrow AI", "status": "SCOPE_DEFINED"},
    {"id": "assistant_conversational_ai", "name": "Assistant and Conversational AI", "status": "SCOPE_DEFINED"},
    {"id": "predictive_analytical_ai", "name": "Predictive and Analytical AI", "status": "SCOPE_DEFINED"},
    {"id": "generative_ai", "name": "Generative AI", "status": "CATALOGED"},
    {"id": "multimodal_multilingual_ai", "name": "Multimodal and Multilingual AI", "status": "CATALOGED"},
    {"id": "reasoning_planning_ai", "name": "Reasoning and Planning AI", "status": "CATALOGED"},
    {"id": "tool_using_agentic_ai", "name": "Tool-Using and Agentic AI", "status": "CATALOGED"},
    {"id": "multi_agent_ai", "name": "Multi-Agent AI", "status": "ROADMAP"},
    {"id": "bounded_autonomous_ai", "name": "Bounded Autonomous AI", "status": "ROADMAP"},
    {"id": "frontier_research_ai", "name": "Frontier and Advanced Research AI", "status": "RESEARCH"},
    {"id": "agi_research", "name": "AGI Research", "status": "LONG_TERM_RESEARCH_ONLY"},
    {"id": "superintelligence_research", "name": "Superintelligence / Supreme AI Research", "status": "LONG_TERM_RESEARCH_ONLY"},
)

# Each entry describes a domain to be catalogued. Provider execution and
# domain-specific runtime behavior belong to their canonical architecture layers.
AI_SCOPE_DOMAINS: tuple[dict[str, Any], ...] = (
    {
        "id": "bharat_india_ai", "name": "Bharat / India AI",
        "description": "India-first AI for Indic languages, local needs, public services, research and businesses.",
        "status": "SCOPE_DEFINED",
        "examples": ["indic_languages", "bharat_datasets", "indian_localization", "digital_public_services", "rural_innovation"],
    },
    {
        "id": "global_world_regional_ai", "name": "Global, World and Regional AI",
        "description": "International AI providers, country and regional ecosystems, languages, standards and interoperability.",
        "status": "SCOPE_DEFINED",
        "examples": ["global_providers", "regional_ai", "cross_border_interoperability", "multilingual_localization", "international_standards"],
    },
    {
        "id": "everyday_personal_life_ai", "name": "Everyday, Personal and Lifestyle AI",
        "description": "General-purpose everyday assistance, planning, accessibility and personal productivity.",
        "status": "SCOPE_DEFINED",
        "examples": ["daily_assistance", "personal_productivity", "planning", "accessibility", "knowledge_help"],
    },
    {
        "id": "business_commerce_economy_ai", "name": "Business, Commerce, Industry and Economy AI",
        "description": "Entrepreneurship, MSMEs, enterprise operations, commerce, marketing, finance support and economic research.",
        "status": "SCOPE_DEFINED",
        "examples": ["entrepreneurship", "msme_support", "enterprise_workflows", "sales_and_marketing", "market_intelligence", "commerce"],
    },
    {
        "id": "finance_banking_insurance_ai", "name": "Finance, Banking, Payments and Insurance AI",
        "description": "Financial information, fraud prevention, risk analysis and regulated financial workflows.",
        "status": "SCOPE_DEFINED",
        "examples": ["financial_education", "fraud_detection", "risk_analysis", "payment_operations", "insurance_support"],
        "safeguards": ["applicable_financial_regulation", "privacy", "human_review_for_consequential_decisions"],
    },
    {
        "id": "education_learning_research_ai", "name": "Education, Learning, Science and Research AI",
        "description": "Learning support, tutoring, research discovery, scientific workflows and knowledge systems.",
        "status": "SCOPE_DEFINED",
        "examples": ["tutoring", "school_and_higher_education", "scientific_research", "knowledge_retrieval", "translation"],
    },
    {
        "id": "healthcare_wellness_ai", "name": "Healthcare, Medical Information and Wellness AI",
        "description": "Health information and wellness support within professional and clinical boundaries.",
        "status": "POLICY_GATED_SCOPE",
        "examples": ["health_education", "wellness_information", "care_navigation", "medical_research_support"],
        "safeguards": ["privacy", "clinical_scope_limits", "qualified_professional_oversight", "applicable_law"],
    },
    {
        "id": "relationship_intimacy_sexual_health_ai", "name": "Relationship, Intimacy and Sexual-Health AI",
        "description": "Relationship education, consent education, intimacy information and sexual-health education.",
        "status": "POLICY_GATED_SCOPE",
        "examples": ["relationship_education", "communication_skills", "consent_education", "sexual_health_information", "adult_wellness"],
        "safeguards": ["adults_only_where_required", "consent", "privacy", "no_exploitation", "professional_scope_limits"],
    },
    {
        "id": "lawful_adult_industry_platform_ai", "name": "Lawful Adult Industry and Adult-Platform AI",
        "description": "Safety, compliance and platform-governance systems for lawful age-restricted adult services.",
        "status": "POLICY_GATED_SCOPE",
        "examples": ["age_assurance", "content_classification", "consent_and_rights_verification", "moderation", "privacy_and_safety_controls"],
        "safeguards": ["adults_only", "informed_consent", "verified_content_rights", "no_minors_or_minor_appearing_content", "no_nonconsensual_intimate_imagery", "no_sexual_exploitation_or_trafficking", "applicable_law_and_platform_policy"],
    },
    {
        "id": "agriculture_environment_climate_ai", "name": "Agriculture, Environment, Climate and Sustainability AI",
        "description": "Agriculture, food systems, biodiversity, climate and resource-management use cases.",
        "status": "SCOPE_DEFINED",
        "examples": ["precision_agriculture", "crop_information", "weather_risk_support", "climate_analysis", "sustainability"],
    },
    {
        "id": "government_public_services_civic_ai", "name": "Government, Public Services and Civic AI",
        "description": "Public-interest information, civic access, service delivery and administrative assistance.",
        "status": "POLICY_GATED_SCOPE",
        "examples": ["public_information", "service_navigation", "civic_accessibility", "administrative_assistance"],
        "safeguards": ["transparency", "privacy", "non_discrimination", "human_accountability", "applicable_law"],
    },
    {
        "id": "law_justice_compliance_ai", "name": "Law, Justice, Compliance and Governance AI",
        "description": "Legal information, document workflows, compliance research and governance support.",
        "status": "POLICY_GATED_SCOPE",
        "examples": ["legal_information", "document_analysis", "compliance_monitoring", "policy_research"],
        "safeguards": ["jurisdiction_awareness", "no_substitute_for_qualified_legal_counsel", "confidentiality", "human_review"],
    },
    {
        "id": "people_society_culture_language_ai", "name": "People, Society, Culture, Heritage and Language AI",
        "description": "Human-centered social applications, cultural preservation, language access and knowledge exchange.",
        "status": "SCOPE_DEFINED",
        "examples": ["bharat_heritage", "world_cultures", "language_preservation", "accessibility", "community_knowledge"],
    },
    {
        "id": "media_entertainment_creative_ai", "name": "Media, Entertainment and Creative AI",
        "description": "Text, image, audio, speech, music, video, animation, design and 3D workflows.",
        "status": "SCOPE_DEFINED",
        "examples": ["writing", "image_creation", "audio_and_speech", "video", "animation", "design", "3d_content"],
        "safeguards": ["copyright_and_licensing", "consent_and_likeness_rights", "content_provenance"],
    },
    {
        "id": "digital_infrastructure_cybersecurity_ai", "name": "Digital Infrastructure, Cybersecurity and Operations AI",
        "description": "AI-assisted software, systems, networks, cloud, hosting, servers, reliability and defensive security.",
        "status": "SCOPE_DEFINED",
        "examples": ["software_assistance", "server_observability", "cloud_operations", "network_operations", "defensive_security"],
        "implementation_boundary": "Infrastructure execution and security enforcement remain in their canonical layers.",
    },
    {
        "id": "web_website_app_platform_ai", "name": "Web, Website, App and Platform AI",
        "description": "AI-assisted creation, testing, accessibility, personalization, discovery and support.",
        "status": "SCOPE_DEFINED",
        "examples": ["web_development", "website_building", "app_assistance", "quality_testing", "accessibility", "platform_support"],
        "implementation_boundary": "Web, website and application runtime remain in their own ecosystems.",
    },
    {
        "id": "robotics_iot_edge_embodied_ai", "name": "Robotics, IoT, Edge and Embodied AI",
        "description": "AI for physical devices, sensors, robotics and edge environments with bounded safety controls.",
        "status": "RESEARCH",
        "examples": ["robotics", "iot", "edge_inference", "computer_vision", "industrial_automation"],
        "safeguards": ["physical_safety", "bounded_authority", "testing", "human_override"],
    },
    {
        "id": "transport_mobility_space_ai", "name": "Transport, Mobility, Aviation and Space AI",
        "description": "Research and decision-support for mobility, logistics, aviation and space systems.",
        "status": "RESEARCH",
        "examples": ["mobility_support", "logistics", "aviation_research", "satellite_data", "space_research"],
        "safeguards": ["safety_critical_validation", "qualified_oversight", "applicable_regulation"],
    },
    {
        "id": "ai_models_compute_infrastructure", "name": "AI Models, Compute, Servers and Runtime Infrastructure",
        "description": "Model lifecycle, compute resources, inference routing, evaluation, deployment and observability.",
        "status": "SCOPE_DEFINED",
        "examples": ["model_registry", "compute_management", "inference_routing", "model_evaluation", "deployment_observability"],
        "implementation_boundary": "AI orchestration belongs to ENGINE; persistence belongs to DATABASE; public interfaces belong to API.",
    },
    {
        "id": "ai_safety_security_governance", "name": "AI Safety, Security, Privacy and Governance",
        "description": "Risk management, privacy, model evaluation, security controls, auditability and responsible deployment.",
        "status": "SCOPE_DEFINED",
        "examples": ["safety_evaluation", "privacy_controls", "model_risk_management", "audit_trails", "policy_enforcement"],
        "implementation_boundary": "Identity, authentication, authorization and enforcement remain in canonical security layers.",
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


def get_domain(domain_id: str) -> dict[str, Any] | None:
    """Return one domain by stable ID, or None when it is not catalogued."""
    for item in AI_SCOPE_DOMAINS:
        if item["id"] == domain_id:
            return {
                **item,
                "examples": list(item.get("examples", [])),
                "safeguards": list(item.get("safeguards", [])),
            }
    return None


def list_domain_ids() -> tuple[str, ...]:
    """Return stable IDs for every catalogued AI domain."""
    return tuple(item["id"] for item in AI_SCOPE_DOMAINS)
