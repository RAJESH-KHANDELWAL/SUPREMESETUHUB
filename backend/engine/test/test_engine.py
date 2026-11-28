"""Tests for the backend MAIN ENGINE only."""
import unittest

from backend.engine.base import BaseEngine
from backend.engine.manager import EngineManager


class MainEngineTests(unittest.TestCase):
    def test_base_engine_lifecycle(self):
        engine = BaseEngine("main")
        self.assertEqual(engine.status()["state"], "STOPPED")
        engine.load()
        self.assertEqual(engine.status()["state"], "LOADED")
        engine.start()
        self.assertEqual(engine.status()["state"], "RUNNING")
        engine.stop()
        self.assertEqual(engine.status()["state"], "STOPPED")

    def test_manager_register_and_lookup(self):
        manager = EngineManager()
        engine = BaseEngine("main")
        self.assertTrue(manager.register_engine("main", engine))
        self.assertIs(manager.get_engine("main"), engine)
        self.assertEqual(manager.list_engines(), ["main"])

    def test_manager_unregister(self):
        manager = EngineManager()
        manager.register_engine("main", BaseEngine("main"))
        self.assertTrue(manager.unregister_engine("main"))
        self.assertFalse(manager.unregister_engine("main"))
        self.assertIsNone(manager.get_engine("main"))


if __name__ == "__main__":
    unittest.main()
