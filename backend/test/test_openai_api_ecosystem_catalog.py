from backend.api.global_ecosystem.global_api_ecosystem.openai_api_ecosystem.openai_api_ecosystem import (
    OPENAI_API_ECOSYSTEM,
    OPENAI_PRODUCTS,
    list_openai_api_ecosystems,
    list_openai_api_capabilities,
)


def test_openai_provider_identity_and_canonical_path():
    assert OPENAI_API_ECOSYSTEM["provider_id"] == "openai"
    assert OPENAI_API_ECOSYSTEM["name"] == "OPENAI API ECOSYSTEM"
    assert OPENAI_API_ECOSYSTEM["folder"].endswith("/openai_api_ecosystem")


def test_openai_named_products_are_separate_children():
    result = list_openai_api_ecosystems()
    assert result["success"] is True
    assert result["live_connection_verified"] is False
    assert result["count"] == 14
    folders = {item["folder"] for item in result["ecosystems"]}
    assert "openai_chatgpt_api_ecosystem" in folders
    assert "openai_codex_api_ecosystem" in folders
    assert "openai_agents_api_ecosystem" in folders
    assert "openai_sora_api_ecosystem" in folders
    assert len(OPENAI_PRODUCTS) == 14


def test_api_capabilities_are_separate_from_product_names():
    result = list_openai_api_capabilities()
    assert result["success"] is True
    assert "responses" in result["capabilities"]
    assert "embeddings" in result["capabilities"]
    assert "moderation" in result["capabilities"]
    assert "gmail" not in result["capabilities"]


def test_sora_is_not_marked_as_an_active_service():
    sora = next(item for item in OPENAI_PRODUCTS if item["id"] == "sora")
    assert sora["status"] == "retired_reference_only"


def test_child_catalog_entries_do_not_claim_live_adapters():
    for item in OPENAI_PRODUCTS:
        assert item["status"] in {
            "active_catalog",
            "availability_dependent_catalog",
            "public_beta_catalog",
            "retired_reference_only",
        }
