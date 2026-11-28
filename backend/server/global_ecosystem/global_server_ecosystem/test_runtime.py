"""Offline tests for safe SERVER runtime diagnostics."""
import unittest
from unittest.mock import patch

from backend.server.global_ecosystem.global_server_ecosystem.runtime import runtime_status


class ServerRuntimeTests(unittest.TestCase):
    def test_runtime_status_contains_safe_process_metadata(self):
        result = runtime_status()
        self.assertEqual(result["service"], "MAIN BASE FOUNDATION SERVER")
        self.assertEqual(result["status"], "PROCESS_RUNNING")
        self.assertIn("hostname", result)
        self.assertIn("process_id", result)
        self.assertGreaterEqual(result["uptime_seconds"], 0)
        self.assertNotIn("SUPREME_CONTROL_TOKEN", result)

    def test_invalid_port_is_reported_without_crashing(self):
        with patch.dict("os.environ", {"PORT": "not-a-port"}):
            self.assertIsNone(runtime_status()["port"])


if __name__ == "__main__":
    unittest.main()
