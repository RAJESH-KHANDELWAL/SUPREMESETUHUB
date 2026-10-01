from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/api/v1/theme-hub",
    tags=["THEME HUB"],
)

BASE_DIR = Path(__file__).resolve().parents[2]

THEMES_DIR = BASE_DIR / "themes"
FRONTEND_DIR = BASE_DIR / "frontend" / "theme-hub"


@router.get("/themes")
def get_themes():
    themes = []

    if not THEMES_DIR.exists():
        return {
            "success": True,
            "themes": [],
        }

    for theme_dir in THEMES_DIR.iterdir():

        if not theme_dir.is_dir():
            continue

        theme_json = theme_dir / "theme.json"

        if not theme_json.is_file():
            continue

        try:
            import json

            data = json.loads(
                theme_json.read_text(
                    encoding="utf-8"
                )
            )

            themes.append(data)

        except Exception:
            continue

    return {
        "success": True,
        "count": len(themes),
        "themes": themes,
    }


@router.get("/themes/{theme_id}")
def get_theme(theme_id: str):

    theme_dir = THEMES_DIR / theme_id
    theme_json = theme_dir / "theme.json"

    if not theme_json.is_file():
        raise HTTPException(
            status_code=404,
            detail="THEME_NOT_FOUND",
        )

    import json

    data = json.loads(
        theme_json.read_text(
            encoding="utf-8"
        )
    )

    return {
        "success": True,
        "theme": data,
    }


@router.get("/themes/{theme_id}/download")
def download_theme(theme_id: str):

    theme_dir = THEMES_DIR / theme_id

    zip_file = theme_dir / f"{theme_id}.zip"

    if not zip_file.is_file():
        raise HTTPException(
            status_code=404,
            detail="THEME_DOWNLOAD_NOT_FOUND",
        )

    return FileResponse(
        zip_file,
        media_type="application/zip",
        filename=f"{theme_id}.zip",
    )


@router.get("/frontend")
def theme_hub_frontend():

    index_file = FRONTEND_DIR / "index.html"

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

    css_file = FRONTEND_DIR / "style.css"

    if not css_file.is_file():
        raise HTTPException(
            status_code=404,
            detail="THEME_HUB_CSS_NOT_FOUND",
        )

    return FileResponse(
        css_file,
        media_type="text/css",
    )
