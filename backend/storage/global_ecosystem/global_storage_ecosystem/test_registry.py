"""Offline metadata tests for GLOBAL STORAGE ECOSYSTEM."""

from .registry import list_providers, get_provider


def test_provider_registry_is_nonempty_and_unconfigured_by_default():
    providers = list_providers()
    assert providers
    assert all(provider["status"] == "not_configured" for provider in providers)


def test_registry_lookup_is_case_insensitive():
    first = list_providers()[0]
    assert get_provider(first["provider_id"].upper())["provider_id"] == first["provider_id"]


def test_registry_rejects_unknown_provider():
    try:
        get_provider("provider-that-does-not-exist")
    except KeyError:
        pass
    else:
        raise AssertionError("Unknown provider must raise KeyError")
