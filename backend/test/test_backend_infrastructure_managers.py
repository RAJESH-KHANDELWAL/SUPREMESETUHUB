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

def test_backend_frontend_infrastructure_connector_is_connected():
    from backend.infrastructure.backend_infrastructure_frontend_infrastructure_connect import (
        connect_infrastructure,
    )

    report = connect_infrastructure()
    assert report["connected"], report
    assert report["backend"]["present_domain_count"] == 21
    assert report["frontend"]["healthy"]

def test_frontend_global_infrastructure_ecosystem_has_no_domain_modules():
    from frontend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.manager import (
        get_manager as get_frontend_ecosystem_manager,
    )
    from frontend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect import (
        connect_infrastructure,
    )

    report = get_frontend_ecosystem_manager().health()
    connection = connect_infrastructure()
    assert report["healthy"], report
    assert report["backend_present_domain_count"] == 21
    assert report["frontend_domain_files_expected"] == 0
    assert report["frontend_domain_folders_expected"] == 0
    assert connection["connected"], connection
    assert connection["frontend"]["domain_file_count"] == 0
    assert connection["frontend"]["domain_folder_count"] == 0
    frontend_root = Path(__file__).resolve().parents[2] / "frontend" / "infrastructure" / "global_ecosystem" / "global_infrastructure_ecosystem"
    domain_names = (
        "backup", "billing", "cdn", "containers", "database", "dns", "domains",
        "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
        "monitoring", "network", "object_storage", "security", "server", "ssl", "storage",
    )
    assert not any((frontend_root / f"{name}.py").exists() for name in domain_names)
    assert not any((frontend_root / name).exists() for name in domain_names)


def test_root_infrastructure_foundation_connectors_are_connected():
    from backend.infrastructure.backend_infrastructure_frontend_foundation_connect import (
        connect_foundation as backend_to_frontend,
    )
    from frontend.infrastructure.frontend_infrastructure_backend_foundation_connect import (
        connect_foundation as frontend_to_backend,
    )

    backend_report = backend_to_frontend()
    frontend_report = frontend_to_backend()
    assert backend_report["connected"], backend_report
    assert frontend_report["connected"], frontend_report
