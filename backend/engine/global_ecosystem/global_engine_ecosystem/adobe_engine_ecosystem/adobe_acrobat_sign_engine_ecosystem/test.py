"""Offline checks for the Adobe Acrobat Sign ENGINE boundary.

These tests do not contact Adobe or require credentials.
"""
import unittest

from .engine import ProviderEngine


class ProviderEngineTests(unittest.TestCase):
    def test_engine_reports_unconfigured_without_a_handler(self):
        engine = ProviderEngine()
        self.assertEqual(engine.health()["layer"], "ENGINE")
        self.assertEqual(engine.health()["status"], "NOT_CONFIGURED")

    def test_engine_executes_only_through_an_injected_handler(self):
        engine = ProviderEngine(
            handler=lambda operation, payload: {
                "operation": operation,
                "payload": payload,
            }
        )
        result = engine.execute("self-test", {"ok": True})
        self.assertEqual(result, {
            "operation": "self-test",
            "payload": {"ok": True},
        })
        self.assertEqual(engine.health()["status"], "READY")

    def test_engine_does_not_claim_live_provider_connection(self):
        engine = ProviderEngine()
        self.assertEqual(engine.health()["status"], "NOT_CONFIGURED")


if __name__ == "__main__":
    unittest.main()
