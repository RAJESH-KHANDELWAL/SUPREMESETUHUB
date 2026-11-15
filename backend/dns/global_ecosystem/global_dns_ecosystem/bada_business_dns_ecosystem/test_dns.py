"""Offline tests for Bada Business DNS tenant facade."""
import pytest

from ..models import DNSChangeRequest, DNSRecord
from ..service import GlobalDNSService
from .models import BusinessDomainDNSBinding
from .service import BadaBusinessDNSService


class BindingRepository:
    def __init__(self, binding):
        self.binding = binding

    def get_binding(self, tenant_id, domain):
        if self.binding.tenant_id == tenant_id and self.binding.normalized_domain == domain:
            return self.binding
        return None


class FakeDNSClient:
    def list_records(self, zone_id):
        return [{"zone_id": zone_id, "type": "A"}]

    def apply_change(self, zone_id, action, record):
        return {"zone_id": zone_id, "action": action, "record": record}


def make_service():
    binding = BusinessDomainDNSBinding(
        tenant_id="tenant-1", domain="example.com",
        provider_id="cloudflare", zone_id="zone-1",
    )
    return BadaBusinessDNSService(
        BindingRepository(binding),
        GlobalDNSService({"cloudflare": FakeDNSClient()}),
    )


def test_domain_binding_is_tenant_scoped():
    service = make_service()
    assert service.get_domain_binding("tenant-1", "EXAMPLE.COM").zone_id == "zone-1"
    with pytest.raises(LookupError):
        service.get_domain_binding("tenant-2", "example.com")


def test_list_records_delegates_to_shared_dns_service():
    result = make_service().list_records("tenant-1", "example.com")
    assert result["success"] is True
    assert result["live_connection_verified"] is False
    assert result["dns_result"]["records"][0]["type"] == "A"


def test_change_must_match_bound_provider_and_zone():
    service = make_service()
    request = DNSChangeRequest(
        provider_id="hostinger", zone_id="zone-1", action="CREATE",
        record=DNSRecord("www.example.com", "A", "192.0.2.10"), approved=True,
    )
    with pytest.raises(PermissionError):
        service.apply_change("tenant-1", "example.com", request)


def test_change_requires_explicit_approval_via_shared_service():
    service = make_service()
    request = DNSChangeRequest(
        provider_id="cloudflare", zone_id="zone-1", action="CREATE",
        record=DNSRecord("www.example.com", "A", "192.0.2.10"),
    )
    with pytest.raises(PermissionError):
        service.apply_change("tenant-1", "example.com", request)


def test_approved_change_delegates_to_shared_dns_service():
    service = make_service()
    request = DNSChangeRequest(
        provider_id="cloudflare", zone_id="zone-1", action="CREATE",
        record=DNSRecord("www.example.com", "A", "192.0.2.10"), approved=True,
    )
    result = service.apply_change("tenant-1", "example.com", request)
    assert result["success"] is True
    assert result["dns_result"]["explicit_approval_supplied"] is True
