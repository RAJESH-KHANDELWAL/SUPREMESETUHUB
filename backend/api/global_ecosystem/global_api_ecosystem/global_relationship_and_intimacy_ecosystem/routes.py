"""Read-only discovery routes for the global relationship and intimacy ecosystem."""
from fastapi import APIRouter, HTTPException, Query

from .schemas import IntimacyCategory, IntimacyEcosystemStatus, IntimacyProvider
from .service import get_ecosystem_status, list_categories, list_providers
from ..categories import list_category_packages
from .providers import list_entries as list_provider_entries
from .integrations.routes import router as integrations_router
from .services.routes import router as services_router
from .tools.routes import router as tools_router

router = APIRouter(
    prefix="/api/v1/global-intimacy-ecosystem",
    tags=["GLOBAL RELATIONSHIP AND INTIMACY ECOSYSTEM"],
)

router.include_router(integrations_router)
router.include_router(services_router)
router.include_router(tools_router)


@router.get("/status", response_model=IntimacyEcosystemStatus)
def ecosystem_status():
    """Describe catalog readiness without implying live provider connections."""
    return get_ecosystem_status()


@router.get("/categories", response_model=list[IntimacyCategory])
def categories():
    """List all relationship, intimacy, sexual-health, and adult-industry categories."""
    return list_categories()


@router.get("/categories/packages")
def category_packages():
    """List the visible category subpackages in the repository structure."""
    return list_category_packages()


@router.get("/providers", response_model=list[IntimacyProvider])
def providers(category_id: str | None = Query(default=None, max_length=64)):
    """List catalog providers, optionally filtered by a category identifier."""
    if category_id:
        key = category_id.strip().upper()
        if key not in {item["category_id"] for item in list_categories()}:
            raise HTTPException(status_code=404, detail="CATEGORY_NOT_FOUND")
    return list_providers(category_id)


@router.get("/providers/directory", response_model=list[IntimacyProvider])
def provider_directory(category_id: str | None = Query(default=None, max_length=64)):
    """Expose the canonical provider research directory from its own package."""
    if category_id:
        key = category_id.strip().upper()
        if key not in {item["category_id"] for item in list_categories()}:
            raise HTTPException(status_code=404, detail="CATEGORY_NOT_FOUND")
    return list_provider_entries(category_id)


# Canonical API namespace. The legacy /global-intimacy-ecosystem routes remain
# available during migration so existing clients do not break.
relationship_router = APIRouter(
    prefix="/api/v1/global-relationship-and-intimacy-ecosystem",
    tags=["GLOBAL RELATIONSHIP AND INTIMACY ECOSYSTEM"],
)
relationship_router.include_router(integrations_router)
relationship_router.include_router(services_router)
relationship_router.include_router(tools_router)

@relationship_router.get("/status", response_model=IntimacyEcosystemStatus)
def relationship_ecosystem_status():
    """Return honest readiness and catalog counts for the canonical API namespace."""
    return get_ecosystem_status()

@relationship_router.get("/categories", response_model=list[IntimacyCategory])
def relationship_categories():
    """List categories using the canonical relationship-and-intimacy API path."""
    return list_categories()

@relationship_router.get("/categories/packages")
def relationship_category_packages():
    """List category package metadata for the canonical API namespace."""
    return list_category_packages()

@relationship_router.get("/providers", response_model=list[IntimacyProvider])
def relationship_providers(category_id: str | None = Query(default=None, max_length=64)):
    """List canonical providers, optionally filtered by category ID."""
    if category_id:
        key = category_id.strip().upper()
        if key not in {item["category_id"] for item in list_categories()}:
            raise HTTPException(status_code=404, detail="CATEGORY_NOT_FOUND")
    return list_providers(category_id)

@relationship_router.get("/providers/directory", response_model=list[IntimacyProvider])
def relationship_provider_directory(category_id: str | None = Query(default=None, max_length=64)):
    """List provider-specific module metadata through the canonical API namespace."""
    if category_id:
        key = category_id.strip().upper()
        if key not in {item["category_id"] for item in list_categories()}:
            raise HTTPException(status_code=404, detail="CATEGORY_NOT_FOUND")
    return list_provider_entries(category_id)

@relationship_router.get("/providers/{provider_id}", response_model=IntimacyProvider)
def relationship_provider_detail(provider_id: str):
    """Fetch one provider record; unknown identifiers return a stable 404 response."""
    provider = next((item for item in list_provider_entries() if item["provider_id"] == provider_id.strip().lower()), None)
    if provider is None:
        raise HTTPException(status_code=404, detail="PROVIDER_NOT_FOUND")
    return provider
