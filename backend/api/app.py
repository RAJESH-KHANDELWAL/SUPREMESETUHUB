from __future__ import annotations

from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from backend.auth.service import AuthenticationService
from backend.supreme.config import USERNAME as SUPREME_OWNER_USERNAME

from backend.api.auth import router as auth_router
from backend.api.core_readiness import router as core_readiness_router
from backend.api.storage_routes import router as storage_routes_router
from backend.api.businesses import router as businesses_router
from backend.api.dashboard import router as dashboard_router
from backend.api.dns import router as dns_router
from backend.api.gallary_woult import router as gallary_woult_router
from backend.api.identity import router as identity_router
from backend.api.infrastructure import router as infrastructure_router
from backend.api.matching import router as matching_router
from backend.api.mukti_mahal import router as mukti_mahal_router
from backend.api.mukti_mahal_creation import (
    router as mukti_mahal_creation_router,
)
from backend.api.mukti_mahal_media import (
    router as mukti_mahal_media_router,
)
from backend.api.opportunities import router as opportunities_router
from backend.api.profiles import router as profiles_router
from backend.api.projects import router as projects_router
from backend.api.roles import router as roles_router
from backend.api.supreme import router as supreme_router
from backend.api.supreme_personal_ai import router as supreme_personal_ai_router
from backend.api.supreme_ecosystem import router as supreme_ecosystem_router
from backend.api.supreme_work_income import router as supreme_work_income_router
from backend.api.supreme_whatsapp_ai import router as supreme_whatsapp_ai_router
from backend.api.users import router as users_router
from backend.api.user_hub import router as user_hub_router
from backend.api.ai import router as ai_router
from backend.api.global_ai_ecosystem import router as global_ai_ecosystem_router
from backend.api.global_business_ecosystem import router as global_business_ecosystem_router
from backend.api.global_ecosystem import GlobalEcosystemAPI
from backend.api.cloud import CloudAPI
from backend.api.storage import StorageAPI
from backend.api.theme_hub import router as theme_hub_router

from backend.wordpress.bootstrap import create_wordpress_service

from backend.api.connectors import router as connectors_router
from backend.api.linksetu import router as linksetu_router
from backend.api.email import router as email_router
from backend.api.print_on_demand import router as print_on_demand_router
from backend.api.digital_marketplace import router as digital_marketplace_router


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

FRONTEND_DIR = BASE_DIR / "frontend"
ROOT_FRONTEND_FILE = FRONTEND_DIR / "index.html"
POD_JS_FILE = FRONTEND_DIR / "print-on-demand.js"

SUPREME_FRONTEND_DIR = FRONTEND_DIR / "supreme"
SUPREME_HTML_FILE = SUPREME_FRONTEND_DIR / "index.html"
SUPREME_CSS_FILE = SUPREME_FRONTEND_DIR / "style.css"


# ============================================================
# MAIN APPLICATION
# ============================================================

app = FastAPI(
    title="SUPREMESETUHUB",
    version="1.0.0",
)


# ============================================================
# CORE SERVICES
# ============================================================

ecosystem_api = GlobalEcosystemAPI()
cloud_api = CloudAPI()
storage_api = StorageAPI()

wordpress_service = create_wordpress_service()


# ============================================================
# CORS CONFIGURATION
# ============================================================

ALLOWED_ORIGINS = [
    # GITHUB PAGES
    "https://rajeshkhandelwal.github.io",
    "https://rajeshkhandelwalofficial.github.io",
    "https://drrajeshkhandelwalibc.github.io",
    "https://drrajeshkhandelwalibcofficial.github.io",

    # MAIN DOMAINS
    "https://rajeshkhandelwal.com",
    "https://www.rajeshkhandelwal.com",
    "https://rajeshkhandelwalofficial.com",
    "https://www.rajeshkhandelwalofficial.com",
    "https://drrajeshkhandelwalibc.com",
    "https://www.drrajeshkhandelwalibc.com",
    "https://drrajeshkhandelwalibcofficial.com",
    "https://www.drrajeshkhandelwalibcofficial.com",

    # RENDER DOMAINS
    "https://rajeshkhandelwal.onrender.com",
    "https://rajeshkhandelwalofficial.onrender.com",
    "https://drrajeshkhandelwalibc.onrender.com",
    "https://drrajeshkhandelwalibcofficial.onrender.com",

    # SUPREMESETUHUB RENDER
    "https://supremesetuhub-3v4e.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# AUTHENTICATION SERVICE
# ============================================================

authentication_service = AuthenticationService()


# ============================================================
# PRIVATE-BY-DEFAULT API ACCESS
# ============================================================

# Public entry points are limited to platform signup/signin, health checks,
# and frontend assets. SUPREME and SUPREME ECOSYSTEM are private control
# systems: their routes must never be used as public customer account APIs.
# Customer sign-up/sign-in uses /users/signup and /auth/signin; legacy registration remains supported.
PUBLIC_API_PATHS = {
    "/health",
    "/print-on-demand.js",
    "/auth/initialize",
    "/auth/signin",
    "/users/signup",
    "/users/register",
    "/api/v1/supreme-ecosystem/whatsapp/webhook",
    "/api/v1/frontend/supreme",
    "/api/v1/frontend/supreme/style.css",
    "/api/v1/frontend/supreme/health",
    "/api/v1/digital-marketplace/catalog",
    "/api/v1/print-on-demand/public/catalog",
}


@app.middleware("http")
async def private_by_default(request: Request, call_next):
    path = request.url.path

    if request.method == "OPTIONS" or path in PUBLIC_API_PATHS or path == "/":
        return await call_next(request)

    authorization = request.headers.get("Authorization", "")
    if not authorization.startswith("Bearer "):
        return JSONResponse(
            status_code=401,
            content={
                "detail": "AUTHENTICATION_REQUIRED",
                "message": "Sign in as the SUPREME owner to access private data.",
            },
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = authorization[len("Bearer "):].strip()
    if not token:
        return JSONResponse(
            status_code=401,
            content={"detail": "AUTHENTICATION_REQUIRED"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    result = authentication_service.validate_token(token)
    if not result.get("authenticated"):
        return JSONResponse(
            status_code=401,
            content={
                "detail": result.get("message", "INVALID_OR_EXPIRED_TOKEN"),
            },
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = str(result.get("username", "")).strip()

    # SUPREME ECOSYSTEM is a private owner-control system. No regular
    # platform account may use its signup, signin, dashboard, account,
    # status, or integration endpoints.
    is_private_ecosystem_path = (
        path == "/api/v1/supreme-ecosystem"
        or path.startswith("/api/v1/supreme-ecosystem/")
    )
    is_supreme_owner = (
        username.casefold() == SUPREME_OWNER_USERNAME.casefold()
    )

    if is_private_ecosystem_path and not is_supreme_owner:
        return JSONResponse(
            status_code=403,
            content={
                "detail": "SUPREME_ECOSYSTEM_PRIVATE",
                "message": "SUPREME ECOSYSTEM is reserved for its owner.",
            },
        )

    # The user hub has its own token-to-identity ownership check. Allow a
    # signed-in customer through so the route can return only that customer's
    # profiles, businesses, and projects. Other data APIs remain owner-only
    # until their resource-level ownership checks are implemented.
    if path.startswith("/user-hub/"):
        return await call_next(request)

    # Storage APIs enforce per-asset owner permissions in the route layer.
    # Health endpoints expose only non-secret diagnostics to signed-in users.
    if path.startswith("/api/v1/storage/") or path in {
        "/api/v1/database/health",
        "/api/v1/engines/status",
    }:
        return await call_next(request)

    # Print-on-demand routes implement user-scoped design briefs and use
    # get_current_user for identity; allow regular signed-in customers here.
    if path.startswith("/api/v1/print-on-demand/"):
        return await call_next(request)

    if not is_supreme_owner:
        return JSONResponse(
            status_code=403,
            content={
                "detail": "SUPREME_OWNER_ACCESS_REQUIRED",
                "message": (
                    "This API is private until explicit resource-level "
                    "permissions and data isolation are implemented."
                ),
            },
        )

    return await call_next(request)


# ============================================================
# AUTHENTICATED USER IDENTIFICATION
# ============================================================

def _require_ai_store_actor(
    authorization: Optional[str],
) -> str:

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="AUTHORIZATION_REQUIRED",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="INVALID_AUTHORIZATION_HEADER",
        )

    token = authorization[len("Bearer "):].strip()

    if not token:
        raise HTTPException(
            status_code=401,
            detail="EMPTY_AUTH_TOKEN",
        )

    result = authentication_service.validate_token(token)

    if not result.get("authenticated"):
        raise HTTPException(
            status_code=401,
            detail=result.get(
                "message",
                "INVALID_AUTHENTICATION_TOKEN",
            ),
        )

    username = result.get("username")

    if not username:
        raise HTTPException(
            status_code=401,
            detail="AUTHENTICATED_USERNAME_NOT_FOUND",
        )

    return username


# ============================================================
# CORE API ROUTERS
# ============================================================

app.include_router(auth_router)
app.include_router(core_readiness_router)
app.include_router(storage_routes_router)
app.include_router(users_router)
app.include_router(identity_router)
app.include_router(profiles_router)
app.include_router(businesses_router)
app.include_router(projects_router)
app.include_router(opportunities_router)
app.include_router(matching_router)
app.include_router(roles_router)
app.include_router(supreme_router)
app.include_router(supreme_personal_ai_router)
app.include_router(supreme_ecosystem_router)
app.include_router(supreme_work_income_router)
app.include_router(supreme_whatsapp_ai_router)
app.include_router(dashboard_router)
app.include_router(infrastructure_router)
app.include_router(dns_router)
app.include_router(user_hub_router)
app.include_router(ai_router)
app.include_router(global_ai_ecosystem_router)
app.include_router(global_business_ecosystem_router)
app.include_router(theme_hub_router)
app.include_router(connectors_router)
app.include_router(linksetu_router)
app.include_router(email_router)
app.include_router(print_on_demand_router)
app.include_router(digital_marketplace_router)


# ============================================================
# GALLARY WOULT
# ============================================================

app.include_router(gallary_woult_router)


# ============================================================
# MUKTI MAHAL
# ============================================================

app.include_router(mukti_mahal_router)
app.include_router(mukti_mahal_creation_router)
app.include_router(mukti_mahal_media_router)


# ============================================================
# ROOT HOME PAGE
# ============================================================

@app.get("/")
def root():

    if not ROOT_FRONTEND_FILE.is_file():
        raise HTTPException(
            status_code=404,
            detail="ROOT frontend not found",
        )

    return FileResponse(
        ROOT_FRONTEND_FILE,
        media_type="text/html",
    )

@app.get("/print-on-demand.js")
def print_on_demand_frontend_script():
    if not POD_JS_FILE.is_file():
        raise HTTPException(status_code=404, detail="Print on Demand frontend script not found")
    return FileResponse(POD_JS_FILE, media_type="application/javascript")


# ============================================================
# SUPREME FRONTEND HTML
# ============================================================

@app.get("/api/v1/frontend/supreme")
def supreme_frontend():

    if not SUPREME_HTML_FILE.is_file():
        raise HTTPException(
            status_code=404,
            detail="SUPREME frontend HTML not found",
        )

    return FileResponse(
        SUPREME_HTML_FILE,
        media_type="text/html",
    )


# ============================================================
# SUPREME FRONTEND CSS
# ============================================================

@app.get("/api/v1/frontend/supreme/style.css")
def supreme_frontend_css():

    if not SUPREME_CSS_FILE.is_file():
        raise HTTPException(
            status_code=404,
            detail="SUPREME frontend CSS not found",
        )

    return FileResponse(
        SUPREME_CSS_FILE,
        media_type="text/css",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )


# ============================================================
# SUPREME FRONTEND STATUS
# ============================================================

@app.get("/api/v1/frontend/supreme/health")
def supreme_frontend_health():

    return {
        "success": True,
        "service": "SUPREMESETUHUB",
        "frontend": "supreme",
        "html": SUPREME_HTML_FILE.is_file(),
        "css": SUPREME_CSS_FILE.is_file(),
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "SUPREMESETUHUB",
    }


# ============================================================
# WORDPRESS STATUS
# ============================================================

@app.get("/api/v1/wordpress/sites")
def wordpress_sites():

    return {
        "success": True,
        "sites": [
            site.to_dict()
            for site in wordpress_service.list_sites()
        ],
    }


@app.get("/api/v1/wordpress/status/{site_id}")
def wordpress_status(site_id: str):

    return wordpress_service.connection_status(site_id)


@app.get("/api/v1/wordpress/health/{site_id}")
def wordpress_health(site_id: str):

    result = wordpress_service.connect_site(
        site_id=site_id,
        environment_prefix="WORDPRESS",
    )

    if not result.get("success"):
        return result

    return {
        "success": True,
        "status": "CONNECTED",
        "site_id": site_id,
        "domain": result.get("domain"),
        "database": result.get("database"),
        "health": result.get("health"),
        "wordpress_tables": (
            wordpress_service.check_wordpress(site_id)
        ),
    }


# ============================================================
# FOUNDATION STATUS API
# ============================================================

@app.get("/api/v1/foundation")
def foundation():

    return {
        "success": True,
        "name": "SUPREMESETUHUB",
        "version": "1.0.0",
        "status": "active",
    }


# ============================================================
# LEGACY ECOSYSTEM API
# Existing URLs preserved for backward compatibility
# ============================================================

@app.get("/api/v1/ecosystem/status")
def ecosystem_status():
    return ecosystem_api.status()


@app.get("/api/v1/ecosystem/health")
def ecosystem_health():
    return ecosystem_api.health()


@app.get("/api/v1/ecosystem/list")
def ecosystem_list():
    return ecosystem_api.list()


@app.get("/api/v1/ecosystem/names")
def ecosystem_names():
    return ecosystem_api.names()


@app.get("/api/v1/ecosystem/{ecosystem_id}/exists")
def ecosystem_exists(ecosystem_id: str):
    return {
        "ecosystem_id": ecosystem_id,
        "exists": ecosystem_api.exists(ecosystem_id),
    }


@app.get("/api/v1/ecosystem/{ecosystem_id}")
def ecosystem_get(ecosystem_id: str):
    return ecosystem_api.get(ecosystem_id)


# ============================================================
# GLOBAL ECOSYSTEM API
# ============================================================

@app.get("/api/v1/global-ecosystem/status")
def global_ecosystem_status():
    return ecosystem_api.status()


@app.get("/api/v1/global-ecosystem/health")
def global_ecosystem_health():
    return ecosystem_api.health()


@app.get("/api/v1/global-ecosystem/tree")
def global_ecosystem_tree():
    return ecosystem_api.tree()


@app.get("/api/v1/global-ecosystem/list")
def global_ecosystem_list():
    return ecosystem_api.list()


@app.get("/api/v1/global-ecosystem/names")
def global_ecosystem_names():
    return ecosystem_api.names()


@app.get("/api/v1/global-ecosystem/{ecosystem_id}/exists")
def global_ecosystem_exists(ecosystem_id: str):
    return {
        "ecosystem_id": ecosystem_id,
        "exists": ecosystem_api.exists(ecosystem_id),
    }


@app.get("/api/v1/global-ecosystem/{ecosystem_id}")
def global_ecosystem_get(ecosystem_id: str):
    return ecosystem_api.get(ecosystem_id)


# ============================================================
# GLOBAL CLOUD ECOSYSTEM
# ============================================================

@app.get("/api/v1/global-cloud/status")
def global_cloud_status():
    return cloud_api.status()


@app.get("/api/v1/global-cloud/health")
def global_cloud_health():
    return cloud_api.health()


@app.get("/api/v1/global-cloud/providers")
def global_cloud_providers():
    return {
        "success": True,
        "providers": cloud_api.providers(),
    }


# ============================================================
# GLOBAL CLOUD STORAGE
# ============================================================

@app.get("/api/v1/global-cloud-storage/status")
def global_cloud_storage_status():
    return storage_api.status()


@app.get("/api/v1/global-cloud-storage/health")
def global_cloud_storage_health():
    return storage_api.health()


@app.get("/api/v1/global-cloud-storage/configuration")
def global_cloud_storage_configuration():
    return storage_api.configuration()


# ============================================================
# GLOBAL STORAGE ECOSYSTEM
# ============================================================

@app.get("/api/v1/global-storage-ecosystem/status")
def global_storage_ecosystem_status():
    return {
        "success": True,
        "ecosystem": "GLOBAL STORAGE ECOSYSTEM",
        "cloud_storage": storage_api.status(),
        "storage_configuration": storage_api.configuration(),
        "cloud_providers": cloud_api.providers(),
        "external_storage_connected": False,
        "google_cloud_setup": "DEFERRED",
    }
