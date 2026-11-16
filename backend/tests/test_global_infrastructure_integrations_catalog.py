"""Regression coverage for the Global Infrastructure integrations package export."""

from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.integrations import (
    INTEGRATIONS,
)


def test_integrations_package_exports_catalog_records() -> None:
    assert isinstance(INTEGRATIONS, tuple)
    assert INTEGRATIONS
    assert all(hasattr(record, "to_dict") for record in INTEGRATIONS)


def test_integrations_catalog_preserves_expected_boundary_entries() -> None:
    ids = {record.id for record in INTEGRATIONS}
    assert "core_foundation" in ids
    assert "api_orchestration_boundary" in ids
    assert "engine_execution_boundary" in ids
