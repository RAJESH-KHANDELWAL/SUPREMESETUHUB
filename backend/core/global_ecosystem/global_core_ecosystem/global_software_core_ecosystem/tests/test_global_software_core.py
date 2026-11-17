from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.catalog import get_provider, list_providers
from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.orchestrator import build_plan
from backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem.policy import evaluate_activation


def test_initial_provider_inventory_is_explicitly_catalog_only():
    providers = list_providers()
    assert {item["provider_id"] for item in providers} == {
        "adobe", "apple", "aws", "github", "atlassian", "microsoft"
    }
    assert all(item["status"] == "CATALOG_ONLY" for item in providers)
    assert all(item["live_connection_verified"] is False for item in providers)


def test_provider_lookup_is_case_insensitive():
    assert get_provider("GitHub")["provider_id"] == "github"


def test_orchestration_returns_plan_only():
    plan = build_plan("github", "REPOSITORIES", tenant_id="tenant-demo")
    assert plan["status"] == "PLAN_ONLY"
    assert plan["execution_enabled"] is False


def test_unknown_provider_rejected():
    try:
        build_plan("unknown", "ANY", tenant_id="tenant-demo")
    except KeyError:
        pass
    else:
        raise AssertionError("unknown provider must be rejected")


def test_activation_requires_external_controls():
    decision = evaluate_activation(
        tenant_id=None, scopes=(), secret_reference=None, consent_recorded=False
    )
    assert decision.allowed is False
