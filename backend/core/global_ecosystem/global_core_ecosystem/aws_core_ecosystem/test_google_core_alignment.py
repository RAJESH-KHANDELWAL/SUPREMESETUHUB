"""Google Core structural and behavior alignment tests for AWS Core."""
from __future__ import annotations
import importlib,re
from pathlib import Path
from .domain_catalog import DOMAIN_DEFINITIONS,aws_domain_summary
from .domain_runtime import AwsCoreDomainManager
DOMAIN_PACKAGES={
 "APPLICATION_INTEGRATION_AND_API_MANAGEMENT":"aws_application_integration_and_api_management_core_ecosystem",
 "AI_ML_AND_INTELLIGENCE":"aws_ai_ml_and_intelligence_core_ecosystem",
 "BILLING_COST_AND_GOVERNANCE":"aws_billing_cost_and_governance_core_ecosystem",
 "COMPUTE_AND_CONTAINERS":"aws_compute_and_containers_core_ecosystem",
 "DATABASE_AND_DATA_SERVICES":"aws_database_and_data_services_core_ecosystem",
 "DOMAIN_AND_NAME_SERVICES":"aws_domain_and_name_services_core_ecosystem",
 "INFRASTRUCTURE_PROVISIONING_AND_AUTOMATION":"aws_infrastructure_provisioning_and_automation_core_ecosystem",
 "NETWORKING_AND_EDGE":"aws_networking_and_edge_core_ecosystem",
 "OBSERVABILITY_AND_AUDIT":"aws_observability_and_audit_core_ecosystem",
 "ORGANIZATION_AND_GOVERNANCE":"aws_organization_and_governance_core_ecosystem",
 "SECURITY_AND_IDENTITY":"aws_security_and_identity_core_ecosystem",
 "STORAGE_AND_DATA_MANAGEMENT":"aws_storage_and_data_management_core_ecosystem",
 "DEVELOPER_AND_APPLICATION_PLATFORM":"aws_developer_and_application_platform_core_ecosystem",
}
PRODUCT_PACKAGES={
 "AWS-API-GATEWAY-CORE-ECOSYSTEM":"aws_api_gateway_core_ecosystem",
 "AWS-BEDROCK-SAGEMAKER-CORE-ECOSYSTEM":"aws_bedrock_sagemaker_core_ecosystem",
 "AWS-BILLING-COST-CORE-ECOSYSTEM":"aws_billing_cost_core_ecosystem",
 "AWS-CLOUDFORMATION-CORE-ECOSYSTEM":"aws_cloudformation_core_ecosystem",
 "AWS-CLOUDTRAIL-CORE-ECOSYSTEM":"aws_cloudtrail_core_ecosystem",
 "AWS-CLOUDWATCH-CORE-ECOSYSTEM":"aws_cloudwatch_core_ecosystem",
 "AWS-CONTAINERS-CORE-ECOSYSTEM":"aws_containers_core_ecosystem",
 "AWS-DATABASE-CORE-ECOSYSTEM":"aws_database_core_ecosystem",
 "AWS-EC2-COMPUTE-CORE-ECOSYSTEM":"aws_ec2_compute_core_ecosystem",
 "AWS-IAM-STS-CORE-ECOSYSTEM":"aws_iam_sts_core_ecosystem",
 "AWS-KMS-SECRETS-CORE-ECOSYSTEM":"aws_kms_secrets_core_ecosystem",
 "AWS-LAMBDA-CORE-ECOSYSTEM":"aws_lambda_core_ecosystem",
 "AWS-LIGHTSAIL-CORE-ECOSYSTEM":"aws_lightsail_core_ecosystem",
 "AWS-ROUTE53-DNS-CORE-ECOSYSTEM":"aws_route53_dns_core_ecosystem",
 "AWS-S3-STORAGE-CORE-ECOSYSTEM":"aws_s3_storage_core_ecosystem",
 "AWS-VPC-NETWORKING-CORE-ECOSYSTEM":"aws_vpc_networking_core_ecosystem",
}
def test_all_thirteen_domain_packages_are_registered():
 assert len(DOMAIN_DEFINITIONS)==13 and set(DOMAIN_PACKAGES)==set(DOMAIN_DEFINITIONS)
def test_each_domain_package_exports_working_manager():
 root="backend.core.global_ecosystem.global_core_ecosystem.aws_core_ecosystem"
 for domain_id,name in DOMAIN_PACKAGES.items():
  package=importlib.import_module(f"{root}.{name}"); manager=package.get_manager()
  assert manager.DOMAIN_ID==domain_id and manager.status()["domain_id"]==domain_id and manager.list_offerings()["success"]
def test_domain_inventory_matches_canonical_offerings():
 summary=aws_domain_summary(); assert summary["domain_count"]==13 and summary["offering_count"]==16
 for item in summary["domains"]: assert AwsCoreDomainManager(item["domain_id"]).list_offerings()["count"]==item["offering_count"]
def test_all_sixteen_family_managers_delegate_to_existing_services():
 root="backend.core.global_ecosystem.global_core_ecosystem.aws_core_ecosystem"
 for ecosystem_id,name in PRODUCT_PACKAGES.items():
  manager=importlib.import_module(f"{root}.{name}").get_manager()
  assert manager.status()["ecosystem_id"]==ecosystem_id and manager.capabilities()["ecosystem_id"]==ecosystem_id
def test_canonical_manager_contract():
 from .manager import get_manager
 manager=get_manager(); assert manager.status()["success"]
 assert manager.health()["product_family_count"]==16 and manager.list_domains()["domain_count"]==13
 assert manager.list_products()["count"]==16 and manager.list_offerings()["count"]==16
def test_aws_package_names_follow_prefix_and_suffix_standard():
 root=Path(__file__).parent; pattern=re.compile(r"^aws_(?:shared_[a-z0-9_]+|[a-z0-9_]+)_core_ecosystem$")
 ignored={"php","tests"}; dirs=[p.name for p in root.iterdir() if p.is_dir() and p.name not in ignored]
 assert dirs and all(pattern.fullmatch(name) for name in dirs)
