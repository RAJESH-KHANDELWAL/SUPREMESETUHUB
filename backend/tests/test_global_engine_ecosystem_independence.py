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
