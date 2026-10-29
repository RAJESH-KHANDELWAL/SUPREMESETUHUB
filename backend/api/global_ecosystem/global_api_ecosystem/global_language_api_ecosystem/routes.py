"""API routes for the Global Language API Ecosystem."""
from fastapi import APIRouter, Query

from .adult_language_catalog import (
    get_adult_language_summary,
    list_adult_language_domains,
)
from .language_catalog import (
    get_language_summary,
    list_languages,
    list_locales,
)

router = APIRouter(tags=["global-language-api-ecosystem"])

@router.get("/languages", summary="List supported language catalog entries")
def get_languages(
    q: str | None = Query(default=None, description="Filter by language name, identifier, or family"),
    limit: int = Query(default=250, ge=1, le=500),
):
    """Return the curated world-language starter catalog."""
    return {"summary": get_language_summary(), "items": list_languages(q, limit)}

@router.get("/locales", summary="List language and regional locale variants")
def get_language_locales(
    language: str | None = Query(default=None, description="Language identifier such as en, hi, or ar"),
    limit: int = Query(default=250, ge=1, le=500),
):
    """Return available locale definitions in the catalog."""
    return {"count": len(list_locales(language, limit)), "items": list_locales(language, limit)}

@router.get("/adult-language/domains", summary="List adult relationship and sexual-health language domains")
def get_adult_language_domains(q: str | None = Query(default=None, description="Filter adult-language education domains")):
    """Return non-graphic, educational adult language support categories."""
    items = list_adult_language_domains(q)
    return {"summary": get_adult_language_summary(), "items": items}

@router.get("/adult-language/summary", summary="Describe adult-language coverage")
def get_adult_language_status():
    """Return scope and limitations for adult-language support."""
    return get_adult_language_summary()
