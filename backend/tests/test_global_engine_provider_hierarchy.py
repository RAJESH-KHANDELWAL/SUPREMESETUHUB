"""Structural regression checks for the mirrored, independent ENGINE ecosystem."""
from pathlib import Path
import re

BACKEND = Path(__file__).resolve().parents[1]
API_ROOT = BACKEND / "api" / "global_ecosystem" / "global_api_ecosystem"
ENGINE_ROOT = BACKEND / "engine" / "global_ecosystem" / "global_engine_ecosystem"
_GENERATED_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def _is_source_directory(path: Path) -> bool:
    return path.is_dir() and path.name not in _GENERATED_DIRS and not path.name.startswith(".")


def _engine_relative(api_relative: Path) -> Path:
    parts = [
        part[:-len("_api_ecosystem")] + "_engine_ecosystem"
        if part.endswith("_api_ecosystem") else part
        for part in api_relative.parts
    ]
    return Path(*parts)


def test_engine_mirrors_every_api_provider_directory_without_importing_it():
    api_dirs = sorted(
        path.relative_to(API_ROOT)
        for path in API_ROOT.rglob("*")
        if _is_source_directory(path)
    )
    assert api_dirs, "No API ecosystem directories were discovered"
    for relative in api_dirs:
        engine_dir = ENGINE_ROOT / _engine_relative(relative)
        assert engine_dir.is_dir(), f"Missing ENGINE directory: {engine_dir}"
        assert (engine_dir / "__init__.py").is_file(), f"Missing package initializer: {engine_dir}"


def test_every_provider_leaf_has_an_engine_execution_boundary():
    api_dirs = [
        path for path in API_ROOT.rglob("*")
        if _is_source_directory(path)
    ]
    api_dir_set = set(api_dirs)
    leaves = [
        path for path in api_dirs
        if not any(child.parent == path for child in api_dir_set)
    ]
    assert leaves, "No API provider leaf directories were discovered"
    for leaf in leaves:
        relative = leaf.relative_to(API_ROOT)
        engine_leaf = ENGINE_ROOT / _engine_relative(relative)
        assert (engine_leaf / "engine.py").is_file(), f"Missing provider engine: {engine_leaf}"


def test_all_provider_roots_have_independent_engine_modules():
    roots = [
        path for path in API_ROOT.iterdir()
        if _is_source_directory(path) and path.name.endswith("_api_ecosystem")
    ]
    assert roots, "No top-level API provider roots were discovered"
    required = ("__init__.py", "catalog.py", "manager.py", "models.py", "registry.py", "engine.py")
    for root in roots:
        engine_root = ENGINE_ROOT / _engine_relative(root.relative_to(API_ROOT))
        for filename in required:
            assert (engine_root / filename).is_file(), f"Missing {filename}: {engine_root}"


def test_engine_ecosystem_source_does_not_import_api_layer():
    pattern = re.compile(r"^\s*(?:from|import)\s+backend\.api(?:\.|\s|$)", re.MULTILINE)
    for source in (BACKEND / "engine" / "global_ecosystem").rglob("*.py"):
        if pattern.search(source.read_text(encoding="utf-8")):
            raise AssertionError(f"ENGINE must not import API layer: {source}")
