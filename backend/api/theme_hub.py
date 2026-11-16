from pathlib import Path

import httpx

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse, RedirectResponse


router = APIRouter(
    prefix="/api/v1/theme-hub",
    tags=["THEME HUB"],
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

THEME_HUB_DIR = (
    BASE_DIR
    / "frontend"
    / "theme-hub"
)


# ============================================================
# WORDPRESS.ORG THEMES API
# ============================================================

WORDPRESS_THEMES_API = (
    "https://api.wordpress.org/themes/info/1.2/"
)


WORDPRESS_THEME_DOWNLOAD_URL = (
    "https://downloads.wordpress.org/theme/"
)


# ============================================================
# THEME HUB FRONTEND
# ============================================================

@router.get("/frontend")
def theme_hub_frontend():

    index_file = (
        THEME_HUB_DIR
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


@router.get("/frontend/style.css")
def theme_hub_css():

    css_file = (
        THEME_HUB_DIR
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


@router.get("/frontend/script.js")
def theme_hub_js():

    js_file = (
        THEME_HUB_DIR
        / "script.js"
    )

    if not js_file.is_file():

        raise HTTPException(
            status_code=404,
            detail="THEME_HUB_JS_NOT_FOUND",
        )

    return FileResponse(
        js_file,
        media_type="application/javascript",
    )


# ============================================================
# LIVE WORDPRESS.ORG THEME LIST
# ============================================================

@router.get("/themes")
async def get_themes(

    search: str = Query(
        default="",
        max_length=100,
    ),

    page: int = Query(
        default=1,
        ge=1,
        le=100,
    ),

    per_page: int = Query(
        default=24,
        ge=1,
        le=100,
    ),

    browse: str = Query(
        default="popular",
        max_length=50,
    ),
):

    params = {

        "action":
            "query_themes",

        "request[page]":
            page,

        "request[per_page]":
            per_page,

        "request[browse]":
            browse,

        "request[fields][description]":
            "true",

        "request[fields][download_link]":
            "true",

        "request[fields][homepage]":
            "true",

        "request[fields][screenshot_url]":
            "true",

        "request[fields][tags]":
            "true",

    }


    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    if search.strip():

        params[
            "request[search]"
        ] = search.strip()


    # --------------------------------------------------------
    # REQUEST WORDPRESS.ORG
    # --------------------------------------------------------

    try:

        async with httpx.AsyncClient(
            timeout=20.0,
            follow_redirects=True,
        ) as client:

            response = await client.get(
                WORDPRESS_THEMES_API,
                params=params,
            )

            response.raise_for_status()

            data = response.json()


    except httpx.HTTPError as error:

        raise HTTPException(
            status_code=502,
            detail={
                "code":
                    "WORDPRESS_THEME_API_ERROR",

                "message":
                    str(error),
            },
        )


    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail={
                "code":
                    "THEME_API_REQUEST_FAILED",

                "message":
                    str(error),
            },
        )


    # --------------------------------------------------------
    # WORDPRESS API ERROR
    # --------------------------------------------------------

    if isinstance(data, dict) and data.get("error"):

        raise HTTPException(
            status_code=502,
            detail={
                "code":
                    "WORDPRESS_THEME_API_RESPONSE_ERROR",

                "message":
                    data.get(
                        "error",
                        "Unknown WordPress.org error",
                    ),
            },
        )


    # --------------------------------------------------------
    # NORMALIZE THEMES
    # --------------------------------------------------------

    themes = []


    for theme in data.get(
        "themes",
        [],
    ):

        themes.append({

            "name":
                theme.get(
                    "name",
                    "",
                ),

            "slug":
                theme.get(
                    "slug",
                    "",
                ),

            "version":
                theme.get(
                    "version",
                    "",
                ),

            "author":
                theme.get(
                    "author",
                    "",
                ),

            "description":
                theme.get(
                    "description",
                    "",
                ),

            "screenshot":
                theme.get(
                    "screenshot_url",
                    "",
                ),

            "preview_url":
                theme.get(
                    "preview_url",
                    "",
                ),

            "homepage":
                theme.get(
                    "homepage",
                    "",
                ),

            "download_url":
                theme.get(
                    "download_link",
                    "",
                ),

            "active_installs":
                theme.get(
                    "active_installs",
                    0,
                ),

            "rating":
                theme.get(
                    "rating",
                    0,
                ),

            "num_ratings":
                theme.get(
                    "num_ratings",
                    0,
                ),

            "tags":
                theme.get(
                    "tags",
                    [],
                ),

        })


    # --------------------------------------------------------
    # WORDPRESS API INFO
    # --------------------------------------------------------

    info = data.get(
        "info",
        {},
    )


    return {

        "success":
            True,

        "source":
            "WORDPRESS.ORG",

        "search":
            search.strip(),

        "browse":
            browse,

        "page":
            info.get(
                "page",
                page,
            ),

        "pages":
            info.get(
                "pages",
                1,
            ),

        "total":
            info.get(
                "results",
                len(themes),
            ),

        "count":
            len(themes),

        "themes":
            themes,

    }


# ============================================================
# SINGLE THEME DETAILS
# ============================================================

@router.get("/themes/{theme_slug}")
async def get_theme(
    theme_slug: str,
):

    theme_slug = theme_slug.strip()


    if not theme_slug:

        raise HTTPException(
            status_code=400,
            detail="THEME_SLUG_REQUIRED",
        )


    params = {

        "action":
            "theme_information",

        "request[slug]":
            theme_slug,

        "request[fields][description]":
            "true",

        "request[fields][download_link]":
            "true",

        "request[fields][homepage]":
            "true",

        "request[fields][screenshot_url]":
            "true",

        "request[fields][tags]":
            "true",

    }


    # --------------------------------------------------------
    # REQUEST WORDPRESS.ORG
    # --------------------------------------------------------

    try:

        async with httpx.AsyncClient(
            timeout=20.0,
            follow_redirects=True,
        ) as client:

            response = await client.get(
                WORDPRESS_THEMES_API,
                params=params,
            )

            response.raise_for_status()

            data = response.json()


    except httpx.HTTPError as error:

        raise HTTPException(
            status_code=502,
            detail={
                "code":
                    "WORDPRESS_THEME_INFO_API_ERROR",

                "message":
                    str(error),
            },
        )


    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail={
                "code":
                    "THEME_INFO_REQUEST_FAILED",

                "message":
                    str(error),
            },
        )


    # --------------------------------------------------------
    # THEME NOT FOUND
    # --------------------------------------------------------

    if not data:

        raise HTTPException(
            status_code=404,
            detail="THEME_NOT_FOUND",
        )


    if isinstance(data, dict) and data.get("error"):

        raise HTTPException(
            status_code=404,
            detail="THEME_NOT_FOUND",
        )


    return {

        "success":
            True,

        "source":
            "WORDPRESS.ORG",

        "theme":
            data,

    }


# ============================================================
# THEME DOWNLOAD / CONNECT URL
# ============================================================

@router.get(
    "/themes/{theme_slug}/download"
)
async def download_theme(
    theme_slug: str,
):

    theme_slug = theme_slug.strip()


    if not theme_slug:

        raise HTTPException(
            status_code=400,
            detail="THEME_SLUG_REQUIRED",
        )


    download_url = (
        WORDPRESS_THEME_DOWNLOAD_URL
        + theme_slug
        + ".latest-stable.zip"
    )


    return RedirectResponse(
        url=download_url,
        status_code=307,
    )
