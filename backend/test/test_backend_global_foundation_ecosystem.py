"""Python tests for Backend Global Foundation Ecosystem."""
import unittest

from backend.foundation.global_ecosystem.manager import get_manager as get_global_manager
from backend.foundation.global_ecosystem.global_foundation_ecosystem import (
    GlobalFoundationEcosystemManager,
    get_manager,
)


class BackendGlobalFoundationEcosystemTests(unittest.TestCase):
    def test_global_ecosystem_resolves_foundation_manager(self):
        manager = get_global_manager().get_global_foundation_manager()
        self.assertIsInstance(manager, GlobalFoundationEcosystemManager)

    def test_global_foundation_manager_health(self):
        report = get_manager().health()
        self.assertTrue(report["healthy"], report)
        self.assertEqual(report["name"], "BACKEND GLOBAL FOUNDATION ECOSYSTEM")
        self.assertEqual(report["expected_domain_count"], 12)
        self.assertEqual(report["present_domain_count"], 12)

    def test_global_foundation_php_bridge_exists(self):
        from pathlib import Path
        package = Path(__file__).resolve().parents[1] / "foundation" / "global_ecosystem" / "global_foundation_ecosystem"
        self.assertTrue((package / "manager.php").is_file())


if __name__ == "__main__":
    unittest.main()
