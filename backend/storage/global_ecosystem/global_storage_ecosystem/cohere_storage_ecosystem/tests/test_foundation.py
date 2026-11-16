"""Offline tests; these do not contact Cohere APIs."""
import pytest

from ..catalog_api import CohereStorageCatalog
from ..ecosystem_models import EcosystemRecord
from ..ecosystem_registry import EcosystemRegistry
from ..ecosystem_service import EcosystemService
from ..ecosystem_taxonomy import find_ecosystem, list_ecosystems, load_taxonomy


def test_health_does_not_claim_provider_connection():
    result = EcosystemService().health()
    assert result["success"]
    assert result["external_connections_verified"] is False


def test_registry_duplicate_guard():
    registry = EcosystemRegistry()
    row = EcosystemRecord("sample-1", "SAMPLE", "Sample")
    registry.register(row)
    with pytest.raises(ValueError, match="DUPLICATE_RECORD_ID"):
        registry.register(row)


def test_record_requires_identity_fields():
    with pytest.raises(ValueError):
        EcosystemRecord("", "SAMPLE", "Sample")


def test_taxonomy_loads_with_expected_identity():
    assert load_taxonomy()["ecosystem_id"] == "COHERE_STORAGE_ECOSYSTEM"


def test_taxonomy_index_matches_group_categories():
    expected = sum(len(group["categories"]) for group in load_taxonomy()["groups"])
    assert len(list_ecosystems()) == expected
    assert expected == 94


def test_taxonomy_lookup_is_case_insensitive():
    row = find_ecosystem("command")
    assert row is not None
    assert row["name"] == "COHERE_COMMAND_STORAGE_ECOSYSTEM"


def test_catalog_api_is_read_only_and_filterable():
    catalog = CohereStorageCatalog()
    assert catalog.health()["external_connections_verified"] is False
    assert catalog.list("LANGUAGE_AND_TEXT")
    assert catalog.get("EMBEDDINGS")["category"] == "EMBEDDINGS"


def test_taxonomy_does_not_claim_provider_products():
    assert load_taxonomy()["provider_product_verified"] is False
