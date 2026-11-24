"""Catalog, lifecycle and policy contract tests."""
import unittest

from ...catalog import get_cohere_core_catalog, list_capabilities
from ...contracts import CapabilityRequest, SecretReference, TenantContext
from ...manager import CohereCoreManager
from ...policy import ensure_operation_allowed
from ...cohere_shared_security.policy import assert_no_secret_fields


class CohereCatalogAndPolicyTests(unittest.TestCase):
    def test_exactly_five_capabilities_are_registered(self):
        self.assertEqual(
            set(list_capabilities()),
            {"classify", "command", "embed", "rerank", "tokenize"},
        )

    def test_catalog_returns_defensive_copy(self):
        first = get_cohere_core_catalog()
        first["children"].clear()
        self.assertEqual(len(get_cohere_core_catalog()["children"]), 5)

    def test_tenant_context_and_secret_reference_validate(self):
        TenantContext("tenant-1", "actor-1").validate()
        SecretReference("cohere", "secret-manager://cohere/key")
        with self.assertRaises(ValueError):
            TenantContext("", "actor-1").validate()

    def test_secret_fields_are_rejected_recursively(self):
        with self.assertRaises(ValueError):
            assert_no_secret_fields({"history": [{"api_key": "never-store"}]})

    def test_sensitive_operations_require_authorization(self):
        with self.assertRaises(PermissionError):
            ensure_operation_allowed("delete_connector")
        with self.assertRaises(PermissionError):
            ensure_operation_allowed("delete_model", explicitly_authorized=True)

    def test_manager_public_facade(self):
        manager = CohereCoreManager()
        result = manager.validate(CapabilityRequest("tokenize", {"text": "hello"}))
        self.assertTrue(result.ok)


if __name__ == "__main__":
    unittest.main()
