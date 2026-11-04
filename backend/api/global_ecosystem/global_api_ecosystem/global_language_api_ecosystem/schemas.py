"""Response schemas for the Global Language API Ecosystem."""
from pydantic import BaseModel, Field

class LanguageItem(BaseModel):
    id: str = Field(description="Language identifier")
    name: str
    family: str

class LocaleItem(BaseModel):
    id: str
    language: str
    region: str

class CatalogSummary(BaseModel):
    language_count: int = 0
    locale_count: int = 0
    provider_status: str = "CATALOG_ONLY"
    live_translation_available: bool = False
