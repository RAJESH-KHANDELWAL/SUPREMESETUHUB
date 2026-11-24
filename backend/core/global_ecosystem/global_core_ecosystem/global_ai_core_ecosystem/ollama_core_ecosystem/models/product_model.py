from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="ollama"
 ecosystem_id:str="AI-OLLAMA-CORE-ECOSYSTEM"
