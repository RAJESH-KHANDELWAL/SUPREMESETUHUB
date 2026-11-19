"""Tests for the eight Foundation ecosystem adapter integrations."""

import unittest

from backend.foundation.audit.global_ecosystem.global_audit_ecosystem import GlobalAuditEcosystemManager
from backend.foundation.core.global_ecosystem.global_core_ecosystem import GlobalCoreEcosystemManager
from backend.foundation.dependencies.global_ecosystem.global_dependencies_ecosystem import GlobalDependenciesEcosystemManager
from backend.foundation.file_manager.global_ecosystem.global_file_manager_ecosystem import GlobalFileManagerEcosystemManager
from backend.foundation.identity.global_ecosystem.global_identity_ecosystem import GlobalIdentityEcosystemManager
from backend.foundation.registry.global_ecosystem.global_registry_ecosystem import GlobalRegistryEcosystemManager
from backend.foundation.security.global_ecosystem.global_security_ecosystem import GlobalSecurityEcosystemManager
from backend.foundation.sync.global_ecosystem.global_sync_ecosystem import GlobalSyncEcosystemManager


class SampleFoundationComponent:
    def ping(self):
        return "PONG"


class FoundationEcosystemIntegrationTests(unittest.TestCase):
    def test_all_ecosystem_managers_wrap_and_delegate_to_original_component(self):
        cases = (
            (GlobalAuditEcosystemManager, "audit"),
            (GlobalCoreEcosystemManager, "core"),
            (GlobalDependenciesEcosystemManager, "dependencies"),
            (GlobalFileManagerEcosystemManager, "file_manager"),
            (GlobalIdentityEcosystemManager, "identity"),
            (GlobalRegistryEcosystemManager, "registry"),
            (GlobalSecurityEcosystemManager, "security"),
            (GlobalSyncEcosystemManager, "sync"),
        )

        for manager_class, component_key in cases:
            with self.subTest(ecosystem=manager_class.NAME):
                original_component = SampleFoundationComponent()
                manager = manager_class(original_component)

                self.assertIs(manager.get_component(), original_component)
                self.assertEqual(manager.ping(), "PONG")
                result = manager.status()
                self.assertEqual(result["status"], "INTEGRATED")
                self.assertEqual(result["ecosystem"], manager_class.NAME)
                self.assertEqual(result["component_key"], component_key)
                self.assertEqual(
                    result["component_type"],
                    "SampleFoundationComponent",
                )

    def test_manager_rejects_missing_component(self):
        for manager_class in (
            GlobalAuditEcosystemManager,
            GlobalCoreEcosystemManager,
            GlobalDependenciesEcosystemManager,
            GlobalFileManagerEcosystemManager,
            GlobalIdentityEcosystemManager,
            GlobalRegistryEcosystemManager,
            GlobalSecurityEcosystemManager,
            GlobalSyncEcosystemManager,
        ):
            with self.subTest(ecosystem=manager_class.NAME):
                with self.assertRaisesRegex(
                    ValueError,
                    "Foundation component is required",
                ):
                    manager_class(None)


if __name__ == "__main__":
    unittest.main()
