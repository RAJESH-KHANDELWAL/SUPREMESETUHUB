from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="aws_bedrock"
 ecosystem_id:str="AI-AWS_BEDROCK-CORE-ECOSYSTEM"
