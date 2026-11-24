"""Structural and behavior tests for the GitHub Core provider manager."""
from __future__ import annotations

import importlib

from backend.core.global_ecosystem.global_core_ecosystem.github_core_ecosystem import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.github_core_ecosystem.catalog import (
    get_github_core_catalog,
    list_github_families,
)
from backend.core.global_ecosystem.global_core_ecosystem.github_core_ecosystem.contracts import (
    TenantContext,
)
from backend.core.global_ecosystem.global_core_ecosystem.github_core_ecosystem.policy import (
    GitHubCorePolicy,
)


EXPECTED_FAMILIES = {
    "actions", "apps", "authentication", "checks", "graphql", "issues",
    "organizations", "pull_requests", "repositories", "rest", "security",
    "webhooks",
}


def test_provider_catalog_registers_exactly_twelve_families():
    catalog = get_github_core_catalog()
    assert catalog["ecosystem_id"] == "GITHUB-CORE-ECOSYSTEM"
    assert {item["family"] for item in catalog["children"]} == EXPECTED_FAMILIES
    assert len(list_github_families()) == 12


def test_google_core_style_manager_public_contract():
    manager = get_manager()
    assert manager.status()["ecosystem_id"] == "GITHUB-CORE-ECOSYSTEM"
    assert manager.health()["family_count"] == 12
    assert manager.list_families()["count"] == 12
    assert manager.get_family("repositories")["family"] == "repositories"
    assert manager.get_offering("actions")["family"] == "actions"
    assert manager.dependency_map()["success"] is True


def test_every_family_package_is_importable():
    root = (
        "backend.core.global_ecosystem.global_core_ecosystem."
        "github_core_ecosystem."
    )
    for family in EXPECTED_FAMILIES:
        package = importlib.import_module(f"{root}github_{family}_core_ecosystem")
        assert package is not None


def test_tenant_context_and_sensitive_capability_classification():
    context = TenantContext(tenant_id="tenant-1", actor_id="actor-1")
    context.validate()
    assert GitHubCorePolicy.classify_capability("REPOSITORY_READ") == (
        "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
    )
    assert "SENSITIVE" in GitHubCorePolicy.classify_capability("REPOSITORY_WRITE")


def test_core_health_never_claims_live_provider_connection():
    health = get_manager().health()
    assert health["live_connections_verified_by_core"] == 0
    assert health["api_calls_performed_by_core"] == 0
