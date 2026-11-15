"""Provider catalog tests."""
import pytest
from .registry import list_providers, get_provider

def test_six_providers_are_registered():
    assert len(list_providers()) == 6

def test_provider_lookup_is_case_insensitive():
    assert get_provider("AWS_STORAGE")["provider_id"] == "aws_storage"

def test_provider_results_are_defensive_copies():
    values = list_providers()
    values[0]["capabilities"].append("tampered")
    assert "tampered" not in list_providers()[0]["capabilities"]

def test_unknown_provider_raises_key_error():
    with pytest.raises(KeyError):
        get_provider("unknown")
