"""Offline tests for the APP engine lifecycle adapter."""
import unittest

from backend.engine.app.manager import AppEngine


class AppEngineTests(unittest.TestCase):
    def test_engine_starts_and_stops_app_lifecycle(self):
        engine = AppEngine()

        started = engine.start()
        self.assertEqual(started["state"], "RUNNING")
        self.assertEqual(started["app_lifecycle"]["state"], "RUNNING")

        stopped = engine.stop()
        self.assertEqual(stopped["state"], "STOPPED")
        self.assertEqual(stopped["app_lifecycle"]["state"], "STOPPED")

    def test_component_inventory_is_delegated_to_app_layer(self):
        engine = AppEngine()
        self.assertEqual(engine.list_components(), [])

    def test_execution_is_explicit_only(self):
        engine = AppEngine()
        self.assertEqual(engine.status()["execution"], "EXPLICIT_ONLY")


if __name__ == "__main__":
    unittest.main()
