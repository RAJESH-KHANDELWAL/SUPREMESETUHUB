import unittest
from ..catalog import AI_PROVIDERS,ADJACENT_INTEGRATIONS
from ..ecosystem_service import GlobalAICoreEcosystemService
from ..request_contracts import validate_ai_request
from ..service import GlobalAICoreService
class RegistryTests(unittest.TestCase):
 def test_provider_and_partner_separation(self):
  self.assertEqual(len(AI_PROVIDERS),17); self.assertEqual(len(ADJACENT_INTEGRATIONS),24)
  self.assertTrue(all(x["is_ai_model_provider"] is False for x in ADJACENT_INTEGRATIONS))
 def test_secret_rejected(self):
  with self.assertRaises(ValueError): validate_ai_request({"context":{"api_key":"x"}})
 def test_request_validation_is_not_execution(self):
  x=validate_ai_request({"provider_id":"openai","capability":"text_generation","task":"hello"})
  self.assertTrue(x["accepted"]); self.assertFalse(x["execution_performed"])
 def test_registry_status_no_live_claim(self):
  x=GlobalAICoreEcosystemService().status()
  self.assertFalse(x["runtime_execution_enabled"]); self.assertFalse(x["live_provider_connections_verified"])
 def test_existing_injected_executor_preserved(self):
  x=GlobalAICoreService(lambda **kw:{"output":"ok","live_verified":False})
  self.assertEqual(x.generate(task="hello")["output"],"ok")
if __name__=="__main__": unittest.main()
