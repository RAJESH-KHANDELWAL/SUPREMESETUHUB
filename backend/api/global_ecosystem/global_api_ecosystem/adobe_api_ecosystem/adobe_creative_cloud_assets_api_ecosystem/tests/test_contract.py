"""Offline contract checks; no Adobe credentials or network calls required."""
import json
import unittest
from pathlib import Path

class ApiContractTests(unittest.TestCase):
    def test_contract_is_explicitly_unverified(self):
        contract = json.loads((Path(__file__).parents[1] / "api_contract.json").read_text(encoding="utf-8"))
        self.assertEqual(contract["provider"], "adobe")
        self.assertEqual(contract["status"], "ADAPTER_SCAFFOLD")
        self.assertFalse(contract["live_connection_verified"])
        self.assertFalse(contract["entitlement_verified"])
        self.assertEqual(contract["endpoint_catalog"], [])

if __name__ == "__main__":
    unittest.main()
