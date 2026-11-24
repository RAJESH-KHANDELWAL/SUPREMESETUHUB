from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="replicate"
 ecosystem_id:str="AI-REPLICATE-CORE-ECOSYSTEM"
