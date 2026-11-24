"""Regression tests for the independent GLOBAL ENGINE ecosystem layer."""
from backend.engine.global_ecosystem import GlobalEcosystemManager

def test_engine_manager_owns_an_independent_registry():
    manager = GlobalEcosystemManager()
    assert manager.status()["success"] is True
    assert manager.exists("GLOBAL-ENGINE-ECOSYSTEM")
    assert manager.registry.count() == manager.list()["count"]

def test_engine_catalog_mirrors_the_shared_category_taxonomy():
    from backend.engine.global_ecosystem.catalog import CATEGORIES
    from backend.engine.global_ecosystem.global_engine_ecosystem import LAYER
    assert LAYER == "ENGINE"
    expected = {
        "companies", "platforms", "server", "ai", "software_ai", "cloud",
        "security", "individual", "developer", "communication", "language",
        "video", "payment", "storage", "system", "hosting", "intimacy",
        "domain", "web", "social_media", "freelancer", "database",
    }
    assert {item[0].lower() for item in CATEGORIES} == expected

def test_engine_packages_do_not_import_sibling_layers():
    import inspect
    import backend.engine.global_ecosystem.manager as manager_module
    import backend.engine.global_ecosystem.models as models_module
    import backend.engine.global_ecosystem.registry as registry_module
    import backend.engine.global_ecosystem.catalog as catalog_module
    source = "\n".join(inspect.getsource(module) for module in (
        manager_module, models_module, registry_module, catalog_module
    ))
    assert "backend.core.global_ecosystem" not in source
    assert "backend.api.global_ecosystem" not in source


def test_engine_catalog_includes_full_provider_hierarchy():
    from backend.engine.global_ecosystem.catalog import PROVIDER_ECOSYSTEMS, get_provider_catalog, get_catalog
    assert len(PROVIDER_ECOSYSTEMS) == 58
    provider_records = get_provider_catalog()
    assert len(provider_records) == 3382
    assert sum(item["ecosystem_type"] == "PROVIDER_OR_DOMAIN" for item in provider_records) == 58
    assert len(get_catalog()) == 1 + 22 + len(provider_records)
    assert all(item["ecosystem_id"].endswith("-ENGINE-ECOSYSTEM") for item in provider_records)
    ids = {item["ecosystem_id"] for item in provider_records}
    assert all(item["parent_id"] == "GLOBAL-ENGINE-ECOSYSTEM" or item["parent_id"] in ids for item in provider_records)


def test_all_engine_categories_have_independent_runtime_modules():
    from pathlib import Path
    import backend.engine.global_ecosystem.global_engine_ecosystem as engine_root
    root = Path(engine_root.__file__).parent
    categories = (
        "companies", "platforms", "server", "ai", "software_ai", "cloud",
        "security", "individual", "developer", "communication", "language",
        "video", "payment", "storage", "system", "hosting", "intimacy",
        "domain", "web", "social_media", "freelancer", "database",
    )
    required = {"models.py", "catalog.py", "registry.py", "manager.py", "engine.py"}
    for category in categories:
        package = root / f"global_{category}_engine_ecosystem"
        assert required.issubset({item.name for item in package.iterdir()})


def test_provider_engine_packages_are_scaffolded_without_sibling_layer_imports():
    from pathlib import Path
    import backend.engine.global_ecosystem.global_engine_ecosystem as engine_root
    root = Path(engine_root.__file__).parent
    assert (root / "global_ai_engine_ecosystem" / "openai_ai_engine_ecosystem" / "engine.py").exists()
    assert (root / "aws_engine_ecosystem" / "aws_lambda_engine_ecosystem" / "engine.py").exists()
    for path in root.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        assert "from backend.api." not in source
        assert "import backend.api." not in source
        assert "from backend.core." not in source
        assert "import backend.core." not in source
