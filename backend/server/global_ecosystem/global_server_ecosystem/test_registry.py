"""Compatibility tests for lowercase SERVER ecosystem imports."""
from .registry import list_providers, get_provider, list_service_types
from . import EcosystemService


def test_lowercase_package_exports_full_provider_and_service_catalog():
    assert list_providers()
    assert list_service_types()
    assert get_provider("AWS")["provider_id"] == "aws"


def test_lowercase_package_exposes_canonical_service():
    service = EcosystemService()
    assert service.status()["status"] == "FOUNDATION_READY"
