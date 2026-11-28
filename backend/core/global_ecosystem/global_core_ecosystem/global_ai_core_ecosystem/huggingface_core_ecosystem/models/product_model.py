from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="huggingface"
 ecosystem_id:str="AI-HUGGINGFACE-CORE-ECOSYSTEM"
