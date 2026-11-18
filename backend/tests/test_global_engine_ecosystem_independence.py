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
    actual = {
        item["ecosystem_id"]
        .removeprefix("GLOBAL-")
        .removesuffix("-ENGINE-ECOSYSTEM")
        .lower()
        .replace("-", "_")
        for item in CATEGORIES
    }
    assert expected.issubset(actual)


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
    from backend.engine.global_ecosystem.catalog import (
        CATEGORIES, PROVIDER_ECOSYSTEMS, get_catalog, get_provider_catalog,
    )

    provider_records = get_provider_catalog()
    category_ids = {item["ecosystem_id"] for item in CATEGORIES}
    assert PROVIDER_ECOSYSTEMS
    assert len(PROVIDER_ECOSYSTEMS) == len(provider_records)
    assert len(get_catalog()) == 1 + len(CATEGORIES) + len(provider_records)
    assert all(item["ecosystem_type"] == "ENGINE_MODULE" for item in provider_records)
    assert all(item["ecosystem_id"].endswith("-ENGINE-ECOSYSTEM") for item in provider_records)
    assert all(item["parent_id"] in category_ids for item in provider_records)


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


def test_provider_engine_packages_are_scaffolded_without_api_imports():
    from pathlib import Path
    import backend.engine.global_ecosystem.global_engine_ecosystem as engine_root

    root = Path(engine_root.__file__).parent
    assert (root / "global_ai_engine_ecosystem" / "openai_ai_engine_ecosystem" / "engine.py").exists()
    assert (root / "aws_engine_ecosystem" / "aws_lambda_engine_ecosystem" / "engine.py").exists()
    # ENGINE may orchestrate CORE contracts; transport/API imports remain forbidden.
    for path in root.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        assert "from backend.api." not in source
        assert "import backend.api." not in source
