"""AWS service ecosystem catalog.

Product/service entries are separate from API capability families. Catalog only;
no live integrations are implied by the presence of these entries.
"""
from __future__ import annotations

AWS_SERVICE_ECOSYSTEMS = (
    {"folder": "aws_amazon_s3_api_ecosystem", "name": "Amazon S3", "scope": "Object storage and data transfer", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_ec2_api_ecosystem", "name": "Amazon EC2", "scope": "Virtual compute instances", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_lambda_api_ecosystem", "name": "AWS Lambda", "scope": "Serverless compute", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_lightsail_api_ecosystem", "name": "Amazon Lightsail", "scope": "Simplified cloud servers and hosting", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_rds_api_ecosystem", "name": "Amazon RDS", "scope": "Managed relational databases", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_dynamodb_api_ecosystem", "name": "Amazon DynamoDB", "scope": "Managed NoSQL database", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_iam_api_ecosystem", "name": "AWS IAM", "scope": "Identity and access management", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_sts_api_ecosystem", "name": "AWS STS", "scope": "Temporary security credentials", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_s3_glacier_api_ecosystem", "name": "Amazon S3 Glacier", "scope": "Archive storage classes", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_route53_api_ecosystem", "name": "Amazon Route 53", "scope": "DNS and domain routing", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_cloudfront_api_ecosystem", "name": "Amazon CloudFront", "scope": "Content delivery network", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_api_gateway_api_ecosystem", "name": "Amazon API Gateway", "scope": "Managed API front door", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_vpc_api_ecosystem", "name": "Amazon VPC", "scope": "Virtual networking", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_cloudwatch_api_ecosystem", "name": "Amazon CloudWatch", "scope": "Monitoring and observability", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_cloudtrail_api_ecosystem", "name": "AWS CloudTrail", "scope": "Audit and account activity", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_kms_api_ecosystem", "name": "AWS KMS", "scope": "Key management", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_secrets_manager_api_ecosystem", "name": "AWS Secrets Manager", "scope": "Secrets storage and rotation", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_bedrock_api_ecosystem", "name": "Amazon Bedrock", "scope": "Foundation model and generative AI services", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_sagemaker_api_ecosystem", "name": "Amazon SageMaker AI", "scope": "Machine learning development and hosting", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_ecs_api_ecosystem", "name": "Amazon ECS", "scope": "Container orchestration", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_eks_api_ecosystem", "name": "Amazon EKS", "scope": "Managed Kubernetes", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_ecr_api_ecosystem", "name": "Amazon ECR", "scope": "Container image registry", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_sqs_api_ecosystem", "name": "Amazon SQS", "scope": "Message queues", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_sns_api_ecosystem", "name": "Amazon SNS", "scope": "Pub/sub messaging and notifications", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_eventbridge_api_ecosystem", "name": "Amazon EventBridge", "scope": "Event routing and integration", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_step_functions_api_ecosystem", "name": "AWS Step Functions", "scope": "Workflow orchestration", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_cloudformation_api_ecosystem", "name": "AWS CloudFormation", "scope": "Infrastructure as code", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_cdk_api_ecosystem", "name": "AWS Cloud Development Kit", "scope": "Infrastructure as code SDK", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_organizations_api_ecosystem", "name": "AWS Organizations", "scope": "Multi-account governance", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_control_tower_api_ecosystem", "name": "AWS Control Tower", "scope": "Multi-account landing zone governance", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_billing_cost_api_ecosystem", "name": "AWS Billing and Cost Management", "scope": "Billing, budgets and cost visibility", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_marketplace_api_ecosystem", "name": "AWS Marketplace", "scope": "Cloud software marketplace", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_console_api_ecosystem", "name": "AWS Management Console", "scope": "Web management interface", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_codebuild_api_ecosystem", "name": "AWS CodeBuild", "scope": "Build and test automation", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_codedeploy_api_ecosystem", "name": "AWS CodeDeploy", "scope": "Application deployment automation", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_codepipeline_api_ecosystem", "name": "AWS CodePipeline", "scope": "Continuous delivery pipelines", "status": "CATALOG_ONLY", "live_connection_verified": False},
    {"folder": "aws_identity_center_api_ecosystem", "name": "AWS IAM Identity Center", "scope": "Workforce identity and SSO", "status": "CATALOG_ONLY", "live_connection_verified": False},
)

AWS_API_CAPABILITIES = (
    "iam_sts", "compute_ec2", "lightsail", "lambda", "containers",
    "s3_storage", "rds_dynamodb", "route53_dns_domains", "vpc_networking",
    "cloudwatch", "cloudtrail", "kms_secrets", "bedrock_sagemaker",
    "billing_cost", "api_gateway", "cloudformation",
)

def list_aws_service_ecosystems() -> list[dict[str, object]]:
    """Return a copy of the AWS service catalog."""
    return [dict(item) for item in AWS_SERVICE_ECOSYSTEMS]

def list_aws_api_capabilities() -> tuple[str, ...]:
    """Return API capability families independently of service products."""
    return AWS_API_CAPABILITIES
