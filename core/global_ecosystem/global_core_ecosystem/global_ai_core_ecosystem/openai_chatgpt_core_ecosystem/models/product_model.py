from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="openai_chatgpt"
 ecosystem_id:str="AI-OPENAI_CHATGPT-CORE-ECOSYSTEM"
