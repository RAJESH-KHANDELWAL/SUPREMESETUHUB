"""Python tests for the Backend Foundation root."""
import unittest
from pathlib import Path

from backend.foundation.manager import get_manager


class BackendFoundationTests(unittest.TestCase):
    def test_foundation_manager_health(self):
        report = get_manager().health()
        self.assertTrue(report["healthy"], report)
        self.assertEqual(report["name"], "BACKEND FOUNDATION")
        self.assertEqual(
            set(report["checks"]),
            {"__init__.py", "manager.py", "manager.php", "global_ecosystem"},
        )

    def test_foundation_resolves_global_ecosystem_manager(self):
        manager = get_manager().get_global_ecosystem_manager()
        self.assertEqual(manager.NAME, "BACKEND GLOBAL ECOSYSTEM")
        self.assertTrue(manager.health()["healthy"])

    def test_foundation_php_bridge_exists(self):
        root = Path(__file__).resolve().parents[1] / "foundation"
        self.assertTrue((root / "manager.php").is_file())


if __name__ == "__main__":
    unittest.main()
