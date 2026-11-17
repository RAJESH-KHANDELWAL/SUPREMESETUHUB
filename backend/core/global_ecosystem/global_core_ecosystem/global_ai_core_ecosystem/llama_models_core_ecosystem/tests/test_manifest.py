import json,unittest
from pathlib import Path
class ManifestTests(unittest.TestCase):
 def test_identity(self):
  x=json.loads((Path(__file__).resolve().parents[1]/"ecosystem_manifest.json").read_text())
  self.assertEqual(x["provider_id"],"llama_models");self.assertEqual(x["parent_id"],"GLOBAL-AI-CORE-ECOSYSTEM");self.assertFalse(x["live_connection_verified"])
if __name__=="__main__":unittest.main()
