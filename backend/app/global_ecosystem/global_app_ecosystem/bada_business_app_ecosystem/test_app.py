"""Unit tests for the Bada Business APP composition foundation."""
import unittest
from .lifecycle import AppState, BadaBusinessAppLifecycle, InvalidAppTransition
from .manager import BadaBusinessAppManager

class TestBadaBusinessApp(unittest.TestCase):
    def test_initialize_registers_six_modules(self):
        manager = BadaBusinessAppManager()
        status = manager.initialize()
        self.assertEqual(status["state"], AppState.READY.value)
        self.assertEqual(len(status["registered_components"]), 6)

    def test_initialize_is_idempotent(self):
        manager = BadaBusinessAppManager()
        first = manager.initialize()
        second = manager.initialize()
        self.assertEqual(first, second)

    def test_dependencies_are_injected_not_imported(self):
        api, ai = object(), object()
        manager = BadaBusinessAppManager(api_service=api, ai_service=ai)
        manager.initialize()
        status = manager.status()
        self.assertTrue(status["api_injected"])
        self.assertTrue(status["ai_injected"])

    def test_lifecycle_rejects_invalid_transition(self):
        lifecycle = BadaBusinessAppLifecycle()
        with self.assertRaises(InvalidAppTransition):
            lifecycle.transition(AppState.READY)

    def test_diagnostics_report_uninjected_dependencies(self):
        manager = BadaBusinessAppManager()
        checks = manager.diagnostics()["checks"]
        self.assertEqual(checks["api_interface"], "not_injected")
        self.assertEqual(checks["ai_interface"], "not_injected")

if __name__ == "__main__":
    unittest.main()
