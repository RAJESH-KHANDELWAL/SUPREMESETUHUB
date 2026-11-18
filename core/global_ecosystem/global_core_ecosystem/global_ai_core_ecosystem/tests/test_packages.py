import json,unittest
from pathlib import Path
from ..catalog import list_ai_providers
class PackageCoverageTests(unittest.TestCase):
 def test_each_runtime_provider_has_core_package(self):
  root=Path(__file__).resolve().parents[1]
  for x in list_ai_providers():
   p=root/(x["id"]+"_core_ecosystem");self.assertTrue((p/"ecosystem_manifest.json").is_file(),x["id"])
   self.assertEqual(json.loads((p/"ecosystem_manifest.json").read_text())["provider_id"],x["id"])
 def test_google_folder_standard(self):
  root=Path(__file__).resolve().parents[1];expected={"authentication","capabilities","docs","events","lifecycle","models","schemas","security","services","tests"}
  for x in list_ai_providers():
   p=root/(x["id"]+"_core_ecosystem");actual={z.name for z in p.iterdir() if z.is_dir() and z.name!="__pycache__"}
   self.assertEqual(actual,expected,x["id"])
if __name__=="__main__":unittest.main()
