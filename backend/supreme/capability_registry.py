"""Shared capability catalog for SUPREME and SUPREME ECOSYSTEM.

This catalog points to existing mounted API routers. It does not duplicate their
business logic or claim that third-party integrations are connected.
"""

from __future__ import annotations

from copy import deepcopy


_CAPABILITIES = [
    {
        "id": "identity-and-accounts",
        "name": "IDENTITY & ACCOUNTS",
        "routes": ["/auth", "/users", "/organizations", "/identity", "/profiles"],
        "functions": ["authentication", "user accounts", "organization records", "identity registry", "profiles"],
    },
    {
        "id": "business-and-work",
        "name": "BUSINESS, PROJECTS & WORK",
        "routes": ["/businesses", "/projects", "/opportunities", "/matching", "/roles"],
        "functions": ["business records", "project management", "work and income opportunities", "matching", "role management"],
    },
    {
        "id": "supreme-control",
        "name": "SUPREME CONTROL",
        "routes": ["/supreme", "/supreme/personal-ai", "/supreme/work-income", "/supreme/whatsapp-ai"],
        "functions": ["owner dashboard", "owner profile and identity search", "personal AI services", "work and income services", "WhatsApp AI endpoints"],
    },
    {
        "id": "supreme-ecosystem",
        "name": "SUPREME ECOSYSTEM",
        "routes": ["/api/v1/supreme-ecosystem", "/api/v1/supreme-ecosystem/business/status", "/api/v1/supreme-ecosystem/ai/status", "/api/v1/supreme-ecosystem/integrations"],
        "functions": ["ecosystem status", "business ecosystem status", "AI ecosystem status", "account and dashboard", "integration readiness"],
    },
    {
        "id": "ai-services",
        "name": "AI SERVICES",
        "routes": ["/ai", "/api/v1/global-ai-ecosystem"],
        "functions": ["AI API", "global AI ecosystem"],
    },
    {
        "id": "global-business",
        "name": "GLOBAL BUSINESS ECOSYSTEM",
        "routes": ["/api/v1/global-business-ecosystem", "/api/v1/frontend/global-business-ecosystem"],
        "functions": ["global business APIs", "public business ecosystem frontend"],
    },
    {
        "id": "infrastructure-and-storage",
        "name": "INFRASTRUCTURE & STORAGE",
        "routes": ["/infrastructure", "/dns", "/storage", "/api/v1/storage"],
        "functions": ["domains and hosting inventory", "servers and network", "DNS", "storage APIs"],
    },
    {
        "id": "connectors-and-commerce",
        "name": "CONNECTORS & DIGITAL COMMERCE",
        "routes": ["/connectors", "/linksetu", "/email", "/api/v1/print-on-demand", "/api/v1/digital-marketplace", "/api/v1/products"],
        "functions": ["provider connector registry", "LinkSetu", "email services", "print-on-demand", "digital marketplace", "product catalog"],
    },
    {
        "id": "creative-and-content",
        "name": "CREATIVE & CONTENT SYSTEMS",
        "routes": ["/api/v1/gallary-woult", "/api/v1/mukti-mahal", "/api/v1/theme-hub"],
        "functions": ["Gallary Woult", "Mukti Mahal", "theme hub"],
    },
    {
        "id": "readiness-and-operations",
        "name": "READINESS & OPERATIONS",
        "routes": ["/api/v1/core-readiness", "/api/v1/product-ecosystem", "/api/v1/language-services", "/dashboard", "/health"],
        "functions": ["core readiness", "product ecosystem", "language services", "dashboard summaries", "application health"],
    },
]


def get_capability_catalog() -> dict:
    """Return a copy so API callers cannot mutate the shared catalog."""
    modules = deepcopy(_CAPABILITIES)
    return {
        "success": True,
        "catalog_version": "1.0.0",
        "source": "existing backend API routers registered by backend/api/app.py",
        "modules_count": len(modules),
        "modules": modules,
        "integration_policy": (
            "Routes are catalogued, not live-probed. Provider credentials or a listed "
            "route do not by themselves prove an external integration is connected."
        ),
    }
