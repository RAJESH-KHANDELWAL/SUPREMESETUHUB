from __future__ import annotations

from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse

from backend.auth.service import AuthenticationService
from backend.supreme.config import USERNAME as SUPREME_OWNER_USERNAME

from backend.api.auth import router as auth_router
from backend.api.language_services import router as language_services_router
from backend.api.product_ecosystem import router as product_ecosystem_router
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
from backend.api.organizations import router as organizations_router
from backend.api.user_hub import router as user_hub_router
from backend.api.ai import router as ai_router
from backend.api.global_ai_ecosystem import router as global_ai_ecosystem_router
from backend.api.global_business_ecosystem import router as global_business_ecosystem_router
from backend.api.global_freelancer_ecosystem import router as global_freelancer_ecosystem_router
from backend.api.global_ecosystem import GlobalEcosystemAPI
from backend.api.cloud import CloudAPI
from backend.api.storage import StorageAPI
from backend.api.theme_hub import router as theme_hub_router

from backend.api.wordpress import router as wordpress_router, wordpress_service, require_wordpress_owner

from backend.api.connectors import router as connectors_router
from backend.api.linksetu import router as linksetu_router
from backend.api.email import router as email_router
from backend.api.print_on_demand import router as print_on_demand_router
from backend.api.people import router as people_engine_router
from backend.api.payee_verification import router as payee_verification_router
from backend.api.digital_marketplace import router as digital_marketplace_router


# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

FRONTEND_DIR = BASE_DIR / "frontend"
ROOT_FRONTEND_FILE = FRONTEND_DIR / "index.html"
POD_JS_FILE = FRONTEND_DIR / "print-on-demand.js"

SUPREME_FRONTEND_DIR = FRONTEND_DIR / "supreme"
SUPREME_HTML_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "home-html.html"
SUPREME_CSS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "home-css.css"
SUPREME_JS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "home-js.js"
ABOUT_HTML_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "about-html.html"
ABOUT_CSS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "about-css.css"
ABOUT_JS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "about-js.js"
CONTACT_HTML_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "contact-html.html"
CONTACT_CSS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "contact-css.css"
CONTACT_JS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "contact-js.js"
SUPREME_ECOSYSTEM_HTML_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "supreme-ecosystem.html"
SUPREME_ECOSYSTEM_CSS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "supreme-ecosystem.css"
SUPREME_ECOSYSTEM_JS_FILE = SUPREME_FRONTEND_DIR / "supreme-ecosystem" / "supreme-ecosystem.js"


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
    "/api/v1/frontend/supreme/script.js",
    "/api/v1/frontend/supreme/health",
    "/api/v1/frontend/supreme-ecosystem",
    "/api/v1/frontend/supreme-ecosystem/style.css",
    "/api/v1/frontend/supreme-ecosystem/script.js",
    "/api/v1/frontend/supreme-ecosystem/health",
    "/api/v1/frontend/global-business-ecosystem",
    "/api/v1/frontend/global-business-ecosystem/health",
    "/api/v1/digital-marketplace/catalog",
    "/api/v1/products/catalog",
    "/api/v1/products/provider-readiness",
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

    # Treat malformed tokens and validation-service failures as unauthenticated.
    # Never let an invalid credential turn an auth check into an HTTP 500.
    try:
        result = authentication_service.validate_token(token)
    except Exception:
        result = None

    if not isinstance(result, dict) or not result.get("authenticated"):
        message = (
            result.get("message", "INVALID_OR_EXPIRED_TOKEN")
            if isinstance(result, dict)
            else "INVALID_OR_EXPIRED_TOKEN"
        )
        return JSONResponse(
            status_code=401,
            content={"detail": message},
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

    # GLOBAL FREELANCER ECOSYSTEM uses authenticated owner-scoped records.
    # Its API routes enforce per-user record ownership; do not apply the
    # general owner-only restriction to these routes.
    if path == "/api/v1/global-freelancer-ecosystem" or path.startswith("/api/v1/global-freelancer-ecosystem/"):
        return await call_next(request)

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
app.include_router(language_services_router)
app.include_router(product_ecosystem_router)
app.include_router(core_readiness_router)
app.include_router(storage_routes_router)
app.include_router(users_router)
app.include_router(organizations_router)
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
app.include_router(global_freelancer_ecosystem_router)
app.include_router(theme_hub_router)
app.include_router(connectors_router)
app.include_router(linksetu_router)
app.include_router(email_router)
app.include_router(print_on_demand_router)
app.include_router(people_engine_router)
app.include_router(payee_verification_router)
app.include_router(digital_marketplace_router)
app.include_router(wordpress_router)


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

    html = SUPREME_HTML_FILE.read_text(encoding="utf-8")

    # The original Fluent Snippet contains a loader that fetches this same endpoint.
    # Strip that loader from the rendered response to prevent recursive self-embedding.
    html = html.replace(
        '<script src="https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/index.js"></script>',
        "",
    )
    loader_marker = '<div id="SUPREMESETUHUB-HOME"></div>'
    loader_start = html.find(loader_marker)
    if loader_start != -1:
        script_start = html.find("<script>", loader_start)
        script_end = html.find("</script>", script_start) if script_start != -1 else -1
        if script_start != -1 and script_end != -1:
            html = html[:loader_start] + html[script_end + len("</script>"):]

    document = (
        '<!doctype html><html lang="en"><head>'
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<style>html,body{width:100%;max-width:100%;margin:0;padding:0;box-sizing:border-box}*,*::before,*::after{box-sizing:border-box}</style>'
        '<meta name="robots" content="index, follow">'
        '<title>DR RAJESH KHANDELWAL IBC | HOME</title>'
        '<link rel="stylesheet" href="/api/v1/frontend/supreme/style.css?v=20261015-most-welcome">'
        '<script src="/api/v1/frontend/supreme/script.js" defer></script>'
        '</head><body>'
        + html +
        '</body></html>'
    )
    return HTMLResponse(content=document, headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


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


@app.get("/api/v1/frontend/supreme/script.js")
def supreme_frontend_js():
    if not SUPREME_JS_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME frontend JavaScript not found")
    return FileResponse(SUPREME_JS_FILE, media_type="application/javascript")


# ============================================================
# SUPREME FRONTEND STATUS
# ============================================================

# ============================================================
# SUPREME ABOUT AND CONTACT PAGES
# ============================================================

@app.get("/api/v1/frontend/supreme/about")
def supreme_about_frontend():
    if not ABOUT_HTML_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME ABOUT page not found")
    return FileResponse(ABOUT_HTML_FILE, media_type="text/html", headers={"Cache-Control": "no-cache"})


@app.get("/api/v1/frontend/supreme/about/style.css")
def supreme_about_frontend_css():
    if not ABOUT_CSS_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME ABOUT CSS not found")
    return FileResponse(ABOUT_CSS_FILE, media_type="text/css")


@app.get("/api/v1/frontend/supreme/about/script.js")
def supreme_about_frontend_js():
    if not ABOUT_JS_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME ABOUT JavaScript not found")
    return FileResponse(ABOUT_JS_FILE, media_type="application/javascript")


@app.get("/api/v1/frontend/supreme/contact")
def supreme_contact_frontend():
    if not CONTACT_HTML_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME CONTACT page not found")
    return FileResponse(CONTACT_HTML_FILE, media_type="text/html", headers={"Cache-Control": "no-cache"})


@app.get("/api/v1/frontend/supreme/contact/style.css")
def supreme_contact_frontend_css():
    if not CONTACT_CSS_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME CONTACT CSS not found")
    return FileResponse(CONTACT_CSS_FILE, media_type="text/css")


@app.get("/api/v1/frontend/supreme/contact/script.js")
def supreme_contact_frontend_js():
    if not CONTACT_JS_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME CONTACT JavaScript not found")
    return FileResponse(CONTACT_JS_FILE, media_type="application/javascript")


@app.get("/api/v1/frontend/supreme/health")
def supreme_frontend_health():

    return {
        "success": True,
        "service": "SUPREMESETUHUB",
        "frontend": "supreme",
        "html": SUPREME_HTML_FILE.is_file(),
        "css": SUPREME_CSS_FILE.is_file(),
        "javascript": SUPREME_JS_FILE.is_file(),
    }


# ============================================================
# SUPREME ECOSYSTEM FRONTEND
# ============================================================

@app.get("/api/v1/frontend/supreme-ecosystem")
def supreme_ecosystem_frontend():
    if not SUPREME_ECOSYSTEM_HTML_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME ECOSYSTEM frontend HTML not found")
    return FileResponse(SUPREME_ECOSYSTEM_HTML_FILE, media_type="text/html")


@app.get("/api/v1/frontend/supreme-ecosystem/style.css")
def supreme_ecosystem_frontend_css():
    if not SUPREME_ECOSYSTEM_CSS_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME ECOSYSTEM frontend CSS not found")
    return FileResponse(SUPREME_ECOSYSTEM_CSS_FILE, media_type="text/css")


@app.get("/api/v1/frontend/supreme-ecosystem/script.js")
def supreme_ecosystem_frontend_js():
    if not SUPREME_ECOSYSTEM_JS_FILE.is_file():
        raise HTTPException(status_code=404, detail="SUPREME ECOSYSTEM frontend JavaScript not found")
    return FileResponse(SUPREME_ECOSYSTEM_JS_FILE, media_type="application/javascript")


@app.get("/api/v1/frontend/supreme-ecosystem/health")
def supreme_ecosystem_frontend_health():
    return {
        "success": True,
        "service": "SUPREMESETUHUB",
        "frontend": "supreme-ecosystem",
        "html": SUPREME_ECOSYSTEM_HTML_FILE.is_file(),
        "css": SUPREME_ECOSYSTEM_CSS_FILE.is_file(),
        "javascript": SUPREME_ECOSYSTEM_JS_FILE.is_file(),
    }


# ============================================================
# GLOBAL BUSINESS ECOSYSTEM FRONTEND
# ============================================================

@app.get("/api/v1/frontend/global-business-ecosystem")
def global_business_ecosystem_frontend():
    """Public WordPress-friendly alias for the main ecosystem homepage."""
    if not ROOT_FRONTEND_FILE.is_file():
        raise HTTPException(
            status_code=404,
            detail="Global business ecosystem frontend HTML not found",
        )
    return FileResponse(ROOT_FRONTEND_FILE, media_type="text/html")


@app.get("/api/v1/frontend/global-business-ecosystem/health")
def global_business_ecosystem_frontend_health():
    return {
        "success": True,
        "service": "SUPREMESETUHUB",
        "frontend": "global-business-ecosystem",
        "html": ROOT_FRONTEND_FILE.is_file(),
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

@app.get("/api/v1/wordpress/status/{site_id}")
def wordpress_status(site_id: str, request: Request):

    require_wordpress_owner(request.headers.get("authorization"))
    return wordpress_service.connection_status(site_id)


@app.get("/api/v1/wordpress/health/{site_id}")
def wordpress_health(site_id: str, request: Request):
    require_wordpress_owner(request.headers.get("authorization"))
    # Each WordPress gate has its own hosting database credentials.
    # Shared platform/customer data remains in SUPREME_DB_PATH.
    environment_prefixes = {
        "rajeshkhandelwalofficial": "WORDPRESS",
        "drrajeshkhandelwalibc": "WORDPRESS_IBC",
    }
    environment_prefix = environment_prefixes.get(site_id)
    if environment_prefix is None:
        return {
            "success": False,
            "status": "UNKNOWN_SITE",
            "site_id": site_id,
        }

    result = wordpress_service.connect_site(
        site_id=site_id,
        environment_prefix=environment_prefix,
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
