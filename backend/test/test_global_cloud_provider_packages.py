"""Validate the 25 Cloud Core provider scaffolds against the runtime registry."""
from __future__ import annotations
import unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.global_cloud_core_ecosystem.manager import GlobalCloudCoreManager

ROOT = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem" / "global_cloud_core_ecosystem"
PROVIDER_IDS = ["aws_india","azure_india","box","ctrls","digiboxx","dropbox","e2e_networks","esds","gcp_india","google_drive","icloud","idrive","jio_cloud","linode","mega","netlify","nxtgen","onedrive","oracle_cloud_india","pcloud","proton_drive","render","tata_communications_cloud","vercel","yotta"]
FOLDERS = {"authentication", "capabilities", "docs", "events", "lifecycle", "models", "schemas", "security", "services", "tests"}

class GlobalCloudProviderPackageTests(unittest.TestCase):
    def test_scaffolds_match_canonical_runtime_provider_ids(self):
        manager = GlobalCloudCoreManager()
        self.assertEqual(len(PROVIDER_IDS), 25)
        self.assertEqual(len(set(PROVIDER_IDS)), 25)
        for provider_id in PROVIDER_IDS:
            with self.subTest(provider=provider_id):
                self.assertIsNotNone(manager.get_product(provider_id))
                package = ROOT / f"{provider_id}_cloud_core_ecosystem"
                self.assertTrue((package / "README.md").is_file())
                self.assertTrue((package / "__init__.py").is_file())
                for folder in FOLDERS:
                    self.assertTrue((package / folder).is_dir(), f"{provider_id}/{folder}")
                init_source = (package / "__init__.py").read_text(encoding="utf-8")
                self.assertIn('IMPLEMENTATION_STATUS = "scaffold_only"', init_source)

if __name__ == "__main__":
    unittest.main()
