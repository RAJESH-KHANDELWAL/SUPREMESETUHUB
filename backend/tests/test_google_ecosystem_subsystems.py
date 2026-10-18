from backend.google.google_ecosystem.engine.service import (
    get_subsystem,
    list_subsystems,
)


def test_google_ecosystem_subsystems_are_registered():
    assert list_subsystems() == [
        "cloud",
        "database",
        "dns",
        "storage",
        "vpn",
        "vps",
    ]


def test_google_ecosystem_subsystems_return_metadata_without_claiming_connection():
    for subsystem in list_subsystems():
        result = get_subsystem(subsystem)
        assert result["subsystem"] == subsystem
        assert result["capabilities"]
        assert all(item["provider"] == "google" for item in result["capabilities"])
        assert all(item["connected"] is False for item in result["capabilities"])
        assert all(item["status"] == "METADATA_ONLY" for item in result["capabilities"])


def test_google_vps_label_is_explained_as_compute_engine_vm():
    result = get_subsystem("vps")
    assert result["capabilities"][0]["product"] == "Google Compute Engine VM"


def test_unknown_google_subsystem_is_rejected():
    try:
        get_subsystem("unknown")
    except KeyError as exc:
        assert "Unsupported Google ecosystem subsystem" in str(exc)
    else:
        raise AssertionError("Unknown subsystem must raise KeyError")
