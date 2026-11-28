"""Structural contract tests for the 29 Global Developer Core provider packages."""
import json
import unittest
from pathlib import Path

ROOT = (Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" /
        "global_core_ecosystem" / "global_developer_core_ecosystem")
PROVIDERS = [
    "adult_creator_business",
    "adult_platform_discovery",
    "age_verification_consent",
    "ai_ml_data",
    "anthropic_developer",
    "apple_developer",
    "atlassian_developer",
    "aws_developer",
    "blockchain_web3",
    "cohere_developer",
    "content_moderation_safety",
    "database_storage",
    "dating_relationships",
    "deepseek_developer",
    "developer_security_compliance",
    "github_developer",
    "global_cloud_infrastructure",
    "google_developer",
    "huggingface_developer",
    "identity_authentication",
    "india_developer_platform",
    "microsoft_developer",
    "mistral_developer",
    "no_code_automation",
    "nvidia_developer",
    "openai_developer",
    "payments_billing",
    "sexual_wellness_education",
    "testing_observability"
]
STANDARD_FOLDERS = {
    "authentication", "capabilities", "docs", "events", "lifecycle",
    "models", "schemas", "security", "services", "tests",
}

class GlobalDeveloperCorePackageTests(unittest.TestCase):
    def test_all_provider_packages_have_standard_metadata_and_folders(self):
        self.assertEqual(len(PROVIDERS), 29)
        self.assertEqual(len(set(PROVIDERS)), 29)
        for provider_id in PROVIDERS:
            with self.subTest(provider=provider_id):
                package = ROOT / f"{provider_id}_core_ecosystem"
                self.assertTrue((package / "README.md").is_file())
                self.assertTrue((package / "__init__.py").is_file())
                self.assertTrue((package / "contracts.py").is_file())
                self.assertTrue((package / "ecosystem_config.py").is_file())
                manifest_path = package / "ecosystem_manifest.json"
                self.assertTrue(manifest_path.is_file())
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                self.assertEqual(manifest["provider_id"], provider_id)
                self.assertEqual(set(manifest["folders"]), STANDARD_FOLDERS)
                self.assertEqual(manifest["status"], "CORE_CATALOG_ONLY")
                self.assertFalse(manifest["connected"])
                self.assertFalse(manifest["live_connection_verified"])
                for folder in STANDARD_FOLDERS:
                    self.assertTrue((package / folder / "README.md").is_file(),
                                    f"{provider_id}/{folder}")
                self.assertTrue((package / "authentication" / "contract.php").is_file())

if __name__ == "__main__":
    unittest.main()
