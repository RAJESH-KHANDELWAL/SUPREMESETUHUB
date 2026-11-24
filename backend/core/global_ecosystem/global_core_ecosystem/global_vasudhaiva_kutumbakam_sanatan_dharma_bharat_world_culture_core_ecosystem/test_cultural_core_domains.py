"""Structural and behavior tests for cultural Core domain packages."""
import importlib

from .domain_catalog import DOMAIN_DEFINITIONS, domain_summary
from .domain_runtime import CulturalCoreDomainManager
from .manager import CulturalCoreManager, get_manager
from .service import get_manager as get_service_manager
from .contracts import TenantContext
from .policy import CulturalCorePolicy, CulturalCorePolicyError


def test_thirteen_domains_and_four_pillars():
    assert len(DOMAIN_DEFINITIONS) == 13
    assert domain_summary()["pillar_count"] == 4


def test_each_domain_package_has_a_working_manager():
    base = "backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem"
    for domain_id, item in DOMAIN_DEFINITIONS.items():
        package = importlib.import_module(f"{base}.{item['package_name']}")
        manager = package.get_manager()
        assert manager.DOMAIN_ID == domain_id
        assert manager.status()["source_domain_available"] is True
        assert manager.list_offerings()["success"] is True


def test_unknown_domain_is_rejected():
    try:
        CulturalCoreDomainManager("NOT_A_DOMAIN")
    except ValueError as exc:
        assert "UNKNOWN_CULTURAL_CORE_DOMAIN" in str(exc)
    else:
        raise AssertionError("unknown domain must be rejected")


def test_manager_reports_no_unverified_connections_or_resource_count():
    health = get_manager().health()
    assert health["domain_count"] == 13
    assert health["live_connections_verified"] == 0
    assert health["resource_count_verified"] is False


def test_google_core_aligned_manager_interface():
    manager = get_manager()
    assert isinstance(manager, CulturalCoreManager)
    assert manager.status()["ecosystem_id"] == manager.ECOSYSTEM_ID
    assert manager.list_products()["count"] == 13
    assert len(manager.list_domain_inventory()) == 13
    assert manager.list_offerings()["count"] == 13
    assert manager.get_product("SANATAN_DHARMA")["domain_id"] == "SANATAN_DHARMA"
    assert manager.get_offering("sanatan_dharma_cultural_core_ecosystem")["domain_id"] == "SANATAN_DHARMA"
    assert manager.get_product("UNKNOWN_DOMAIN") is None


def test_service_manager_factory_remains_backward_compatible():
    assert isinstance(get_service_manager(), CulturalCoreManager)


def test_tenant_and_rights_policy():
    try:
        CulturalCorePolicy.require_tenant_context(None)
    except CulturalCorePolicyError:
        pass
    else:
        raise AssertionError("tenant context is mandatory")
    CulturalCorePolicy.require_tenant_context(TenantContext("tenant", "actor"))
    assert CulturalCorePolicy.classify_access({"access_level": "restricted"}) == "RESTRICTED_ACCESS_DENIED"


def test_approved_record_requires_source_reference():
    record = {
        "record_id": "r1",
        "domain_id": "SANATAN_DHARMA",
        "title": "Test",
        "content": "Test",
        "source_kind": "documented",
        "confidence": "HIGH",
        "publication_status": "APPROVED",
    }
    assert "APPROVED_REQUIRES_SOURCE_REFERENCE" in CulturalCorePolicy.validate_record(record)
    record["source_url"] = "https://example.org/source"
    assert CulturalCorePolicy.validate_record(record) == []
