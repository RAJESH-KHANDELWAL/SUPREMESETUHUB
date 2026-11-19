from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="cohere"
 ecosystem_id:str="AI-COHERE-CORE-ECOSYSTEM"
