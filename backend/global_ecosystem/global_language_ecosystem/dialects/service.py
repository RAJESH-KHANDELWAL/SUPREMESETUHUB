"""Create structured dialect profiles without treating dialects as inferior."""
from dataclasses import dataclass
@dataclass(frozen=True)
class DialectProfile:
 language_code: str
 variety_name: str
 region: str
 community_label: str | None = None
 notes: str | None = None

def build_dialect_profile(language_code: str, variety_name: str, region: str, *, community_label: str | None = None, notes: str | None = None) -> DialectProfile:
 if not all(x.strip() for x in (language_code, variety_name, region)):
  raise ValueError("language_code, variety_name and region are required")
 return DialectProfile(language_code.strip(), variety_name.strip(), region.strip(), community_label, notes)
