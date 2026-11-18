"""API routes for the Global Language API Ecosystem."""
from fastapi import APIRouter, Query

from .adult_language_catalog import get_adult_language_summary, list_adult_language_domains
from .api_modules import get_api_module_summary, list_api_modules
from .global_language_api_ecosystem import GLOBAL_LANGUAGE_API_ECOSYSTEM
from .language_catalog import get_language_summary, list_languages, list_locales
from .authoritative_catalog import (
    get_authoritative_catalog_status,
    list_iso6393_languages,
    list_cldr_locales,
)

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


@router.get("/ecosystem/catalog", summary="Get the Global Language API ecosystem master catalog")
def get_global_language_catalog():
    """Return category and provider module indexes for this ecosystem."""
    return GLOBAL_LANGUAGE_API_ECOSYSTEM


@router.get("/catalog/sources", summary="Show authoritative language catalog sources")
def get_language_catalog_sources():
    """Return source metadata and local dataset readiness without downloading data."""
    return get_authoritative_catalog_status()


@router.get("/languages", summary="List curated language catalog entries")
def get_languages(
    q: str | None = Query(default=None, description="Filter by language name, identifier, or family"),
    limit: int = Query(default=250, ge=1, le=500),
):
    """Return the built-in curated starter catalog."""
    items = list_languages(q, limit)
    return {"summary": get_language_summary(), "count": len(items), "items": items}


@router.get("/languages/iso639-3", summary="Search locally configured ISO 639-3 language data")
def get_iso6393_languages(
    q: str | None = Query(default=None, description="Filter by ISO code or reference name"),
    limit: int = Query(default=100, ge=1, le=250),
):
    """Search a locally supplied ISO 639-3 table; does not fetch or redistribute source files."""
    items = list_iso6393_languages(q, limit)
    return {
        "source": "ISO 639-3 Registration Authority (SIL)",
        "count": len(items),
        "items": items,
        "catalog_status": get_authoritative_catalog_status()["iso639_3"]["status"],
    }


@router.get("/locales", summary="List curated language and regional locale variants")
def get_language_locales(
    language: str | None = Query(default=None, description="Language identifier such as en, hi, or ar"),
    limit: int = Query(default=250, ge=1, le=500),
):
    """Return built-in locale definitions in the starter catalog."""
    items = list_locales(language, limit)
    return {"count": len(items), "items": items}


@router.get("/locales/cldr", summary="Search locally configured Unicode CLDR locales")
def get_cldr_language_locales(
    q: str | None = Query(default=None, description="Filter by locale identifier"),
    limit: int = Query(default=100, ge=1, le=250),
):
    """Search locale identifiers from a locally supplied CLDR availableLocales JSON file."""
    items = list_cldr_locales(q, limit)
    return {
        "source": "Unicode CLDR",
        "count": len(items),
        "items": items,
        "catalog_status": get_authoritative_catalog_status()["cldr"]["status"],
    }


@router.get("/adult-language/domains", summary="List adult relationship and mature-language domains")
def get_adult_language_domains(
    q: str | None = Query(default=None, description="Filter adult-language education and register domains"),
):
    """Return non-graphic adult-language support categories."""
    items = list_adult_language_domains(q)
    return {"summary": get_adult_language_summary(), "count": len(items), "items": items}


@router.get("/adult-language/summary", summary="Describe adult-language coverage")
def get_adult_language_status():
    """Return scope and limitations for adult-language support."""
    return get_adult_language_summary()
