from backend.engines.subsystem_ecosystem_catalog import (
    get_subsystem_ecosystem,
    list_subsystem_ecosystems,
)


def test_catalog_contains_requested_subsystems():
    items = list_subsystem_ecosystems()
    ids = {item["subsystem_id"] for item in items}
    assert ids == {"core", "engine", "database", "storage", "dns", "vps", "vpn", "cloud"}
    assert all(item["external_connection_verified"] is False for item in items)


def test_catalog_returns_defensive_copies():
    items = list_subsystem_ecosystems()
    items[0]["name"] = "MUTATED"
    assert get_subsystem_ecosystem("CORE")["name"] == "GLOBAL CORE ECOSYSTEM"


def test_unknown_subsystem_returns_none():
    assert get_subsystem_ecosystem("not-a-subsystem") is None
