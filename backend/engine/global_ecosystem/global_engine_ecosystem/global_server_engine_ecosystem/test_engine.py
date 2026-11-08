"""Offline tests for GLOBAL SERVER ENGINE boundary."""
import unittest
from .engine import ProviderEngine
from .manager import EcosystemEngineManager
from .provider_catalog import list_providers, get_provider
from .aws_server_engine_ecosystem.engine import ProviderEngine as AwsEngine
from .google_server_engine_ecosystem.engine import ProviderEngine as GoogleEngine
from .microsoft_server_engine_ecosystem.engine import ProviderEngine as MicrosoftEngine
from .cloudflare_server_engine_ecosystem.engine import ProviderEngine as CloudflareEngine
from .digitalocean_server_engine_ecosystem.engine import ProviderEngine as DigitalOceanEngine
from .abelohost_server_engine_ecosystem.engine import ProviderEngine as AbelohostEngine
from .vicetemple_server_engine_ecosystem.engine import ProviderEngine as VicetempleEngine

class GlobalServerEngineTests(unittest.TestCase):
    def test_default_engine_does_not_claim_provider_connection(self):
        engine=ProviderEngine()
        self.assertEqual(engine.health()["status"],"NOT_CONFIGURED")
        with self.assertRaises(NotImplementedError): engine.execute("provision")

    def test_handler_receives_operation_and_payload_copy(self):
        seen={}
        def handler(operation,payload):
            seen.update(operation=operation,payload=payload)
            return {"accepted":True}
        engine=ProviderEngine(handler)
        body={"region":"ap-south-1"}
        self.assertEqual(engine.execute("create",body),{"accepted":True})
        body["region"]="tampered"
        self.assertEqual(seen["payload"]["region"],"ap-south-1")
        with self.assertRaises(ValueError): engine.execute(" ")

    def test_provider_catalog_unique_and_lookup(self):
        items=list_providers()
        ids=[x["provider_id"] for x in items]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertGreaterEqual(len(items),7)
        self.assertEqual(get_provider("AWS")["provider_id"],"aws")
        with self.assertRaises(KeyError): get_provider("not-real")

    def test_provider_adapters_are_distinct_boundaries(self):
        for adapter in (AwsEngine,GoogleEngine,MicrosoftEngine,CloudflareEngine,
                        DigitalOceanEngine,AbelohostEngine,VicetempleEngine):
            self.assertEqual(adapter().health()["status"],"NOT_CONFIGURED")

    def test_registry_lifecycle(self):
        manager=EcosystemEngineManager()
        marker=object()
        manager.register("server",marker)
        self.assertIs(manager.get("server"),marker)
        self.assertTrue(manager.unregister("server"))
        self.assertIsNone(manager.get("server"))
        self.assertEqual(manager.status()["layer"],"ENGINE")

if __name__=="__main__": unittest.main()
