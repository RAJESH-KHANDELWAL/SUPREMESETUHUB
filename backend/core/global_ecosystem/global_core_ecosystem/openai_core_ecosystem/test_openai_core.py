"""Structural, behavior and architecture-boundary tests for OpenAI Core."""
from __future__ import annotations

import importlib

from backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem.catalog import (
    get_openai_core_catalog,
    list_openai_core_modules,
    validate_openai_core_catalog,
)
from backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem.contracts import TenantContext
from backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem.domain_catalog import (
    DOMAIN_DEFINITIONS,
    openai_domain_summary,
    validate_openai_domain_catalog,
)
from backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem.policy import (
    OpenAICorePolicy,
)


PRODUCT_PACKAGES = {
    "chatgpt": "openai_chatgpt_core_ecosystem",
    "chatgpt_business": "openai_chatgpt_business_core_ecosystem",
    "chatgpt_enterprise": "openai_chatgpt_enterprise_core_ecosystem",
    "chatgpt_education": "openai_chatgpt_education_core_ecosystem",
    "chatgpt_health": "openai_chatgpt_health_core_ecosystem",
    "codex": "openai_codex_core_ecosystem",
    "dots": "openai_dots_core_ecosystem",
    "agents_api": "openai_agents_core_ecosystem",
    "agents_sdk": "openai_agents_sdk_core_ecosystem",
    "apps_sdk": "openai_apps_sdk_core_ecosystem",
    "chatkit": "openai_chatkit_core_ecosystem",
    "sdk_libraries": "openai_sdk_libraries_core_ecosystem",
    "plugins_mcp": "openai_plugins_mcp_core_ecosystem",
    "sora": "openai_sora_core_ecosystem",
}
DOMAIN_PACKAGES = {
    "CHATGPT_AND_WORKSPACE": "openai_chatgpt_and_workspace_core_ecosystem",
    "AGENT_RUNTIME_AND_ORCHESTRATION": "openai_agent_runtime_and_orchestration_core_ecosystem",
    "CODEX_AND_DEVELOPER_EXECUTION": "openai_codex_and_developer_execution_core_ecosystem",
    "APP_AND_EMBEDDED_EXPERIENCES": "openai_app_and_embedded_experiences_core_ecosystem",
    "EXTENSIBILITY_AND_TOOL_INTEGRATION": "openai_extensibility_and_tool_integration_core_ecosystem",
    "MODEL_API_AND_INFERENCE": "openai_model_api_and_inference_core_ecosystem",
    "MULTIMODAL_AND_REALTIME": "openai_multimodal_and_realtime_core_ecosystem",
    "FILES_AND_RETRIEVAL": "openai_files_and_retrieval_core_ecosystem",
    "SAFETY_EVALUATION_AND_MODERATION": "openai_safety_evaluation_and_moderation_core_ecosystem",
    "BUSINESS_EDUCATION_AND_ENTERPRISE": "openai_business_education_and_enterprise_core_ecosystem",
    "RETIRED_PRODUCT_REFERENCES": "openai_retired_product_references_core_ecosystem",
}


def test_catalog_contains_fourteen_unique_product_families():
    catalog = get_openai_core_catalog()
    products = list_openai_core_modules()
    assert catalog["ecosystem_id"] == "OPENAI-CORE-ECOSYSTEM"
    assert len(products) == 14
    assert len({item["id"] for item in products}) == 14
    assert validate_openai_core_catalog() == ()


def test_all_product_packages_export_a_shared_service():
    package_root = "backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem"
    for product_id, package_name in PRODUCT_PACKAGES.items():
        package = importlib.import_module(f"{package_root}.{package_name}")
        manager = package.get_manager()
        assert manager.status()["id"] == product_id
        assert manager.status()["live_connection_verified"] is False


def test_all_eleven_domain_packages_are_registered_and_working():
    assert len(DOMAIN_DEFINITIONS) == 11
    assert set(DOMAIN_PACKAGES) == set(DOMAIN_DEFINITIONS)
    package_root = "backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem"
    for domain_id, package_name in DOMAIN_PACKAGES.items():
        package = importlib.import_module(f"{package_root}.{package_name}")
        manager = package.get_manager()
        assert manager.DOMAIN_ID == domain_id
        assert manager.status()["domain_id"] == domain_id
        assert manager.list_offerings()["success"] is True


def test_domain_inventory_covers_all_products_without_unknown_ids():
    assert validate_openai_domain_catalog() == ()
    summary = openai_domain_summary()
    assert summary["domain_count"] == 11
    assert summary["product_count"] == 14


def test_tenant_policy_requires_authenticated_context():
    try:
        OpenAICorePolicy.require_tenant_context(None)
    except PermissionError:
        pass
    else:
        raise AssertionError("Authenticated tenant context must be required")


def test_tenant_context_validation_and_capability_authorization():
    service = importlib.import_module(
        "backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem.openai_agents_core_ecosystem"
    ).get_manager()
    context = TenantContext(tenant_id="tenant-test", actor_id="user-test")
    result = service.authorize_capability("MANAGED_AGENT_API_METADATA", context)
    assert result["success"] is True
    assert result["data"]["api_call_performed"] is False


def test_retired_sora_is_not_enabled_or_authorizable():
    sora = importlib.import_module(
        "backend.core.global_ecosystem.global_core_ecosystem.openai_core_ecosystem.openai_sora_core_ecosystem"
    ).get_manager()
    status = sora.status()
    assert status["enabled"] is False
    assert status["readiness"] == "RETIRED_REFERENCE_ONLY"
    denied = sora.authorize_capability("RETIRED_PRODUCT_REFERENCE_ONLY", TenantContext("t", "u"))
    assert denied["success"] is False


def test_master_catalog_alignment_is_read_only_and_does_not_claim_2468_entries():
    master = get_openai_core_catalog()["master_catalog"]
    assert master["path"] == "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    assert master["target_unique_entries"] == 2468
    assert master["catalog_entries_added"] == 0
    assert len(master["canonical_entry_ids"]) == 6


def test_manager_health_reports_catalog_not_live_connectivity():
    manager = get_manager()
    health = manager.health()
    assert health["product_family_count"] == 14
    assert health["domain_count"] == 11
    assert health["live_connections_verified"] == 0
    assert manager.status()["live_connection_verified"] is False


def test_public_metadata_sanitizer_removes_nested_credentials():
    cleaned = OpenAICorePolicy.safe_summary({
        "name": "OpenAI",
        "nested": {"api_key": "never-return", "safe": True},
    })
    assert "api_key" not in cleaned["nested"]
    assert cleaned["nested"]["safe"] is True
