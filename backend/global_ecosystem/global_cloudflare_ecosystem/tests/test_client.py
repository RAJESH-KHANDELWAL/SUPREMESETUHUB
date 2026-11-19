import pytest
from global_ecosystem.global_cloudflare_ecosystem.client import CloudflareAPIError, CloudflareClient

def test_token_is_required():
    with pytest.raises(ValueError): CloudflareClient("")

def test_timeout_must_be_positive():
    with pytest.raises(ValueError): CloudflareClient("test-token",timeout=0)

def test_invalid_zone_id_is_rejected_without_network():
    with pytest.raises(ValueError): CloudflareClient("test-token").get_zone("../invalid")

def test_pagination_is_validated_without_network():
    client=CloudflareClient("test-token")
    with pytest.raises(ValueError): client.list_zones(page=0)
    with pytest.raises(ValueError): client.list_dns_records("zone-id",per_page=101)

def test_error_type_is_runtime_error():
    assert issubclass(CloudflareAPIError,RuntimeError)
