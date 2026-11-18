import unittest
from ..catalog import list_ai_providers,validate_provider_registry
from ..domain_catalog import ai_domain_summary
from ..ecosystem_service import GlobalAICoreEcosystemService
from ..request_contracts import validate_ai_request
from ..service import GlobalAICoreService
class GlobalAICoreTests(unittest.TestCase):
 def test_registry_integrity(self):self.assertGreaterEqual(len(list_ai_providers()),68);self.assertEqual(validate_provider_registry(),())
 def test_domain_coverage(self):self.assertEqual(ai_domain_summary()["provider_count"],len(list_ai_providers()))
 def test_secret_rejection(self):
  with self.assertRaises(ValueError):validate_ai_request({"context":{"api_key":"x"}})
 def test_request_not_execution(self):
  x=validate_ai_request({"provider_id":"openai_chatgpt","capability":"text","task":"hello"});self.assertTrue(x["accepted"]);self.assertFalse(x["execution_performed"])
 def test_status_no_live_claim(self):
  x=GlobalAICoreEcosystemService().status();self.assertFalse(x["live_connection_verified"]);self.assertEqual(x["api_calls_performed"],0)
 def test_injected_executor(self):
  x=GlobalAICoreService(lambda **kw:{"output":"ok","live_verified":False});self.assertEqual(x.generate(task="hello")["output"],"ok")
if __name__=="__main__":unittest.main()
