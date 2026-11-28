"""Tests for SECOND GLOBAL ENGINE ECOSYSTEM (kept separate from MAIN ENGINE)."""
import unittest

# Transitional import: implementation remains in its legacy nested path for now.
from backend.engine.global_ecosystem.global_engine_ecosystem.manager import (
    EcosystemIdentity,
    ROOT_ID,
)
from backend.engine.global_ecosystem.global_engine_ecosystem.registry import (
    GlobalEcosystemRegistry,
)


class GlobalEngineEcosystemTests(unittest.TestCase):
    def test_registry_register_and_retrieve(self):
        registry = GlobalEcosystemRegistry()
        item = EcosystemIdentity(ecosystem_id="test-child", name="Test Child")
        registered = registry.register(item)
        self.assertEqual(registered["ecosystem_id"], "test-child")
        self.assertEqual(registry.get("test-child")["name"], "Test Child")
        self.assertEqual(registry.count(), 1)

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

    def test_root_identifier_constant(self):
        self.assertEqual(ROOT_ID, "GLOBAL-ENGINE-ECOSYSTEM")


if __name__ == "__main__":
    unittest.main()
