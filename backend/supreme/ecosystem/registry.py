"""Read-only catalog of existing SUPREME capabilities.

This registry documents current module ownership. It deliberately does not import
routers or initialize services, so it cannot introduce circular imports or alter
runtime startup behavior.
"""

from __future__ import annotations

from typing import Any


_SUPREME_ECOSYSTEM_REGISTRY: dict[str, dict[str, Any]] = {
    "SUPREME-API-ECOSYSTEM": {
        "purpose": "API routing, authentication boundaries, status and frontend delivery",
        "runtime_entry": "backend/api/app.py",
        "modules": [
            "backend/api/auth.py",
            "backend/api/supreme.py",
            "backend/api/supreme_ecosystem.py",
            "backend/api/dashboard.py",
            "backend/api/identity.py",
            "backend/api/global_business_ecosystem.py",
            "backend/api/global_ai_ecosystem.py",
        ],
    },
    "SUPREME-BUSINESS-ECOSYSTEM": {
        "purpose": "Business records, projects, opportunities, matching, roles, work/income and marketplace workflows",
        "modules": [
            "backend/api/businesses.py",
            "backend/api/projects.py",
            "backend/api/opportunities.py",
            "backend/api/matching.py",
            "backend/api/roles.py",
            "backend/api/profiles.py",
            "backend/api/organizations.py",
            "backend/api/supreme_work_income.py",
            "backend/api/linksetu.py",
            "backend/api/digital_marketplace.py",
            "backend/api/print_on_demand.py",
            "backend/api/user_hub.py",
        ],
    },
    "SUPREME-CLOUD-ECOSYSTEM": {
        "purpose": "Infrastructure, cloud, storage, database, DNS and external service connectors",
        "modules": [
            "backend/api/cloud.py",
            "backend/api/infrastructure.py",
            "backend/api/storage.py",
            "backend/api/storage_routes.py",
            "backend/api/database.py",
            "backend/api/dns.py",
            "backend/api/connectors.py",
            "backend/api/email.py",
            "backend/api/connectivity.py",
            "backend/api/app.py",
        ],
        "domain_roots": [
            "backend/CLOUD/",
            "backend/DATABASE/",
            "backend/STORAGE/",
            "backend/SERVER/",
            "backend/SSH/",
        ],
    },
    "SUPREME-AI-ECOSYSTEM": {
        "purpose": "AI, language services, personal AI, WhatsApp AI and global AI workflows",
        "modules": [
            "backend/api/ai.py",
            "backend/api/language_services.py",
            "backend/api/supreme_personal_ai.py",
            "backend/api/supreme_whatsapp_ai.py",
            "backend/api/global_ai_ecosystem.py",
            "backend/supreme/personal_ai/",
        ],
    },
    "GLOBAL-BUSINESS-ECOSYSTEM": {
        "purpose": "Separate global business ecosystem entry and its business-facing capabilities",
        "runtime_entry": "backend/api/global_business_ecosystem.py",
        "architecture_path": "backend/supreme/ecosystem/global-business-ecosystem/GLOBAL-BUSINESS-ECOSYSTEM/",
        "separate_system": True,
    },
}


def get_supreme_ecosystem_registry() -> dict[str, dict[str, Any]]:
    """Return a defensive copy of the documented capability catalog."""
    return {
        name: {key: list(value) if isinstance(value, list) else value for key, value in details.items()}
        for name, details in _SUPREME_ECOSYSTEM_REGISTRY.items()
    }
