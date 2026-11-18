from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="snowflake_cortex"
 ecosystem_id:str="AI-SNOWFLAKE_CORTEX-CORE-ECOSYSTEM"
