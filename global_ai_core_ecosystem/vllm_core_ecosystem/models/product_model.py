from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="vllm"
 ecosystem_id:str="AI-VLLM-CORE-ECOSYSTEM"
