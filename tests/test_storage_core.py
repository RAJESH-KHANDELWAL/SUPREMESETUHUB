import unittest
from ..catalog import get_provider,list_providers
from ..domain_catalog import list_domains
from ..lifecycle import transition
from ..orchestrator import build_plan
from ..policy import validate_resource_metadata
class StorageCoreTests(unittest.TestCase):
 def test_inventory(self): self.assertEqual({x["provider_id"] for x in list_providers()},{"apple","aws","digitalocean","google","microsoft"})
 def test_domains(self): self.assertIn("OBJECT_STORAGE",list_domains()); self.assertIn("BACKUP",list_domains())
 def test_rejects_bytes(self):
  with self.assertRaisesRegex(ValueError,"SENSITIVE_PAYLOAD_NOT_ALLOWED"): validate_resource_metadata({"tenant_id":"t","resource_id":"r","provider_id":"aws","resource_type":"object","file_bytes":"x"})
 def test_accepts_metadata(self): self.assertTrue(validate_resource_metadata({"tenant_id":"t","resource_id":"r","provider_id":"aws","resource_type":"object"})["metadata_only"])
 def test_plan_only(self):
  x=build_plan(provider_id="google",tenant_id="t",actor_id="a",operation="UPLOAD"); self.assertTrue(x["plan_only"]); self.assertFalse(x["data_transferred"])
 def test_lifecycle(self):
  self.assertTrue(transition("CONFIGURED","CONNECTED")["requires_external_verification"])
  with self.assertRaises(ValueError): transition("CATALOG_ONLY","CONNECTED")
if __name__=="__main__": unittest.main()
