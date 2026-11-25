"""Tests for the canonical infrastructure model contracts.

The former dedicated infrastructure CORE package was removed. Validation now
belongs to the existing provider-neutral GLOBAL MODEL ECOSYSTEM.
"""
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.model.global_ecosystem.global_model_ecosystem import (
    get_model_catalog,
    validate_resource_record,
)


def test_model_catalog_exposes_resource_identity():
    assert "resource_identity" in get_model_catalog()


def test_valid_resource_record_is_accepted():
    assert validate_resource_record({
        "resource_id": "srv-001",
        "resource_type": "vps",
        "category": "compute",
    }) == []


def test_incomplete_resource_record_is_rejected():
    errors = validate_resource_record({"resource_id": "", "resource_type": "vps"})
    assert "resource_id must be a non-empty string" in errors
    assert "category must be a non-empty string" in errors


def test_invalid_metadata_type_is_rejected():
    errors = validate_resource_record({
        "resource_id": "srv-002",
        "resource_type": "server",
        "category": "compute",
        "metadata": "not-a-mapping",
    })
    assert "metadata must be a mapping when provided" in errors
