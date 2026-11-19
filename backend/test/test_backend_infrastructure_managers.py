"""Backend Infrastructure manager and ownership tests."""
from pathlib import Path

from backend.infrastructure.manager import get_manager as get_backend_manager
from backend.infrastructure.global_ecosystem.manager import get_manager as get_global_manager
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.manager import (
    get_manager as get_ecosystem_manager,
)
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.structure import (
    INFRASTRUCTURE_MODULES,
)


def test_backend_infrastructure_root_manager_is_healthy():
    report = get_backend_manager().health()
    assert report["healthy"], report


def test_backend_global_infrastructure_entry_manager_is_healthy():
    report = get_global_manager().health()
    assert report["healthy"], report


def test_backend_global_infrastructure_ecosystem_has_all_domains():
    report = get_ecosystem_manager().health()
    assert report["healthy"], report
    assert report["expected_domain_count"] == 21
    assert report["present_domain_count"] == 21
    assert len(INFRASTRUCTURE_MODULES) == 21


def test_global_infrastructure_service_reports_read_only_provider_state():
    overview = get_ecosystem_manager().overview()
    assert overview["provider_operations_enabled"] is False


def test_frontend_infrastructure_scaffold_checks_backend_managers_and_domains():
    root = Path(__file__).resolve().parents[2]
    frontend = root / "frontend" / "infrastructure"
    connector_path = frontend / "frontend_infrastructure_backend_infrastructure_connect.py"
    assert connector_path.is_file()
    assert (root / "backend" / "infrastructure" / "manager.py").is_file()
    assert (root / "backend" / "infrastructure" / "global_ecosystem" / "manager.py").is_file()
    assert (root / "backend" / "infrastructure" / "global_ecosystem" /
            "global_infrastructure_ecosystem" / "manager.py").is_file()


def test_infrastructure_ecosystem_does_not_duplicate_core_ownership():
    root = Path(__file__).resolve().parents[2]
    infrastructure_ecosystem = (
        root / "backend" / "infrastructure" / "global_ecosystem"
        / "global_infrastructure_ecosystem"
    )
    canonical_google_core = (
        root / "backend" / "core" / "global_ecosystem"
        / "global_core_ecosystem" / "google_core_ecosystem"
    )
    assert canonical_google_core.is_dir()
    assert not (infrastructure_ecosystem / "CORE").exists()
