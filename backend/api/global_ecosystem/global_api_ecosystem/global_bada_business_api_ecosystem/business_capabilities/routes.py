"""API routes for Bada Business lifecycle, trust, compliance and BI contracts."""
from fastapi import APIRouter

from .service import (
    get_business_intelligence,
    get_capability_integrity,
    get_compliance,
    get_lifecycle,
    get_trust_safety,
)

router = APIRouter(prefix="/capabilities", tags=["GLOBAL BADA BUSINESS - CAPABILITIES"])

@router.get("/lifecycle")
def lifecycle():
    return get_lifecycle()

@router.get("/trust-safety")
def trust_safety():
    return get_trust_safety()

@router.get("/compliance/framework")
def compliance_framework():
    return get_compliance()

@router.get("/business-intelligence")
def business_intelligence():
    return get_business_intelligence()

@router.get("/integrity")
def capability_integrity():
    return get_capability_integrity()

@router.get("/architecture/modules")
def connected_module_inventory():
    # Import at request time to avoid a package import cycle while observing
    # the final router after all child routers have been mounted.
    from ..routes import router as ecosystem_router

    # Build the effective OpenAPI schema so nested routers included by
    # FastAPI are expanded with their inherited prefixes. Reading router.routes
    # directly is not reliable across FastAPI versions because included routers
    # may be represented by internal wrapper objects without a .path attribute.
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(ecosystem_router)
    openapi_paths = app.openapi().get("paths", {})
    prefix = "/api/v1/global-ecosystem/business"
    http_methods = {"get", "post", "put", "patch", "delete", "options", "head"}
    grouped = {}
    for path, operations in openapi_paths.items():
        if not path.startswith(prefix):
            continue
        relative = path[len(prefix):].strip("/")
        segments = relative.split("/") if relative else []
        module_id = (
            f"industries/{segments[1]}"
            if len(segments) > 1 and segments[0] == "industries"
            else segments[0] if segments else "root"
        )
        methods = sorted(method.upper() for method in operations if method.lower() in http_methods and method.lower() not in {"head", "options"})
        if methods:
            grouped.setdefault(module_id, []).append({"path": path, "methods": methods})

    modules = [
        {"id": module_id, "endpoint_count": len(endpoints), "endpoints": sorted(endpoints, key=lambda item: item["path"])}
        for module_id, endpoints in sorted(grouped.items())
    ]
    return {
        "success": True,
        "ecosystem_id": "global-bada-business",
        "architecture": "one_connected_ecosystem_with_separately_owned_api_modules",
        "module_count": len(modules),
        "endpoint_count": sum(item["endpoint_count"] for item in modules),
        "modules": modules,
        "ecosystem_boundaries": [
            {"id": "bada_business", "ownership": "this folder", "relationship": "current API ecosystem"},
            {"id": "company_companies", "ownership": "separate owning ecosystem", "relationship": "connect through its documented API; do not duplicate its implementation here"},
            {"id": "platforms", "ownership": "separate owning ecosystem", "relationship": "connect through its documented API; do not duplicate its implementation here"},
            {"id": "organizations", "ownership": "separate owning ecosystem", "relationship": "connect through its documented API; do not duplicate its implementation here"},
        ],
        "external_api_policy": "Authorised provider APIs only; banking and payment APIs remain in their separately owned folders.",
        "ai_automation_in_scope": False,
        "note": "Inventory reflects routes registered in this Python router; it does not prove external APIs are live or that every module is production-ready.",
    }
