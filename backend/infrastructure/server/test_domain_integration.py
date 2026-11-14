"""Tests for the infrastructure facade's bridge to the canonical SERVER domain."""

import unittest

from backend.infrastructure.server.domain_integration import ServerDomainIntegration


class FakeServerDomain:
    def health(self):
        return {"domain": "SERVER", "external_connections": "NOT_ATTEMPTED"}

    def describe(self):
        return {"domain": "SERVER", "server_types": ["WEB", "VPS"]}

    def register(self, **kwargs):
        return {"server_id": "SRV-TEST", **kwargs}

    def get(self, server_id):
        return {"server_id": server_id}

    def list(self):
        return [{"server_id": "SRV-TEST"}]

    def update(self, server_id, **changes):
        return {"server_id": server_id, **changes}

    def delete(self, server_id):
        return {"server_id": server_id, "deleted": True}

    def start(self, server_id):
        return {"server_id": server_id, "status": "START_REQUESTED"}

    def stop(self, server_id):
        return {"server_id": server_id, "status": "STOP_REQUESTED"}

    def restart(self, server_id):
        return {"server_id": server_id, "status": "RESTART_REQUESTED"}

    def register_provider(self, provider_id, adapter, *, replace=False):
        return provider_id

    def describe_provider(self, provider_id):
        return {"provider": provider_id}

    def provider_health(self, provider_id):
        return {"provider": provider_id, "status": "NOT_PROBED"}

    def execute_provider_operation(self, provider_id, operation, payload=None):
        return {"provider": provider_id, "operation": operation, "payload": payload}

    def register_operation_adapter(self, capability, adapter, *, replace=False):
        return capability

    def execute_operation(self, capability, operation, payload=None):
        return {"capability": capability, "operation": operation, "payload": payload}


class ServerDomainIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.domain = ServerDomainIntegration(service=FakeServerDomain())

    def test_domain_crud_and_lifecycle_are_delegated(self):
        created = self.domain.register(name="test", server_type="WEB")
        self.assertEqual(created["server_id"], "SRV-TEST")
        self.assertEqual(self.domain.get("SRV-TEST")["server_id"], "SRV-TEST")
        self.assertEqual(len(self.domain.list()), 1)
        self.assertEqual(self.domain.update("SRV-TEST", region="ap-south-1")["region"], "ap-south-1")
        self.assertEqual(self.domain.start("SRV-TEST")["status"], "START_REQUESTED")
        self.assertEqual(self.domain.stop("SRV-TEST")["status"], "STOP_REQUESTED")
        self.assertEqual(self.domain.restart("SRV-TEST")["status"], "RESTART_REQUESTED")
        self.assertTrue(self.domain.delete("SRV-TEST")["deleted"])

    def test_health_and_provider_operations_are_delegated(self):
        self.assertEqual(self.domain.health()["external_connections"], "NOT_ATTEMPTED")
        self.assertEqual(self.domain.describe()["domain"], "SERVER")
        self.assertEqual(self.domain.provider_health("aws")["status"], "NOT_PROBED")
        result = self.domain.execute_provider_operation("aws", "inspect", {"id": "x"})
        self.assertEqual(result["operation"], "inspect")
        result = self.domain.execute_operation("DEPLOYMENT", "release", {"version": "1"})
        self.assertEqual(result["capability"], "DEPLOYMENT")


if __name__ == "__main__":
    unittest.main()
