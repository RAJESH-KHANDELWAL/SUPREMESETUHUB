from dataclasses import dataclass
@dataclass(frozen=True)
class ProductModel:
 provider_id:str="anthropic_claude"
 ecosystem_id:str="AI-ANTHROPIC_CLAUDE-CORE-ECOSYSTEM"
