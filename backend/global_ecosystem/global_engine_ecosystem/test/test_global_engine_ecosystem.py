"""Tests for the independent People, Work, and Business Global Engine."""
import unittest

from backend.global_ecosystem.global_engine_ecosystem.manager import (
    EcosystemIdentity,
    ROOT_ID,
    SUPPORTED_DOMAINS,
)
from backend.global_ecosystem.global_engine_ecosystem.registry import (
    GlobalEcosystemRegistry,
)


class GlobalEngineEcosystemTests(unittest.TestCase):
    def test_registry_register_and_retrieve(self):
        registry = GlobalEcosystemRegistry()
        item = EcosystemIdentity(ecosystem_id="test-person", name="Test Person")
        registered = registry.register(item)
        self.assertEqual(registered["ecosystem_id"], "test-person")
        self.assertEqual(registry.get("test-person")["name"], "Test Person")
        self.assertEqual(registry.count(), 1)

    def test_people_work_and_business_domains_are_supported(self):
        registry = GlobalEcosystemRegistry()
        for domain in SUPPORTED_DOMAINS:
            registry.register(EcosystemIdentity(
                ecosystem_id=domain.lower(), name=domain.title(), ecosystem_type=domain
            ))
        self.assertEqual(registry.count(), 3)
        self.assertEqual(registry.count("WORK"), 1)
        self.assertEqual(registry.get(ROOT_ID)["capabilities"], list(SUPPORTED_DOMAINS))

    def test_parent_relationship_validation(self):
        registry = GlobalEcosystemRegistry()
        with self.assertRaises(ValueError):
            registry.register(EcosystemIdentity(
                ecosystem_id="child", name="Child", parent_id="missing-parent"
            ))

    def test_self_parent_rejected(self):
        registry = GlobalEcosystemRegistry()
        with self.assertRaises(ValueError):
            registry.register(EcosystemIdentity(
                ecosystem_id="self", name="Self", parent_id="self"
            ))

    def test_unsupported_domain_rejected(self):
        registry = GlobalEcosystemRegistry()
        with self.assertRaises(ValueError):
            registry.register(EcosystemIdentity(
                ecosystem_id="unknown", name="Unknown", ecosystem_type="UNKNOWN"
            ))

    def test_root_identifier_constant(self):
        self.assertEqual(ROOT_ID, "GLOBAL-ENGINE-ECOSYSTEM")


if __name__ == "__main__":
    unittest.main()
