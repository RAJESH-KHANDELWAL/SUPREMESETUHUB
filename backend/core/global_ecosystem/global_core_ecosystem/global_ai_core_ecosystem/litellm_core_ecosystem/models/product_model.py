from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="litellm"
 ecosystem_id:str="AI-LITELLM-CORE-ECOSYSTEM"
