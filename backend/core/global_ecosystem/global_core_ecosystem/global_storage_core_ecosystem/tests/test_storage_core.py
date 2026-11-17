import unittest

from ..catalog import get_provider, list_providers
from ..domain_catalog import list_domains
from ..lifecycle import transition
from ..orchestrator import build_plan
from ..policy import validate_resource_metadata


class StorageCoreTests(unittest.TestCase):
    def test_inventory(self):
        self.assertEqual(
            {item["provider_id"] for item in list_providers()},
            {"apple", "aws", "digitalocean", "google", "microsoft"},
        )

    def test_domains(self):
        self.assertIn("OBJECT_STORAGE", list_domains())
        self.assertIn("BACKUP", list_domains())

    def test_rejects_bytes(self):
        payload = {
            "tenant_id": "t",
            "resource_id": "r",
            "provider_id": "aws",
            "resource_type": "object",
            "file_bytes": "x",
        }
        with self.assertRaisesRegex(ValueError, "SENSITIVE_PAYLOAD_NOT_ALLOWED"):
            validate_resource_metadata(payload)

    def test_accepts_metadata(self):
        result = validate_resource_metadata(
            {
                "tenant_id": "t",
                "resource_id": "r",
                "provider_id": "aws",
                "resource_type": "object",
            }
        )
        self.assertTrue(result["metadata_only"])

    def test_plan_only(self):
        result = build_plan(
            provider_id=" GOOGLE ",
            tenant_id="t",
            actor_id="a",
            operation=" upload ",
        )
        self.assertEqual(result["provider_id"], "google")
        self.assertEqual(result["operation"], "UPLOAD")
        self.assertTrue(result["plan_only"])
        self.assertFalse(result["data_transferred"])
        self.assertFalse(result["provider_call_performed"])

    def test_rejects_invalid_plan_inputs(self):
        with self.assertRaisesRegex(ValueError, "STORAGE_PROVIDER_ID_REQUIRED"):
            build_plan(provider_id=" ", tenant_id="t", actor_id="a", operation="LIST")
        with self.assertRaisesRegex(ValueError, "STORAGE_OPERATION_REQUIRED"):
            build_plan(provider_id="google", tenant_id="t", actor_id="a", operation=None)
        with self.assertRaisesRegex(ValueError, "INVALID_STORAGE_RESOURCE_ID"):
            build_plan(
                provider_id="google",
                tenant_id="t",
                actor_id="a",
                operation="LIST",
                resource_id=" ",
            )

    def test_lifecycle(self):
        self.assertTrue(
            transition("CONFIGURED", "CONNECTED")["requires_external_verification"]
        )
        with self.assertRaises(ValueError):
            transition("CATALOG_ONLY", "CONNECTED")


if __name__ == "__main__":
    unittest.main()
