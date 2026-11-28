from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="groq"
 ecosystem_id:str="AI-GROQ-CORE-ECOSYSTEM"
