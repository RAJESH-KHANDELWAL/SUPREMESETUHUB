"""Independent ENGINE catalog for AWS."""
from .models import EngineDescriptor
PROVIDER = "AWS"
CHILD_ECOSYSTEMS = [
    "AWS API GATEWAY ECOSYSTEM",
    "AWS BEDROCK SAGEMAKER",
    "AWS BILLING COST",
    "AWS CLOUDFORMATION",
    "AWS CLOUDTRAIL",
    "AWS CLOUDWATCH",
    "AWS CONTAINERS",
    "AWS DATABASE",
    "AWS EC2 COMPUTE",
    "AWS IAM STS",
    "AWS KMS SECRETS",
    "AWS LAMBDA",
    "AWS LIGHTSAIL",
    "AWS ROUTE53 DNS",
    "AWS S3 STORAGE",
    "AWS VPC NETWORKING"
]
CATALOG = (EngineDescriptor("ENGINE-AWS", PROVIDER, PROVIDER, ("LIFECYCLE","EXECUTION_BOUNDARY")),)
def list_engines():
    return [dict(engine_id=x.engine_id,name=x.name,provider=x.provider,capabilities=list(x.capabilities),metadata=dict(x.metadata)) for x in CATALOG]
