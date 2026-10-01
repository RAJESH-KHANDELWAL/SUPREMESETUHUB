from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
import httpx


router = APIRouter(
    prefix="/api/v1/theme-hub",
    tags=["THEME HUB"],
)


WORDPRESS_THEMES_API = (
    "https://api.wordpress.org/themes/info/1.2/"
)


@router.get("/themes")
async def get_themes(
    search: str = Query(
        default="",
        max_length=100
    ),
    page: int = Query(
        default=1,
        ge=1,
        le=100
    ),
    per_page: int = Query(
        default=24,
        ge=1,
        le=100
    ),
    browse: str = Query(
        default="popular"
    ),
):

    params = {
        "action": "query_themes",
        "request[page]": page,
        "request[per_page]": per_page,
        "request[browse]": browse,
        "request[fields][description]": "true",
        "request[fields][download_link]": "true",
        "request[fields][homepage]": "true",
        "request[fields][screenshot_url]": "true",
        "request[fields][tags]": "true",
    }


    if search.strip():

        params[
            "request[search]"
        ] = search.strip()


    try:

        async with httpx.AsyncClient(
            timeout=20.0,
            follow_redirects=True
        ) as client:

            response = await client.get(
                WORDPRESS_THEMES_API,
                params=params
            )


        response.raise_for_status()

        data = response.json()


    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail={
                "code": "WORDPRESS_THEME_API_ERROR",
                "message": str(error),
            }
        )


    themes = []


    for theme in data.get(
        "themes",
        []
    ):

        themes.append({

            "name":
                theme.get(
                    "name",
                    ""
                ),

            "slug":
                theme.get(
                    "slug",
                    ""
                ),

            "version":
                theme.get(
                    "version",
                    ""
                ),

            "author":
                theme.get(
                    "author",
                    ""
                ),

            "description":
                theme.get(
                    "description",
                    ""
                ),

            "screenshot":
                theme.get(
                    "screenshot_url",
                    ""
                ),

            "preview_url":
                theme.get(
                    "preview_url",
                    ""
                ),

            "homepage":
                theme.get(
                    "homepage",
                    ""
                ),

            "download_url":
                theme.get(
                    "download_link",
                    ""
                ),

            "active_installs":
                theme.get(
                    "active_installs",
                    0
                ),

            "rating":
                theme.get(
                    "rating",
                    0
                ),

            "num_ratings":
                theme.get(
                    "num_ratings",
                    0
                ),

        })


    info = data.get(
        "info",
        {}
    )


    return {

        "success": True,

        "source":
            "WORDPRESS.ORG",

        "page":
            info.get(
                "page",
                page
            ),

        "pages":
            info.get(
                "pages",
                1
            ),

        "total":
            info.get(
                "results",
                len(themes)
            ),

        "count":
            len(themes),

        "themes":
            themes,

    }


@router.get("/themes/{theme_slug}")
async def get_theme(
    theme_slug: str
):

    if not theme_slug.strip():

        raise HTTPException(
            status_code=400,
            detail="THEME_SLUG_REQUIRED"
        )


    params = {

        "action":
            "theme_information",

        "request[slug]":
            theme_slug.strip(),

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


    try:

        async with httpx.AsyncClient(
            timeout=20.0,
            follow_redirects=True
        ) as client:

            response = await client.get(
                WORDPRESS_THEMES_API,
                params=params
            )


        response.raise_for_status()

        data = response.json()


    except Exception as error:

        raise HTTPException(
            status_code=502,
            detail={
                "code":
                    "WORDPRESS_THEME_INFO_API_ERROR",

                "message":
                    str(error),
            }
        )


    if (
        not data
        or data.get("error")
    ):

        raise HTTPException(
            status_code=404,
            detail="THEME_NOT_FOUND"
        )


    return {

        "success": True,

        "source":
            "WORDPRESS.ORG",

        "theme":
            data,

    }


@router.get(
    "/themes/{theme_slug}/download"
)
async def download_theme(
    theme_slug: str
):

    if not theme_slug.strip():

        raise HTTPException(
            status_code=400,
            detail="THEME_SLUG_REQUIRED"
        )


    download_url = (
        "https://downloads.wordpress.org/theme/"
        + theme_slug.strip()
        + ".latest-stable.zip"
    )


    return RedirectResponse(
        url=download_url,
        status_code=307
    )
