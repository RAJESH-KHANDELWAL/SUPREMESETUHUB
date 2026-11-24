"""Public manager for Global Human Language CORE Ecosystem."""
from __future__ import annotations

from typing import Any

from .catalog import get_catalog
from .master_catalog import (
    get_adjacent_master_entries,
    get_language_master_entries,
    master_catalog_mapping_summary,
)
from .orchestrator import GlobalHumanLanguageCoreOrchestrator
from .service import GlobalHumanLanguageCoreService

_MANAGER = GlobalHumanLanguageCoreService()


def get_manager() -> GlobalHumanLanguageCoreService:
    return _MANAGER


def describe() -> dict[str, Any]:
    return _MANAGER.describe()


def status() -> dict[str, Any]:
    return _MANAGER.status()


def health() -> dict[str, Any]:
    return _MANAGER.health()


def catalog() -> dict[str, Any]:
    data = get_catalog()
    data["master_catalog_mapping"] = master_catalog_mapping_summary()
    data["master_language_entries"] = get_language_master_entries()
    data["master_adjacent_context_entries"] = get_adjacent_master_entries()
    return data


def list_domains() -> list[dict[str, Any]]:
    return _MANAGER.list_domains()


def list_providers() -> list[dict[str, Any]]:
    return _MANAGER.list_providers()


def get_provider(provider_id: str) -> dict[str, Any] | None:
    return _MANAGER.get_provider(provider_id)


def list_master_language_entries() -> list[dict[str, Any]]:
    return get_language_master_entries()


def list_master_adjacent_entries() -> list[dict[str, Any]]:
    return get_adjacent_master_entries()


def dependency_map() -> dict[str, Any]:
    return GlobalHumanLanguageCoreOrchestrator().dependency_map()


__all__ = [
    "get_manager", "describe", "status", "health", "catalog", "list_domains",
    "list_providers", "get_provider", "list_master_language_entries",
    "list_master_adjacent_entries", "dependency_map",
]
