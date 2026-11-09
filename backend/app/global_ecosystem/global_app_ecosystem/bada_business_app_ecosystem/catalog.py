"""Bada Business APP composition catalog; contains no provider resource data."""
from __future__ import annotations
from typing import Any

APP_ECOSYSTEM_PROFILE = {
    "ecosystem_id": "BADA_BUSINESS_APP_ECOSYSTEM",
    "name": "BADA BUSINESS APP ECOSYSTEM",
    "layer": "APP",
    "parent": "GLOBAL APP ECOSYSTEM",
    "status": "APP_COMPOSITION_FOUNDATION_READY",
    "runtime_status": "NOT_MOUNTED",
    "api_package": "backend.api.global_ecosystem.global_api_ecosystem.bada_business_api_ecosystem",
    "ai_package": "backend.ai.global_ecosystem.global_ai_ecosystem.bada_business_ai_ecosystem",
    "description": "Application composition, module registration, lifecycle and diagnostics for Bada Business.",
}

APP_MODULES = (
    {"id": "resource_hub", "name": "Resource Hub", "purpose": "Present canonical Bada Business resources through the API layer.", "api_capability": "resource_catalog", "ai_capability": "resource_understanding"},
    {"id": "programs_learning", "name": "Programs & Learning", "purpose": "Organize program discovery and learning experiences.", "api_capability": "program_catalog", "ai_capability": "business_learning"},
    {"id": "digital_dukan", "name": "Digital Dukan", "purpose": "Application surface for digital-store resources and workflows.", "api_capability": "provider_resources", "ai_capability": "resource_recommendation"},
    {"id": "coach_workspace", "name": "Coach Workspace", "purpose": "Provide a workspace entry point for coaching and business guidance.", "api_capability": "provider_resources", "ai_capability": "business_research"},
    {"id": "growth_insights", "name": "Growth Insights", "purpose": "Display insights based on explicitly supplied business metrics.", "api_capability": "provider_resources", "ai_capability": "performance_insights"},
    {"id": "lead_referral_workspace", "name": "Lead & Referral Workspace", "purpose": "Organize consent-based lead and referral interactions.", "api_capability": "provider_resources", "ai_capability": "lead_qualification_support"},
)

def get_app_catalog() -> dict[str, Any]:
    return {
        "ecosystem": dict(APP_ECOSYSTEM_PROFILE),
        "modules": [dict(item) for item in APP_MODULES],
        "module_count": len(APP_MODULES),
        "execution_enabled": False,
    }
