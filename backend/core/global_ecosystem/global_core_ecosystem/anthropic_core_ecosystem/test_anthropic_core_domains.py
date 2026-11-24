"""Behavior and structural checks for Anthropic Core domains and manager API."""
from __future__ import annotations

import importlib

from backend.core.global_ecosystem.global_core_ecosystem.anthropic_core_ecosystem.domain_catalog import (
    DOMAIN_DEFINITIONS, anthropic_domain_summary,
)
from backend.core.global_ecosystem.global_core_ecosystem.anthropic_core_ecosystem.domain_runtime import AnthropicCoreDomainManager
from backend.core.global_ecosystem.global_core_ecosystem.anthropic_core_ecosystem.manager import get_manager

DOMAIN_PACKAGES = {
    "MESSAGING_AND_CONVERSATION": "anthropic_messages_core_ecosystem",
    "BATCH_PROCESSING": "anthropic_batches_core_ecosystem",
    "MODEL_DISCOVERY_AND_METADATA": "anthropic_models_core_ecosystem",
    "TOKEN_ACCOUNTING": "anthropic_token_counting_core_ecosystem",
    "FILE_ASSETS": "anthropic_files_core_ecosystem",
    "WORKSPACE_GOVERNANCE": "anthropic_admin_workspaces_core_ecosystem",
    "MANAGED_AGENT_OPERATIONS": "anthropic_managed_agents_core_ecosystem",
    "TOOL_INTERACTION": "anthropic_tool_use_core_ecosystem",
    "AUTHENTICATION_AND_IDENTITY": "anthropic_auth_identity_core_ecosystem",
}


def test_domain_catalog_has_nine_registered_domains():
    assert len(DOMAIN_DEFINITIONS) == 9
    assert set(DOMAIN_PACKAGES) == set(DOMAIN_DEFINITIONS)


def test_each_domain_package_has_manager_entry_point():
    root = "backend.core.global_ecosystem.global_core_ecosystem.anthropic_core_ecosystem"
    for domain_id, package_name in DOMAIN_PACKAGES.items():
        package = importlib.import_module(f"{root}.{package_name}")
        manager = package.get_manager()
        assert manager.DOMAIN_ID == domain_id
        assert manager.status()["domain_id"] == domain_id
        assert manager.list_offerings()["success"] is True


def test_inventory_coverage_and_manager_parity():
    summary = anthropic_domain_summary()
    manager = get_manager()
    assert summary["domain_count"] == 9
    assert summary["offering_count"] == 9
    assert summary["assigned_offering_count"] == 9
    assert manager.list_domain_inventory()
    for domain in summary["domains"]:
        scoped = AnthropicCoreDomainManager(domain["domain_id"]).list_offerings()
        assert scoped["count"] == domain["offering_count"]


def test_manager_discovery_health_and_safe_catalog_status():
    m = get_manager()
    assert m.health()["product_family_count"] == 9
    assert m.list_products()["count"] == 9
    assert m.get_product("ANTHROPIC-MESSAGES-CORE-ECOSYSTEM")
    assert m.get_offering("messages")
    assert m.status()["live_connection_verified"] is False
    assert m.dependency_map()["success"] is True


def test_unknown_domain_is_rejected():
    try:
        AnthropicCoreDomainManager("UNKNOWN")
    except ValueError as exc:
        assert "UNKNOWN_ANTHROPIC_CORE_DOMAIN" in str(exc)
    else:
        raise AssertionError("Unknown domain must fail closed")
