"""Structural regression checks for the mirrored, independent ENGINE ecosystem."""
from pathlib import Path
import re

BACKEND = Path(__file__).resolve().parents[1]
API_ROOT = BACKEND / "api" / "global_ecosystem" / "global_api_ecosystem"
ENGINE_ROOT = BACKEND / "engine" / "global_ecosystem" / "global_engine_ecosystem"

KAMASUTRA_API_ROOT = (
    "global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem"
)
KAMASUTRA_ENGINE_ROOT = (
    "global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_engine_ecosystem"
)


def _engine_relative(api_relative: Path) -> Path:
    parts = []
    for part in api_relative.parts:
        if part == KAMASUTRA_API_ROOT:
            parts.append(KAMASUTRA_ENGINE_ROOT)
        elif part.endswith("_api_ecosystem"):
            parts.append(part[:-len("_api_ecosystem")] + "_engine_ecosystem")
        else:
            parts.append(part)
    return Path(*parts)


def test_engine_mirrors_every_api_provider_directory_without_importing_it():
    api_dirs = sorted(path.relative_to(API_ROOT) for path in API_ROOT.rglob("*") if path.is_dir())
    assert api_dirs, "API provider tree must not be empty"
    for relative in api_dirs:
        engine_dir = ENGINE_ROOT / _engine_relative(relative)
        if relative.name == "tests":
            # API test directories are represented by one ENGINE-side test.py file.
            engine_test = engine_dir.parent / "test.py"
            assert engine_test.is_file(), f"Missing ENGINE test file: {engine_test}"
            continue
        assert engine_dir.is_dir(), f"Missing ENGINE directory: {engine_dir}"
        assert (engine_dir / "__init__.py").is_file(), f"Missing package initializer: {engine_dir}"


def test_every_provider_leaf_has_an_engine_execution_boundary():
    api_dirs = [path for path in API_ROOT.rglob("*") if path.is_dir()]
    api_dir_set = set(api_dirs)
    leaves = [
        path for path in api_dirs
        if path.name not in {"shared", "tests"}
        and not any(child.parent == path for child in api_dir_set)
    ]
    assert leaves, "API provider tree must contain leaf providers"
    for leaf in leaves:
        relative = leaf.relative_to(API_ROOT)
        engine_leaf = ENGINE_ROOT / _engine_relative(relative)
        assert (engine_leaf / "engine.py").is_file(), f"Missing provider engine: {engine_leaf}"


def test_all_provider_roots_have_independent_engine_modules():
    roots = [path for path in API_ROOT.iterdir() if path.is_dir()]
    assert roots, "API provider tree must contain provider roots"
    required = ("__init__.py", "models.py", "registry.py", "engine.py")
    for root in roots:
        engine_root = ENGINE_ROOT / _engine_relative(root.relative_to(API_ROOT))
        root_required = required if root.name == "global_infrastructure_api_ecosystem" else (*required, "manager.py")
        for filename in root_required:
            assert (engine_root / filename).is_file(), f"Missing {filename}: {engine_root}"
        if root.name == KAMASUTRA_API_ROOT:
            manager_source = (engine_root / "manager.py").read_text(encoding="utf-8")
            assert "CATALOG =" in manager_source, "Consolidated catalog must remain in manager.py"
        else:
            assert (engine_root / "catalog.py").is_file(), f"Missing catalog.py: {engine_root}"


def test_kamasutra_manager_loads_and_registers_all_62_existing_child_engines():
    from backend.engine.global_ecosystem.global_engine_ecosystem.global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_engine_ecosystem import (
        CHILD_ENGINE_MODULES,
        EcosystemEngineManager,
    )

    manager = EcosystemEngineManager()
    status = manager.status()
    assert len(CHILD_ENGINE_MODULES) == 62
    assert status["loaded_child_engine_count"] == 62
    assert status["registered_count"] == 62
    assert status["load_error_count"] == 0
    assert status["status"] == "NOT_CONFIGURED"


def test_kamasutra_manager_configures_and_executes_a_registered_child_engine():
    from backend.engine.global_ecosystem.global_engine_ecosystem.global_kamasutra_relationship_intimacy_sex_chudai_porn_adult_health_wellness_engine_ecosystem import (
        CHILD_ENGINE_MODULES,
        EcosystemEngineManager,
    )

    manager = EcosystemEngineManager()
    child_id = CHILD_ENGINE_MODULES[0]
    manager.configure_child(child_id, lambda operation, payload: {
        "operation": operation,
        "payload": payload,
    })
    result = manager.execute(child_id, "self-test", {"ok": True})
    assert result == {"operation": "self-test", "payload": {"ok": True}}
    assert manager.status()["configured_child_engine_count"] == 1
    assert manager.status()["status"] == "PARTIALLY_CONFIGURED"


def test_engine_ecosystem_source_has_no_api_or_core_imports():
    pattern = re.compile(r"^\\s*(?:from|import)\\s+backend\\.(?:api|core)(?:\\.|\\s|$)", re.MULTILINE)
    for source in (BACKEND / "engine" / "global_ecosystem").rglob("*.py"):
        if pattern.search(source.read_text(encoding="utf-8")):
            raise AssertionError(f"Cross-layer import found in {source}")
