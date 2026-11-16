import pytest

from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.catalog import (
    get_ai_provider,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.contracts import (
    Readiness,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.module_service import (
    AIProductCoreService,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.policy import (
    GlobalAICorePolicy,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.request_contracts import (
    validate_ai_request,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.service import (
    GlobalAICoreService,
)


def test_legacy_openai_alias_resolves_to_canonical_provider():
    provider = get_ai_provider("openai")
    assert provider is not None
    assert provider["id"] == "openai_chatgpt"


def test_task_service_uses_canonical_default_provider():
    captured = {}

    def executor(**kwargs):
        captured.update(kwargs)
        return {"output": "ok"}

    result = GlobalAICoreService(executor).generate(task="hello")
    assert result["success"] is True
    assert captured["provider_id"] == "openai_chatgpt"


def test_unknown_provider_is_rejected_before_engine_execution():
    called = False

    def executor(**kwargs):
        nonlocal called
        called = True
        return {"output": "unexpected"}

    with pytest.raises(LookupError, match="AI_PROVIDER_NOT_REGISTERED"):
        GlobalAICoreService(executor).generate(task="hello", provider_id="not-a-provider")
    assert called is False


def test_request_contract_rejects_nested_secret_material():
    with pytest.raises(ValueError, match="SECRET_MATERIAL_FORBIDDEN_IN_CORE"):
        validate_ai_request({
            "provider_id": "openai_chatgpt",
            "capability": "text",
            "task": "hello",
            "context": {"nested": {"api-key": "must-not-enter-core"}},
        })


def test_request_contract_requires_provider_capability_and_task():
    with pytest.raises(ValueError, match="AI_REQUEST_REQUIRED_FIELDS_MISSING"):
        validate_ai_request({"provider_id": "openai_chatgpt"})


def test_provider_summary_recursively_filters_secrets_without_mutation():
    source = {"id": "sample", "metadata": {"api_key": "secret", "region": "global"}}
    safe = GlobalAICorePolicy.safe_provider_summary(source)
    assert safe == {"id": "sample", "metadata": {"region": "global"}}
    assert source["metadata"]["api_key"] == "secret"


def test_live_registry_label_is_not_reported_as_verified_ready():
    class SampleCore(AIProductCoreService):
        PROVIDER_ID = "openai_chatgpt"

    service = SampleCore()
    service._provider["integration_status"] = "live"
    status = service.status()
    assert status["readiness"] == Readiness.LIVE_VERIFICATION_REQUIRED.value
    assert status["live_connection_verified"] is False
