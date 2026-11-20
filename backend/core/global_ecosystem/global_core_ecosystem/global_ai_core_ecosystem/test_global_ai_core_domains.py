"""Google Core-style public manager and domain contract tests."""
from __future__ import annotations

from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem import (
    GlobalAICoreDomainManager,
    get_manager,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.catalog import (
    list_ai_providers,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.domain_catalog import (
    AI_DOMAIN_DEFINITIONS,
)


def test_global_ai_manager_public_contract():
    manager = get_manager()
    assert manager.status()["ecosystem_id"] == "GLOBAL-AI-CORE-ECOSYSTEM"
    assert manager.health()["provider_count"] == len(list_ai_providers())
    assert manager.list_products()["count"] == len(list_ai_providers())
    assert manager.list_domains()["domain_count"] == 19
    assert len(manager.list_domain_inventory()) == 19
    assert manager.get_product("openai")["id"] == "openai_chatgpt"
    assert manager.get_offering("openai_chatgpt")["id"] == "openai_chatgpt"
    assert manager.dependency_map()["success"] is True


def test_global_ai_domain_manager_is_scoped_to_registered_domain():
    manager = GlobalAICoreDomainManager("GLOBAL_FOUNDATION_MODELS")
    assert manager.status()["domain_id"] == "GLOBAL_FOUNDATION_MODELS"
    assert manager.list_products()["success"] is True
    assert manager.get_product("openai_chatgpt") is not None


def test_unknown_global_ai_domain_is_rejected():
    try:
        GlobalAICoreDomainManager("NOT_A_REAL_DOMAIN")
    except ValueError as exc:
        assert "UNKNOWN_GLOBAL_AI_CORE_DOMAIN" in str(exc)
    else:
        raise AssertionError("Unknown AI domain must be rejected")


def test_2468_master_catalog_is_referenced_not_loaded_or_counted_as_ai_providers():
    reference = get_manager().master_catalog_reference()
    assert reference["target_unique_entries"] == 2468
    assert reference["source_path"] == "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
    assert reference["loaded_by_global_ai_core"] is False
    assert len(list_ai_providers()) != 2468


def test_domain_definitions_remain_nineteen():
    assert len(AI_DOMAIN_DEFINITIONS) == 19
