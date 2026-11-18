from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="ibm_watsonx"
 ecosystem_id:str="AI-IBM_WATSONX-CORE-ECOSYSTEM"
