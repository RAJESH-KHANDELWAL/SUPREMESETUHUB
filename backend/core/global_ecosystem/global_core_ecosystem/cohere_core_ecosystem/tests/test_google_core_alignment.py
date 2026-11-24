"""Structural and behavior regression tests for Cohere Core's Google Core alignment."""
from __future__ import annotations

import unittest

from ..catalog import get_cohere_core_catalog, list_capabilities
from ..contracts import CapabilityRequest, TenantContext
from ..domain_catalog import DOMAIN_DEFINITIONS, domain_summary
from ..domain_runtime import CohereCoreDomainManager
from ..manager import CohereCoreManager, get_manager
from ..policy import CohereCorePolicyError
from ..service import CohereCoreService


class CohereGoogleCoreAlignmentTests(unittest.TestCase):
    def test_canonical_manager_and_entry_point(self):
        manager = get_manager()
        self.assertIsInstance(manager, CohereCoreManager)
        self.assertEqual(manager.ECOSYSTEM_ID, "COHERE-CORE-ECOSYSTEM")

    def test_five_capabilities_are_registered(self):
        self.assertEqual(set(list_capabilities()), {"classify", "command", "embed", "rerank", "tokenize"})
        self.assertEqual(len(get_cohere_core_catalog()["children"]), 5)

    def test_domain_inventory_covers_all_capabilities(self):
        summary = domain_summary()
        self.assertEqual(summary["domain_count"], 4)
        self.assertEqual(summary["unassigned_capabilities"], [])

    def test_domain_manager_rejects_unknown_domain(self):
        with self.assertRaises(KeyError):
            CohereCoreDomainManager("unknown")

    def test_domain_manager_exposes_readiness_only(self):
        result = CohereCoreDomainManager("text_generation").status()
        self.assertEqual(result["status"], "CORE_CATALOG_AVAILABLE")
        self.assertFalse(result["live_provider_calls_enabled"])

    def test_manager_discovery_and_dependency_map(self):
        manager = get_manager()
        self.assertEqual(manager.list_products()["count"], 5)
        self.assertEqual(len(manager.dependency_map()["edges"]), 5)

    def test_invalid_capability_is_rejected(self):
        result = CohereCoreService().validate(CapabilityRequest("unknown", {}))
        self.assertFalse(result.ok)

    def test_tenant_context_is_required_for_authorization(self):
        result = CohereCoreService().authorize_capability("embed", None)
        self.assertFalse(result["success"])

    def test_tenant_context_validation(self):
        with self.assertRaisesRegex(ValueError, "TENANT_ID_REQUIRED"):
            TenantContext("", "actor").validate()

    def test_provider_calls_remain_disabled(self):
        status = get_manager().status()
        self.assertFalse(status["live_provider_calls_enabled"])
        self.assertEqual(status["api_calls_performed"], 0)

    def test_package_names_follow_provider_core_convention(self):
        import pathlib
        root = pathlib.Path(__file__).resolve().parents[1]
        packages = [
            path.name for path in root.iterdir()
            if path.is_dir() and path.name.startswith("cohere_")
        ]
        self.assertTrue(packages)
        self.assertTrue(all(name.startswith("cohere_") and name.endswith("_core_ecosystem")
                            for name in packages if "_shared_" not in name))
