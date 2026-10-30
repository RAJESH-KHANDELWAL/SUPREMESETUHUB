"""API routes for the Global Language API Ecosystem."""
from fastapi import APIRouter, Query

from .adult_language_catalog import get_adult_language_summary, list_adult_language_domains
from .api_modules import get_api_module_summary, list_api_modules
from .language_catalog import get_language_summary, list_languages, list_locales

router = APIRouter(tags=["global-language-api-ecosystem"])


@router.get("/api-modules", summary="List Global Language API modules")
def get_global_language_api_modules(
    category: str | None = Query(default=None, description="Filter by module category"),
    status: str | None = Query(default=None, description="Filter by implementation status"),
):
    """Return module registry and readiness metadata."""
    items = list_api_modules(category=category, status=status)
    return {"summary": get_api_module_summary(), "count": len(items), "items": items}


@router.get("/api-modules/summary", summary="Summarize Global Language API modules")
def get_global_language_api_module_status():
    """Return API module counts and provider-integration status."""
    return get_api_module_summary()


@router.get("/languages", summary="List supported language catalog entries")
def get_languages(
    q: str | None = Query(default=None, description="Filter by language name, identifier, or family"),
    limit: int = Query(default=250, ge=1, le=500),
):
    """Return the curated world-language starter catalog."""
    items = list_languages(q, limit)
    return {"summary": get_language_summary(), "count": len(items), "items": items}


@router.get("/locales", summary="List language and regional locale variants")
def get_language_locales(
    language: str | None = Query(default=None, description="Language identifier such as en, hi, or ar"),
    limit: int = Query(default=250, ge=1, le=500),
):
    """Return available locale definitions in the catalog."""
    items = list_locales(language, limit)
    return {"count": len(items), "items": items}


@router.get("/adult-language/domains", summary="List adult relationship and mature-language domains")
def get_adult_language_domains(q: str | None = Query(default=None, description="Filter adult-language education and register domains")):
    """Return non-graphic adult-language support categories."""
    items = list_adult_language_domains(q)
    return {"summary": get_adult_language_summary(), "count": len(items), "items": items}


@router.get("/adult-language/summary", summary="Describe adult-language coverage")
def get_adult_language_status():
    """Return scope and limitations for adult-language support."""
    return get_adult_language_summary()
