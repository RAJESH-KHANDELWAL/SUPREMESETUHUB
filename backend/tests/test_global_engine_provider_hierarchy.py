"""Structural regression checks for the mirrored, independent ENGINE ecosystem."""
from pathlib import Path
import re

BACKEND = Path(__file__).resolve().parents[1]
API_ROOT = BACKEND / "api" / "global_ecosystem" / "global_api_ecosystem"
ENGINE_ROOT = BACKEND / "engine" / "global_ecosystem" / "global_engine_ecosystem"

def _engine_relative(api_relative: Path) -> Path:
    parts = [
        part[:-len("_api_ecosystem")] + "_engine_ecosystem"
        if part.endswith("_api_ecosystem") else part
        for part in api_relative.parts
    ]
    return Path(*parts)

def test_engine_mirrors_every_api_provider_directory_without_importing_it():
    api_dirs = sorted(path.relative_to(API_ROOT) for path in API_ROOT.rglob("*") if path.is_dir())
    assert len(api_dirs) == 3382
    for relative in api_dirs:
        engine_dir = ENGINE_ROOT / _engine_relative(relative)
        assert engine_dir.is_dir(), f"Missing ENGINE directory: {engine_dir}"
        assert (engine_dir / "__init__.py").is_file(), f"Missing package initializer: {engine_dir}"

def test_every_provider_leaf_has_an_engine_execution_boundary():
    api_dirs = [path for path in API_ROOT.rglob("*") if path.is_dir()]
    api_dir_set = set(api_dirs)
    leaves = [
        path for path in api_dirs
        if not any(child.parent == path for child in api_dir_set)
    ]
    assert len(leaves) == 2716
    for leaf in leaves:
        relative = leaf.relative_to(API_ROOT)
        engine_leaf = ENGINE_ROOT / _engine_relative(relative)
        assert (engine_leaf / "engine.py").is_file(), f"Missing provider engine: {engine_leaf}"

def test_all_58_provider_roots_have_independent_engine_modules():
    roots = [path for path in API_ROOT.iterdir() if path.is_dir()]
    assert len(roots) == 58
    required = ("__init__.py", "catalog.py", "manager.py", "models.py", "registry.py", "engine.py")
    for root in roots:
        engine_root = ENGINE_ROOT / _engine_relative(root.relative_to(API_ROOT))
        for filename in required:
            assert (engine_root / filename).is_file(), f"Missing {filename}: {engine_root}"

def test_engine_ecosystem_source_has_no_api_or_core_imports():
    pattern = re.compile(r"^\s*(?:from|import)\s+backend\.(?:api|core)(?:\.|\s|$)", re.MULTILINE)
    for source in (BACKEND / "engine" / "global_ecosystem").rglob("*.py"):
        if pattern.search(source.read_text(encoding="utf-8")):
            raise AssertionError(f"Cross-layer import found in {source}")
