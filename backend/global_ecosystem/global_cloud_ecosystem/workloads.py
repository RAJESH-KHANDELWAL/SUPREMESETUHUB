"""Bharat-to-global cloud workload coverage, including lawful adult-industry infrastructure.

This is a workload taxonomy, not a content repository or proof of provider integration.
Adult-industry workloads are limited to lawful, adults-only, consensual and rights-cleared services.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

_TIERS = ("normal", "standard", "advanced", "supreme")
_REGIONS = ("bharat_india", "asia_pacific", "europe", "middle_east_africa", "americas", "global_world")

_ROWS = (
    ("agriculture_food", "Agriculture, food and rural infrastructure", "normal", "bharat_india,global_world", "farm_records,precision_agriculture,food_supply_chain,cold_chain"),
    ("education_research", "Education, learning and research", "normal", "bharat_india,global_world", "learning_platforms,digital_classrooms,research_compute,libraries"),
    ("healthcare_wellness", "Healthcare, wellness and fitness", "standard", "bharat_india,global_world", "health_records,telehealth,clinical_workflows,fitness_platforms"),
    ("government_civic", "Government, civic and public services", "standard", "bharat_india,global_world", "citizen_services,digital_identity,public_records,disaster_response"),
    ("banking_finance", "Banking, finance, insurance and payments", "advanced", "bharat_india,global_world", "banking_core,payments,risk_analytics,fraud_detection"),
    ("business_enterprise", "Business, enterprise and SaaS", "normal", "bharat_india,global_world", "erp,crm,hrms,accounting,enterprise_saas"),
    ("commerce_retail", "Commerce, marketplace and retail", "normal", "bharat_india,global_world", "ecommerce,marketplaces,inventory,order_management"),
    ("media_entertainment", "Media, entertainment and streaming", "standard", "bharat_india,global_world", "video_streaming,audio_streaming,live_events,content_delivery"),
    ("social_community", "Social networking, communities and creator platforms", "standard", "bharat_india,global_world", "social_networks,messaging,creator_tools,community_platforms"),
    ("adult_creator_platforms", "Adult creator and subscription platforms", "advanced", "bharat_india,global_world", "adult_creator_subscriptions,creator_payouts,age_gating,consent_records,rights_management"),
    ("adult_entertainment_streaming", "Lawful adult entertainment and pornographic streaming services", "advanced", "bharat_india,global_world", "age_verified_adult_streaming,rights_cleared_media_storage,access_controls,moderation,privacy_protection"),
    ("adult_dating_relationships", "Adult dating and relationship platforms", "standard", "bharat_india,global_world", "adult_dating,identity_assurance,consent_controls,abuse_reporting,privacy"),
    ("sexual_wellness_education", "Sexual wellness and adult education", "standard", "bharat_india,global_world", "sexual_health_education,wellness_content,private_consultation,age_appropriate_access"),
    ("adult_content_safety", "Adult-content safety, rights and compliance", "supreme", "bharat_india,global_world", "age_assurance,consent_verification,content_rights,nonconsensual_content_prevention,reporting_and_takedown"),
    ("cybersecurity_privacy", "Cybersecurity, privacy and digital identity", "advanced", "bharat_india,global_world", "zero_trust,identity_access,key_management,threat_detection,privacy_engineering"),
    ("developer_platforms", "Developer tools, software engineering and CI/CD", "standard", "bharat_india,global_world", "source_control,build_pipelines,artifact_registry,developer_environments"),
    ("ai_machine_learning", "Artificial intelligence, machine learning and data science", "advanced", "bharat_india,global_world", "model_training,inference,gpu_compute,vector_search,mlops"),
    ("data_database_analytics", "Databases, data platforms and analytics", "standard", "bharat_india,global_world", "relational_databases,document_databases,data_warehouses,stream_processing"),
    ("storage_backup_migration", "Cloud storage, backup, sync and migration", "normal", "bharat_india,global_world", "object_storage,file_storage,backup,disaster_recovery,cloud_migration"),
    ("web_mobile_desktop", "Web, mobile, desktop and app delivery", "normal", "bharat_india,global_world", "web_hosting,mobile_backends,desktop_updates,pwa,app_distribution"),
    ("telecom_network_edge", "Telecommunications, networking and edge", "advanced", "bharat_india,global_world", "5g_core,sd_wan,cdn,dns,edge_compute"),
    ("manufacturing_industry", "Manufacturing, logistics and industrial systems", "advanced", "bharat_india,global_world", "industrial_iot,digital_twins,robotics,warehouse_automation"),
    ("energy_environment", "Energy, climate and environmental systems", "advanced", "bharat_india,global_world", "smart_grids,renewables,carbon_accounting,environmental_monitoring"),
    ("travel_transport", "Travel, transport and mobility", "standard", "bharat_india,global_world", "booking_platforms,route_optimization,telematics,mobility_services"),
    ("real_estate_construction", "Real estate, construction and smart buildings", "standard", "bharat_india,global_world", "property_platforms,bim,building_management,facility_operations"),
    ("gaming_esports", "Gaming, esports and virtual worlds", "advanced", "bharat_india,global_world", "game_backend,matchmaking,anti_cheat,virtual_worlds"),
    ("science_space_defence", "Scientific, space and regulated critical infrastructure", "supreme", "bharat_india,global_world", "hpc,simulation,satellite_data,restricted_workload_isolation"),
    ("multi_cloud_sovereign", "Multi-cloud, hybrid-cloud and sovereign infrastructure", "supreme", "bharat_india,asia_pacific,europe,middle_east_africa,americas,global_world", "multi_cloud_control_plane,sovereign_workload_placement,policy_orchestration,cross_cloud_observability"),
)

_ADULT_GUARDRAILS = (
    "adults_only_age_assurance",
    "documented_informed_consent",
    "content_and_distribution_rights_cleared",
    "block_minors_and_nonconsensual_intimate_content",
    "anti_exploitation_and_takedown_workflows",
    "privacy_security_and_legal_compliance",
)

_WORKLOADS: tuple[dict[str, Any], ...] = tuple(
    {
        "id": row[0],
        "name": row[1],
        "tier": row[2],
        "regions": tuple(row[3].split(",")),
        "workloads": tuple(row[4].split(",")),
        "adult_industry": row[0].startswith("adult_") or row[0] == "sexual_wellness_education",
        "guardrails": _ADULT_GUARDRAILS if row[0].startswith("adult_") else (
            ("age_appropriate_access", "privacy_and_legal_compliance")
            if row[0] == "sexual_wellness_education" else ()
        ),
        "integration_status": "workload_taxonomy_only",
        "live_provider_connection_verified": False,
    }
    for row in _ROWS
)


def list_cloud_workloads(*, tier: str | None = None, region: str | None = None,
                         adult_industry: bool | None = None) -> tuple[dict[str, Any], ...]:
    """Return defensive copies of workload entries, optionally filtered."""
    rows = _WORKLOADS
    if tier is not None:
        key = str(tier).strip().lower()
        if key not in _TIERS:
            return ()
        rows = tuple(item for item in rows if item["tier"] == key)
    if region is not None:
        key = str(region).strip().lower()
        rows = tuple(item for item in rows if key in item["regions"])
    if adult_industry is not None:
        rows = tuple(item for item in rows if item["adult_industry"] is adult_industry)
    return tuple(deepcopy(item) for item in rows)


def get_cloud_workload(workload_id: str) -> dict[str, Any] | None:
    """Get one workload by stable identifier."""
    key = str(workload_id or "").strip().lower()
    for item in _WORKLOADS:
        if item["id"] == key:
            return deepcopy(item)
    return None


def validate_cloud_workloads() -> tuple[str, ...]:
    """Validate identifiers, tier/region values and adult-industry safeguards."""
    errors: list[str] = []
    ids = [item["id"] for item in _WORKLOADS]
    if len(ids) != len(set(ids)):
        errors.append("duplicate workload ids")
    for item in _WORKLOADS:
        if item["tier"] not in _TIERS:
            errors.append(f"{item['id']} has invalid tier")
        if not item["regions"] or any(region not in _REGIONS for region in item["regions"]):
            errors.append(f"{item['id']} has invalid region")
        if item["adult_industry"] and not set(_ADULT_GUARDRAILS).issubset(item["guardrails"]):
            errors.append(f"{item['id']} is missing adult-industry safeguards")
        if item["live_provider_connection_verified"] is not False:
            errors.append(f"{item['id']} incorrectly claims live provider verification")
    return tuple(errors)


__all__ = ["list_cloud_workloads", "get_cloud_workload", "validate_cloud_workloads"]
