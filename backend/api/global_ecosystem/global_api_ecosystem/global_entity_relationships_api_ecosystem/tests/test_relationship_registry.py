"""Validation tests for the shared cross-ecosystem relationship registry."""
import pytest
from backend.api.global_ecosystem.global_api_ecosystem.global_entity_relationships_api_ecosystem import service


def test_empty_registry_is_valid(monkeypatch):
    monkeypatch.setattr(service, "DATA_PATH", __import__("pathlib").Path("/nonexistent/relationships.json"))
    assert service.load_relationships() == []


def test_relationship_requires_stable_id_and_known_type(monkeypatch, tmp_path):
    data = tmp_path / "relationships.json"
    data.write_text('{"records":[{"relationship_id":"r1","source_entity_id":"company:1","target_entity_id":"platform:1","relationship_type":"unknown"}]}', encoding="utf-8")
    monkeypatch.setattr(service, "DATA_PATH", data)
    with pytest.raises(ValueError):
        service.load_relationships()


def test_verified_relationship_requires_provenance(monkeypatch, tmp_path):
    data = tmp_path / "relationships.json"
    data.write_text('{"records":[{"relationship_id":"r1","source_entity_id":"company:1","target_entity_id":"platform:1","relationship_type":"owns","verification_status":"verified"}]}', encoding="utf-8")
    monkeypatch.setattr(service, "DATA_PATH", data)
    with pytest.raises(ValueError):
        service.load_relationships()
