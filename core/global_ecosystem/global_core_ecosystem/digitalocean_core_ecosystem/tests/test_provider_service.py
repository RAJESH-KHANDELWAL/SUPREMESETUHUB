import unittest
from .service import DigitalOceanCoreService
class ProviderTests(unittest.TestCase):
 def setUp(self): self.service=DigitalOceanCoreService()
 def test_unknown_capability(self):
  with self.assertRaises(ValueError): self.service.validate("unknown",{})
 def test_all_capabilities_route(self):
  for name in ("cloud","hosting","server","storage","vps"):
   self.assertEqual(self.service.validate(name,{"operation":"inspect"})["capability"],name)
 def test_live_execution_disabled(self):
  with self.assertRaisesRegex(RuntimeError,"LIVE_PROVIDER_CALLS_DISABLED"): self.service.execute()
if __name__=="__main__": unittest.main()
