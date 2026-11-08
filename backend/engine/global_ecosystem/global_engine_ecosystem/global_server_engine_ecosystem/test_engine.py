"""Offline tests for GLOBAL SERVER ENGINE boundary."""
import unittest
from .engine import ProviderEngine
from .manager import EcosystemEngineManager
from .provider_catalog import list_providers, get_provider

class GlobalServerEngineTests(unittest.TestCase):
    def test_handler_is_required_before_execute(self):
        engine=ProviderEngine()
        self.assertEqual(engine.health()["status"], "NOT_CONFIGURED")
        with self.assertRaises(NotImplementedError): engine.execute("provision")

    def test_handler_receives_copy_of_payload(self):
        seen={}
        def handler(operation,payload):
            seen.update(operation=operation,payload=payload)
            return {"accepted":True}
        engine=ProviderEngine(handler)
        body={"region":"ap-south-1"}
        self.assertEqual(engine.execute("create",body),{"accepted":True})
        body["region"]="tampered"
        self.assertEqual(seen["payload"]["region"],"ap-south-1")

    def test_provider_catalog_is_unique_and_resolvable(self):
        items=list_providers()
        self.assertGreaterEqual(len(items),7)
        ids=[x["provider_id"] for x in items]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(get_provider("AWS")["provider_id"],"aws")
        with self.assertRaises(KeyError): get_provider("not-real")

    def test_manager_registry_lifecycle(self):
        manager=EcosystemEngineManager()
        marker=object()
        manager.register("server",marker)
        self.assertIs(manager.get("server"),marker)
        self.assertTrue(manager.unregister("server"))
        self.assertIsNone(manager.get("server"))
        self.assertEqual(manager.status()["layer"],"ENGINE")

if __name__=="__main__": unittest.main()
