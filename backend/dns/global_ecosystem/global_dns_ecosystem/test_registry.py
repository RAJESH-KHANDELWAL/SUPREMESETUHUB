"""Offline behavior tests for global DNS orchestration."""
import pytest

from .models import DNSChangeRequest, DNSRecord
from .registry import list_providers, get_provider
from .service import GlobalDNSService


class FakeDNSClient:
    provider_id = "cloudflare"

    def list_records(self, zone_id):
        return [{"zone_id": zone_id, "type": "A"}]

    def apply_change(self, zone_id, action, record):
        return {"zone_id": zone_id, "action": action, "record": record}


def test_registry_lists_only_unconfigured_provider_metadata():
    providers = list_providers()
    assert providers
    assert all(item["status"] == "not_configured" for item in providers)


def test_registry_lookup_is_case_insensitive():
    item = list_providers()[0]
    assert get_provider(item["provider_id"].upper())["provider_id"] == item["provider_id"]


def test_registry_rejects_unknown_provider():
    with pytest.raises(KeyError):
        get_provider("not-a-real-provider")


def test_injected_client_does_not_claim_live_connectivity():
    service = GlobalDNSService({"cloudflare": FakeDNSClient()})
    status = service.status()
    assert status["live_dns_connectivity_verified"] is False
    assert status["providers"][0]["connection_status"] == "adapter_injected_unverified"


def test_list_records_does_not_claim_connection_verified():
    service = GlobalDNSService({"cloudflare": FakeDNSClient()})
    result = service.list_records("cloudflare", "zone-1")
    assert result["adapter_call_completed"] is True
    assert result["live_connection_verified"] is False
    assert len(result["records"]) == 1


def test_unknown_provider_is_rejected_before_adapter_dispatch():
    service = GlobalDNSService({"cloudflare": FakeDNSClient()})
    with pytest.raises(KeyError):
        service.list_records("unknown", "zone-1")


def test_dns_change_requires_explicit_approval():
    service = GlobalDNSService({"cloudflare": FakeDNSClient()})
    request = DNSChangeRequest(
        provider_id="cloudflare", zone_id="zone-1", action="CREATE",
        record=DNSRecord("www.example.com", "A", "192.0.2.1"),
    )
    with pytest.raises(PermissionError):
        service.apply_change(request)


def test_approved_dns_change_does_not_claim_persisted_audit():
    service = GlobalDNSService({"cloudflare": FakeDNSClient()})
    request = DNSChangeRequest(
        provider_id="cloudflare", zone_id="zone-1", action="CREATE",
        record=DNSRecord("www.example.com", "A", "192.0.2.1"), approved=True,
    )
    result = service.apply_change(request)
    assert result["success"] is True
    assert result["explicit_approval_supplied"] is True
    assert result["approval_audit_persisted"] is False
