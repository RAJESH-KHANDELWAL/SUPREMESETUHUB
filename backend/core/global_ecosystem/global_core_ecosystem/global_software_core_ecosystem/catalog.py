"""Software provider registry; metadata only, with no implicit connectivity."""

from __future__ import annotations

from .contracts import Provider

ROOT = "backend/core/global_ecosystem/global_core_ecosystem/global_software_core_ecosystem"

_PROVIDERS = (
    Provider("adobe", "Adobe", f"{ROOT}/adobe_software_core_ecosystem",
             ("CREATIVE", "DOCUMENTS", "DIGITAL_EXPERIENCE"),
             capabilities=("CREATIVE_CLOUD", "DOCUMENT_WORKFLOWS", "DIGITAL_ASSETS")),
    Provider("apple", "Apple", f"{ROOT}/apple_software_core_ecosystem",
             ("OPERATING_SYSTEMS", "DEVELOPMENT", "PRODUCTIVITY"),
             capabilities=("PLATFORM_SERVICES", "APP_DISTRIBUTION", "DEVICE_ECOSYSTEM")),
    Provider("aws", "Amazon Web Services", f"{ROOT}/aws_software_core_ecosystem",
             ("CLOUD", "DEVELOPER_TOOLS", "DATA", "SECURITY"),
             capabilities=("CLOUD_CONTROL_PLANE", "DEVELOPER_SERVICES", "CLOUD_SECURITY")),
    Provider("github", "GitHub", f"{ROOT}/github_software_core_ecosystem",
             ("SOURCE_CONTROL", "CI_CD", "DEVELOPER_COLLABORATION"),
             capabilities=("REPOSITORIES", "PULL_REQUESTS", "ACTIONS", "ISSUES")),
    Provider("atlassian", "Atlassian", f"{ROOT}/global_atlassian_core_ecosystem",
             ("WORK_MANAGEMENT", "SERVICE_MANAGEMENT", "DEVELOPER_COLLABORATION"),
             capabilities=("PROJECTS", "ISSUES", "KNOWLEDGE_BASE", "SERVICE_DESK")),
    Provider("microsoft", "Microsoft", f"{ROOT}/microsoft_software_core_ecosystem",
             ("PRODUCTIVITY", "CLOUD", "OPERATING_SYSTEMS", "DEVELOPER_TOOLS"),
             capabilities=("PRODUCTIVITY_SUITE", "CLOUD_SERVICES", "IDENTITY", "DEVELOPER_PLATFORM")),
)

_INDEX = {item.provider_id: item for item in _PROVIDERS}


def list_providers(*, include_disabled: bool = False) -> list[dict]:
    """Return provider records in stable identifier order."""
    items = sorted(_PROVIDERS, key=lambda item: item.provider_id)
    return [item.to_dict() for item in items if include_disabled or item.status != "DISABLED"]


def get_provider(provider_id: str) -> dict | None:
    """Return one provider record, or None when it is not registered."""
    item = _INDEX.get(provider_id.strip().lower())
    return item.to_dict() if item else None
