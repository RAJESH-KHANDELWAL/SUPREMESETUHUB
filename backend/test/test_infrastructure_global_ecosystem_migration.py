"""Regression tests for canonical Infrastructure module ownership and compatibility."""
from importlib import import_module
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "infrastructure" / "global_ecosystem" / "global_infrastructure_ecosystem" / "modules"
REQUIRED = ("controller.py", "repository.py", "service.py", "hostinger_catalog.py", "__init__.py")

def test_canonical_infrastructure_modules_exist():
    assert CANONICAL.is_dir()
    for filename in REQUIRED:
        assert (CANONICAL / filename).is_file(), filename

def test_module_registry_points_to_ecosystem_ownership():
    registry = import_module("backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules")
    for name in ("controller", "repository", "service", "hostinger_catalog"):
        assert registry.ROOT_MODULES[name].startswith(
            "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules."
        )

def test_root_compatibility_shims_import_canonical_classes():
    canonical = "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules"
    assert import_module("backend.infrastructure.controller").InfrastructureController is import_module(f"{canonical}.controller").InfrastructureController
    assert import_module("backend.infrastructure.repository").InfrastructureRepository is import_module(f"{canonical}.repository").InfrastructureRepository
    assert import_module("backend.infrastructure.service").InfrastructureService is import_module(f"{canonical}.service").InfrastructureService

def test_hostinger_catalog_compatibility_shim():
    old = import_module("backend.infrastructure.hostinger_catalog")
    canonical = import_module("backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules.hostinger_catalog")
    assert old.hostinger_catalog is canonical.hostinger_catalog
    assert old.hostinger_readiness is canonical.hostinger_readiness


def test_python_managers_report_canonical_structure():
    from backend.infrastructure.manager import get_manager
    from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.manager import get_manager as get_ecosystem_manager
    root_health = get_manager().health()
    ecosystem_health = get_ecosystem_manager().health()
    assert root_health["healthy"], root_health
    assert ecosystem_health["healthy"], ecosystem_health
