import pytest
from global_ecosystem.global_cloudflare_ecosystem.client import (
    CloudflareAPIError, CloudflareClient,
)

def test_client_requires_token():
    with pytest.raises(ValueError):
        CloudflareClient("")

def test_client_validates_timeout():
    with pytest.raises(ValueError):
        CloudflareClient("test-token", timeout=0)

def test_client_rejects_invalid_zone_id_before_network():
    client = CloudflareClient("test-token")
    with pytest.raises(ValueError):
        client.get_zone("../invalid")

def test_client_validates_pagination_before_network():
    client = CloudflareClient("test-token")
    with pytest.raises(ValueError):
        client.list_zones(page=0)
    with pytest.raises(ValueError):
        client.list_dns_records("zone-id", per_page=101)

def test_api_error_type_is_exported():
    assert issubclass(CloudflareAPIError, RuntimeError)
