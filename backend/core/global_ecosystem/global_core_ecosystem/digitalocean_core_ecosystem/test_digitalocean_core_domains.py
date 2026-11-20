"""Structural and behavior tests for the DigitalOcean Core control plane."""
import unittest

from .catalog import get_catalog, list_capabilities
from .contracts import CoreResult, SecretReference, TenantContext
from .manager import get_manager
from .service import DigitalOceanCoreService


class DigitalOceanCoreTests(unittest.TestCase):
    def test_catalog_registers_five_capabilities(self):
        catalog = get_catalog()
        self.assertEqual(catalog["provider"], "digitalocean")
        self.assertEqual(set(list_capabilities()), {"cloud", "hosting", "server", "storage", "vps"})

    def test_manager_reports_metadata_only(self):
        status = get_manager().status()
        self.assertEqual(status["ecosystem_id"], "DIGITALOCEAN-CORE-ECOSYSTEM")
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)

    def test_all_capability_contracts_validate_without_live_calls(self):
        service = DigitalOceanCoreService()
        for capability in ("cloud", "hosting", "server", "storage", "vps"):
            with self.subTest(capability=capability):
                result = service.validate(capability, {"operation": "inspect"})
                self.assertEqual(result["capability"], capability)
                self.assertFalse(result["live_call"])

    def test_unknown_capability_is_rejected(self):
        with self.assertRaises(ValueError):
            get_manager().validate("unknown", {})

    def test_nested_secret_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            get_manager().validate("cloud", {"options": {"api_key": "never-accept"}})

    def test_unsupported_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            get_manager().validate("vps", {"unexpected": True})

    def test_execute_is_disabled(self):
        with self.assertRaisesRegex(RuntimeError, "LIVE_PROVIDER_CALLS_DISABLED"):
            DigitalOceanCoreService().execute()

    def test_tenant_context_and_secret_reference_contracts(self):
        TenantContext(tenant_id="tenant", actor_id="actor").validate()
        SecretReference(provider="digitalocean", reference="vault://digitalocean/key")
        self.assertEqual(CoreResult(success=True).to_dict()["ecosystem_id"], "DIGITALOCEAN-CORE-ECOSYSTEM")


if __name__ == "__main__":
    unittest.main()
