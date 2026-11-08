"""Tests for the GLOBAL SERVER ENGINE provider boundaries."""
import unittest
from .engine import ProviderEngine
from .manager import EcosystemEngineManager
from .provider_catalog import list_providers, get_provider
from .aws_server_engine_ecosystem.engine import ProviderEngine as Aws
from .google_server_engine_ecosystem.engine import ProviderEngine as Google
from .microsoft_server_engine_ecosystem.engine import ProviderEngine as Microsoft
from .cloudflare_server_engine_ecosystem.engine import ProviderEngine as Cloudflare
from .digitalocean_server_engine_ecosystem.engine import ProviderEngine as DigitalOcean
from .abelohost_server_engine_ecosystem.engine import ProviderEngine as Abelohost
from .vicetemple_server_engine_ecosystem.engine import ProviderEngine as Vicetemple

class TestGlobalServerEngine(unittest.TestCase):
    def test_provider_catalog(self):
        items=list_providers()
        ids=[x["provider_id"] for x in items]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(get_provider("AWS")["provider_id"],"aws")
        with self.assertRaises(KeyError): get_provider("missing")

    def test_all_adapters_are_unconfigured_without_handler(self):
        for cls in (ProviderEngine,Aws,Google,Microsoft,Cloudflare,DigitalOcean,Abelohost,Vicetemple):
            self.assertEqual(cls().health()["status"],"NOT_CONFIGURED")

    def test_handler_is_injected_and_payload_is_copied(self):
        seen={}
        def handler(op,payload):
            seen.update(op=op,payload=payload)
            return {"ok":True}
        instance=Aws(handler)
        body={"region":"ap-south-1"}
        self.assertEqual(instance.execute("create",body),{"ok":True})
        body["region"]="changed"
        self.assertEqual(seen["payload"]["region"],"ap-south-1")

    def test_registry_manager_lifecycle(self):
        manager=EcosystemEngineManager()
        item=object()
        manager.register("compute",item)
        self.assertIs(manager.get("compute"),item)
        self.assertTrue(manager.unregister("compute"))
        self.assertIsNone(manager.get("compute"))

if __name__=="__main__": unittest.main()
