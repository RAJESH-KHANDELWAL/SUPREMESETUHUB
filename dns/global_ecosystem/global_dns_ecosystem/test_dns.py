"""Offline tests for DNS contracts and fail-closed provider behavior."""
import unittest
from .models import DNSRecord, DNSChangeRequest
from .manager import GlobalDNSManager

class FakeClient:
    def __init__(self):
        self.changes = []
    def list_records(self, zone_id):
        return [{"zone_id": zone_id, "type": "A"}]
    def apply_change(self, zone_id, action, record):
        self.changes.append((zone_id, action, record))
        return {"change_id": "test-change"}

class GlobalDNSTests(unittest.TestCase):
    def test_record_validation(self):
        self.assertEqual(DNSRecord("example.com", "A", "192.0.2.1").validate().to_dict()["type"], "A")
        with self.assertRaises(ValueError):
            DNSRecord("example.com", "INVALID", "x").validate()

    def test_no_client_fails_closed(self):
        with self.assertRaises(RuntimeError):
            GlobalDNSManager().list_records("cloudflare", "zone-1")

    def test_change_requires_approval(self):
        manager = GlobalDNSManager(provider_clients={"cloudflare": FakeClient()})
        request = DNSChangeRequest("cloudflare", "zone-1", "CREATE", DNSRecord("www.example.com", "A", "192.0.2.1"))
        with self.assertRaises(PermissionError):
            manager.apply_change(request)

    def test_approved_change_uses_injected_client(self):
        client = FakeClient()
        manager = GlobalDNSManager(provider_clients={"cloudflare": client})
        request = DNSChangeRequest("cloudflare", "zone-1", "CREATE", DNSRecord("www.example.com", "A", "192.0.2.1"), approved=True)
        self.assertTrue(manager.apply_change(request)["success"])
        self.assertEqual(len(client.changes), 1)

    def test_status_does_not_claim_verified_connectivity(self):
        manager = GlobalDNSManager(provider_clients={"cloudflare": FakeClient()})
        self.assertFalse(manager.status()["live_dns_connectivity_verified"])

if __name__ == "__main__":
    unittest.main()
