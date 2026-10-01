from __future__ import annotations

import json
from typing import Optional

import httpx
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/api/v1/theme-hub",
    tags=["THEME HUB"],
)


# ============================================================
# WORDPRESS.ORG THEMES API
# ============================================================

WORDPRESS_THEMES_API = (
    "https://api.wordpress.org/themes/info/1.2/"
)

BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = BASE_DIR / "frontend" / "theme-hub"


# ============================================================
# WORDPRESS.ORG API REQUEST
# ============================================================

async def wordpress_themes_api(
    action: str,
    request_data: dict,
) -> dict:

    params = {
        "action": action,
        "request": json.dumps(
            request_data,
            separators=(",", ":"),
        ),
    }

    try:

        async with httpx.AsyncClient(
            timeout=20.0
        ) as client:

            response = await client.get(
                WORDPRESS_THEMES_API,
                params=params,
                headers={
                    "User-Agent": (
                        "SUPREMESETUHUB/1.0 "
                        "WordPress Theme Hub"
                    )
                },
            )

    except httpx.HTTPError as error:

        raise HTTPException(
            status_code=502,
            detail={
                "error": "WORDPRESS_THEMES_API_UNAVAILABLE",
                "message": str(error),
            },
        )

    if response.status_code != 200:

        raise HTTPException(
            status_code=502,
            detail={
                "error": "WORDPRESS_THEMES_API_ERROR",
                "status_code": response.status_code,
            },
        )

    try:

        return response.json()

    except Exception:

        raise HTTPException(
            status_code=502,
            detail="INVALID_WORDPRESS_THEMES_API_RESPONSE",
        )


# ============================================================
# SEARCH WORDPRESS.ORG THEMES
# ============================================================

@router.get("/themes")
async def get_themes(
    search: Optional[str] = Query(
        default=None
    ),
    page: int = Query(
        default=1,
        ge=1
    ),
    per_page: int = Query(
        default=24,
        ge=1,
        le=100
    ),
):

    request_data = {
        "per_page": per_page,
        "page": page,

        "fields": {
            "description": True,
            "downloadlink": True,
            "homepage": True,
            "last_updated": True,
            "rating": True,
            "ratings": True,
            "downloaded": True,
            "screenshot_url": True,
            "theme_url": True,
            "tags": True,
        },
    }

    if search:
        request_data["search"] = search

    data = await wordpress_themes_api(
        "query_themes",
        request_data,
    )

    themes = data.get(
        "themes",
        []
    )

    return {
        "success": True,
        "source": "WORDPRESS.ORG",
        "page": page,
        "per_page": per_page,
        "count": len(themes),
        "themes": themes,
    }


# ============================================================
# THEME INFORMATION
# ============================================================

@router.get("/themes/{theme_id}")
async def get_theme(
    theme_id: str
):

    request_data = {
        "slug": theme_id,

        "fields": {
            "description": True,
            "sections": True,
            "downloadlink": True,
            "homepage": True,
            "last_updated": True,
            "rating": True,
            "ratings": True,
            "downloaded": True,
            "screenshots": True,
            "screenshot_url": True,
            "theme_url": True,
            "tags": True,
            "versions": True,
            "template": True,
            "parent": True,
        },
    }

    data = await wordpress_themes_api(
        "theme_information",
        request_data,
    )

    if not data:

        raise HTTPException(
            status_code=404,
            detail="THEME_NOT_FOUND",
        )

    return {
        "success": True,
        "source": "WORDPRESS.ORG",
        "theme": data,
    }


# ============================================================
# OFFICIAL DOWNLOAD INFORMATION
# ============================================================

@router.get(
    "/themes/{theme_id}/download"
)
async def download_theme(
    theme_id: str
):

    request_data = {
        "slug": theme_id,

        "fields": {
            "downloadlink": True,
            "theme_url": True,
            "homepage": True,
        },
    }

    data = await wordpress_themes_api(
        "theme_information",
        request_data,
    )

    download_link = data.get(
        "download_link"
    )

    if not download_link:

        download_link = data.get(
            "downloadlink"
        )

    if not download_link:

        raise HTTPException(
            status_code=404,
            detail="OFFICIAL_THEME_DOWNLOAD_NOT_FOUND",
        )

    return {
        "success": True,
        "source": "WORDPRESS.ORG",
        "theme_id": theme_id,
        "theme_name": data.get(
            "name"
        ),
        "download_url": download_link,
        "theme_url": data.get(
            "theme_url"
        ),
        "homepage": data.get(
            "homepage"
        ),
    }


# ============================================================
# FEATURED THEMES
# ============================================================

@router.get("/featured")
async def featured_themes():

    request_data = {
        "browse": "featured",
        "per_page": 24,

        "fields": {
            "description": True,
            "downloadlink": True,
            "homepage": True,
            "last_updated": True,
            "rating": True,
            "screenshot_url": True,
            "theme_url": True,
        },
    }

    data = await wordpress_themes_api(
        "query_themes",
        request_data,
    )

    return {
        "success": True,
        "source": "WORDPRESS.ORG",
        "type": "featured",
        "count": len(
            data.get(
                "themes",
                []
            )
        ),
        "themes": data.get(
            "themes",
            []
        ),
    }


# ============================================================
# POPULAR THEMES
# ============================================================

@router.get("/popular")
async def popular_themes():

    request_data = {
        "browse": "popular",
        "per_page": 24,

        "fields": {
            "description": True,
            "downloadlink": True,
            "homepage": True,
            "last_updated": True,
            "rating": True,
            "screenshot_url": True,
            "theme_url": True,
        },
    }

    data = await wordpress_themes_api(
        "query_themes",
        request_data,
    )

    return {
        "success": True,
        "source": "WORDPRESS.ORG",
        "type": "popular",
        "count": len(
            data.get(
                "themes",
                []
            )
        ),
        "themes": data.get(
            "themes",
            []
        ),
    }


# ============================================================
# UPDATED THEMES
# ============================================================

@router.get("/updated")
async def updated_themes():

    request_data = {
        "browse": "updated",
        "per_page": 24,

        "fields": {
            "description": True,
            "downloadlink": True,
            "homepage": True,
            "last_updated": True,
            "rating": True,
            "screenshot_url": True,
            "theme_url": True,
        },
    }

    data = await wordpress_themes_api(
        "query_themes",
        request_data,
    )

    return {
        "success": True,
        "source": "WORDPRESS.ORG",
        "type": "updated",
        "count": len(
            data.get(
                "themes",
                []
            )
        ),
        "themes": data.get(
            "themes",
            []
        ),
    }


# ============================================================
# THEME HUB FRONTEND
# ============================================================

@router.get("/frontend")
def theme_hub_frontend():

    index_file = (
        FRONTEND_DIR
        / "index.html"
    )

    if not index_file.is_file():

        raise HTTPException(
            status_code=404,
            detail="THEME_HUB_FRONTEND_NOT_FOUND",
        )

    return FileResponse(
        index_file,
        media_type="text/html",
    )


# ============================================================
# THEME HUB CSS
# ============================================================

@router.get("/frontend/style.css")
def theme_hub_css():

    css_file = (
        FRONTEND_DIR
        / "style.css"
    )

    if not css_file.is_file():

        raise HTTPException(
            status_code=404,
            detail="THEME_HUB_CSS_NOT_FOUND",
        )

    return FileResponse(
        css_file,
        media_type="text/css",
    )
