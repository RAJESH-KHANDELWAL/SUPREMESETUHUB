"""AWS Core inventory, package, policy and safe-boundary tests."""
import json
import unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.aws_core_ecosystem.catalog import get_aws_core_catalog
from backend.core.global_ecosystem.global_core_ecosystem.aws_core_ecosystem.contracts import AwsAccountContext, CredentialReference
from backend.core.global_ecosystem.global_core_ecosystem.aws_core_ecosystem.product_catalog import list_aws_offerings
from backend.core.global_ecosystem.global_core_ecosystem.aws_core_ecosystem.domain_catalog import aws_domain_summary
from backend.core.global_ecosystem.global_core_ecosystem.aws_core_ecosystem.service import AwsCoreEcosystemService

ROOT = Path(__file__).resolve().parents[1]
FAMILIES = ["aws_api_gateway_core_ecosystem","aws_bedrock_sagemaker_core_ecosystem","aws_billing_cost_core_ecosystem","aws_cloudformation_core_ecosystem","aws_cloudtrail_core_ecosystem","aws_cloudwatch_core_ecosystem","aws_containers_core_ecosystem","aws_database_core_ecosystem","aws_ec2_compute_core_ecosystem","aws_iam_sts_core_ecosystem","aws_kms_secrets_core_ecosystem","aws_lambda_core_ecosystem","aws_lightsail_core_ecosystem","aws_route53_dns_core_ecosystem","aws_s3_storage_core_ecosystem","aws_vpc_networking_core_ecosystem"]
STANDARD_DIRS = ["authentication", "capabilities", "docs", "events", "lifecycle", "models", "schemas", "security", "services", "tests"]

class TestAwsCoreCatalog(unittest.TestCase):
    def test_provider_inventory_and_safe_readiness(self):
        catalog = get_aws_core_catalog()
        self.assertEqual(catalog["provider"], "aws")
        self.assertEqual(len(catalog["children"]), 16)
        offerings = list_aws_offerings()
        self.assertEqual(len(offerings), 16)
        self.assertTrue(all(item["api_available"] is None for item in offerings))
        self.assertTrue(all(item["live_connection_verified"] is False for item in offerings))
        self.assertTrue(all(item["api_catalog_ref"].startswith("backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/") for item in offerings))

    def test_domain_coverage(self):
        summary = aws_domain_summary()
        self.assertEqual(summary["domain_count"], 13)
        self.assertEqual(summary["offering_count"], 16)
        self.assertEqual(summary["live_connections_verified"], 0)
        self.assertTrue(all(item["offering_count"] >= 1 for item in summary["domains"]))

    def test_google_style_package_structure_and_manifests(self):
        for family in FAMILIES:
            package = ROOT / family
            self.assertTrue(package.is_dir(), family)
            for folder in STANDARD_DIRS:
                self.assertTrue((package / folder).is_dir(), f"{family}/{folder}")
            manifest = json.loads((package / "ecosystem_manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["provider"], "aws")
            self.assertEqual(manifest["core_layer"], "AWS_CORE")
            self.assertFalse(manifest["live_connection_verified"])
            compile((package / "ecosystem_config.py").read_text(encoding="utf-8"), str(package / "ecosystem_config.py"), "exec")

    def test_account_context_validation(self):
        AwsAccountContext("123456789012", "ap-south-1", "tenant-1", "actor-1").validate()
        with self.assertRaises(ValueError):
            AwsAccountContext("123", "ap-south-1", "tenant-1", "actor-1").validate()

    def test_credential_reference_never_accepts_raw_secret_value_as_provider(self):
        with self.assertRaises(ValueError):
            CredentialReference("raw_access_key", "not-a-secret")

    def test_provider_service_reports_no_live_connections(self):
        status = AwsCoreEcosystemService().status()
        self.assertTrue(status["success"])
        self.assertEqual(status["module_count"], 16)
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["connected_modules"], 0)

if __name__ == "__main__":
    unittest.main()
