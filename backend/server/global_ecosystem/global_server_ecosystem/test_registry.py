"""Offline registry tests for the SERVER ecosystem."""

from .registry import list_providers, get_provider


def test_registry_lists_only_unconfigured_provider_metadata():
    providers = list_providers()
    assert providers
    assert all(provider["status"] == "not_configured" for provider in providers)


def test_registry_lookup_is_case_insensitive():
    provider = list_providers()[0]
    assert get_provider(provider["provider_id"].upper())["provider_id"] == provider["provider_id"]


def test_registry_rejects_unknown_provider():
    try:
        get_provider("not-a-real-provider")
    except KeyError:
        pass
    else:
        raise AssertionError("Unknown provider must raise KeyError")
