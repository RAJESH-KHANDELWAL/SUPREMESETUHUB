"""Validate individual terminology entries."""
from dataclasses import dataclass
@dataclass(frozen=True)
class GlossaryEntry:
 source_term: str
 target_term: str
 source_language: str
 target_language: str
 domain: str = "general"
 preferred: bool = True

def validate_glossary_entry(entry: GlossaryEntry) -> GlossaryEntry:
 if not all((entry.source_term.strip(), entry.target_term.strip(), entry.source_language.strip(), entry.target_language.strip())):
  raise ValueError("terms and language codes are required")
 if entry.source_language == entry.target_language and entry.source_term != entry.target_term:
  raise ValueError("same-language glossary entries must preserve the term or explicitly model a variant")
 return entry
