from __future__ import annotations

import json
import shutil
import zipfile
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/api/v1/theme-hub",
    tags=["THEME HUB"],
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

THEMES_DIR = BASE_DIR / "themes"
UPLOADED_THEMES_DIR = THEMES_DIR / "uploaded"
INSTALLED_THEMES_DIR = THEMES_DIR / "installed"

FRONTEND_DIR = BASE_DIR / "frontend" / "theme-hub"


# ============================================================
# DIRECTORY SETUP
# ============================================================

THEMES_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

UPLOADED_THEMES_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

INSTALLED_THEMES_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# ============================================================
# HELPERS
# ============================================================

def _safe_theme_id(theme_id: str) -> str:
    """
    Prevent path traversal and keep theme IDs filesystem-safe.
    """

    cleaned = "".join(
        character
        for character in theme_id
        if character.isalnum()
        or character in ("-", "_")
    )

    if not cleaned:
        raise HTTPException(
            status_code=400,
            detail="INVALID_THEME_ID",
        )

    return cleaned


def _theme_metadata(theme_dir: Path) -> dict:
    """
    Read theme.json when available.
    """

    theme_json = theme_dir / "theme.json"

    if not theme_json.is_file():
        return {
            "id": theme_dir.name,
            "name": theme_dir.name,
        }

    try:
        return json.loads(
            theme_json.read_text(
                encoding="utf-8"
            )
        )

    except Exception:
        return {
            "id": theme_dir.name,
            "name": theme_dir.name,
        }


def _find_theme_root(extract_dir: Path) -> Path:
    """
    Detect whether the ZIP contains the theme directly
    or inside one top-level folder.
    """

    direct_style = extract_dir / "style.css"

    if direct_style.is_file():
        return extract_dir

    directories = [
        item
        for item in extract_dir.iterdir()
        if item.is_dir()
    ]

    if len(directories) == 1:
        possible_root = directories[0]

        if (
            (possible_root / "style.css").is_file()
            or (possible_root / "theme.json").is_file()
        ):
            return possible_root

    return extract_dir


def _validate_theme_directory(theme_dir: Path) -> dict:
    """
    Validate common WordPress theme structure.

    This does not execute PHP.
    """

    style_css = theme_dir / "style.css"
    index_php = theme_dir / "index.php"
    functions_php = theme_dir / "functions.php"
    screenshot_png = theme_dir / "screenshot.png"
    screenshot_jpg = theme_dir / "screenshot.jpg"
    screenshot_jpeg = theme_dir / "screenshot.jpeg"
    theme_json = theme_dir / "theme.json"

    errors = []
    warnings = []

    if not style_css.is_file():
        errors.append(
            "style.css NOT FOUND"
        )

    if not index_php.is_file():
        warnings.append(
            "index.php NOT FOUND"
        )

    if not functions_php.is_file():
        warnings.append(
            "functions.php NOT FOUND"
        )

    screenshot_found = any(
        file.is_file()
        for file in (
            screenshot_png,
            screenshot_jpg,
            screenshot_jpeg,
        )
    )

    if not screenshot_found:
        warnings.append(
            "Theme screenshot NOT FOUND"
        )

    if theme_json.is_file():
        theme_type = "BLOCK / MODERN THEME"
    else:
        theme_type = "CLASSIC / STANDARD THEME"

    valid = len(errors) == 0

    return {
        "valid": valid,
        "theme_type": theme_type,
        "files": {
            "style.css": style_css.is_file(),
            "index.php": index_php.is_file(),
            "functions.php": functions_php.is_file(),
            "screenshot": screenshot_found,
            "theme.json": theme_json.is_file(),
        },
        "errors": errors,
        "warnings": warnings,
    }


# ============================================================
# EXISTING THEMES
# ============================================================

@router.get("/themes")
def get_themes():

    themes = []

    if not THEMES_DIR.exists():
        return {
            "success": True,
            "count": 0,
            "themes": [],
        }

    for theme_dir in THEMES_DIR.iterdir():

        if not theme_dir.is_dir():
            continue

        # Internal upload/install folders are not normal
        # theme listings.
        if theme_dir.name in {
            "uploaded",
            "installed",
        }:
            continue

        theme_json = theme_dir / "theme.json"

        if not theme_json.is_file():
            continue

        try:

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


# ============================================================
# THEME DETAILS
# ============================================================

@router.get("/themes/{theme_id}")
def get_theme(theme_id: str):

    theme_id = _safe_theme_id(theme_id)

    theme_dir = THEMES_DIR / theme_id
    theme_json = theme_dir / "theme.json"

    if not theme_json.is_file():
        raise HTTPException(
            status_code=404,
            detail="THEME_NOT_FOUND",
        )

    try:

        data = json.loads(
            theme_json.read_text(
                encoding="utf-8"
            )
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="THEME_METADATA_INVALID",
        )

    return {
        "success": True,
        "theme": data,
    }


# ============================================================
# THEME DOWNLOAD
# ============================================================

@router.get("/themes/{theme_id}/download")
def download_theme(theme_id: str):

    theme_id = _safe_theme_id(theme_id)

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


# ============================================================
# THEME UPLOAD
# ============================================================

@router.post("/upload")
async def upload_theme(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="THEME_FILE_REQUIRED",
        )

    original_name = Path(
        file.filename
    ).name

    if not original_name.lower().endswith(".zip"):
        raise HTTPException(
            status_code=400,
            detail="ONLY_THEME_ZIP_ALLOWED",
        )

    theme_id = Path(
        original_name
    ).stem

    theme_id = _safe_theme_id(
        theme_id
    )

    upload_dir = (
        UPLOADED_THEMES_DIR
        / theme_id
    )

    if upload_dir.exists():
        shutil.rmtree(
            upload_dir
        )

    upload_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    zip_path = (
        upload_dir
        / f"{theme_id}.zip"
    )

    try:

        with zip_path.open(
            "wb"
        ) as destination:

            while True:

                chunk = await file.read(
                    1024 * 1024
                )

                if not chunk:
                    break

                destination.write(
                    chunk
                )

    finally:

        await file.close()

    # --------------------------------------------------------
    # ZIP SAFETY CHECK
    # --------------------------------------------------------

    try:

        with zipfile.ZipFile(
            zip_path,
            "r",
        ) as archive:

            for member in archive.infolist():

                member_path = Path(
                    member.filename
                )

                if member_path.is_absolute():
                    raise HTTPException(
                        status_code=400,
                        detail="UNSAFE_THEME_ZIP",
                    )

                if ".." in member_path.parts:
                    raise HTTPException(
                        status_code=400,
                        detail="UNSAFE_THEME_ZIP",
                    )

            extract_dir = (
                upload_dir
                / "extracted"
            )

            extract_dir.mkdir(
                parents=True,
                exist_ok=True,
            )

            archive.extractall(
                extract_dir
            )

    except zipfile.BadZipFile:

        shutil.rmtree(
            upload_dir,
            ignore_errors=True,
        )

        raise HTTPException(
            status_code=400,
            detail="INVALID_THEME_ZIP",
        )

    # --------------------------------------------------------
    # DETECT THEME ROOT
    # --------------------------------------------------------

    theme_root = _find_theme_root(
        extract_dir
    )

    validation = (
        _validate_theme_directory(
            theme_root
        )
    )

    return {
        "success": True,
        "theme_id": theme_id,
        "filename": original_name,
        "validation": validation,
        "upload_directory": str(
            upload_dir
        ),
    }


# ============================================================
# THEME CHECK
# ============================================================

@router.get(
    "/check/{theme_id}"
)
def check_theme(theme_id: str):

    theme_id = _safe_theme_id(
        theme_id
    )

    upload_dir = (
        UPLOADED_THEMES_DIR
        / theme_id
    )

    extract_dir = (
        upload_dir
        / "extracted"
    )

    if not extract_dir.is_dir():
        raise HTTPException(
            status_code=404,
            detail="UPLOADED_THEME_NOT_FOUND",
        )

    theme_root = _find_theme_root(
        extract_dir
    )

    validation = (
        _validate_theme_directory(
            theme_root
        )
    )

    return {
        "success": True,
        "theme_id": theme_id,
        "validation": validation,
    }


# ============================================================
# INSTALL THEME INTO THEME HUB
# ============================================================

@router.post(
    "/install/{theme_id}"
)
def install_theme(theme_id: str):

    theme_id = _safe_theme_id(
        theme_id
    )

    upload_dir = (
        UPLOADED_THEMES_DIR
        / theme_id
    )

    extract_dir = (
        upload_dir
        / "extracted"
    )

    if not extract_dir.is_dir():
        raise HTTPException(
            status_code=404,
            detail="UPLOADED_THEME_NOT_FOUND",
        )

    theme_root = _find_theme_root(
        extract_dir
    )

    validation = (
        _validate_theme_directory(
            theme_root
        )
    )

    if not validation["valid"]:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "THEME_VALIDATION_FAILED",
                "validation": validation,
            },
        )

    installed_dir = (
        INSTALLED_THEMES_DIR
        / theme_id
    )

    if installed_dir.exists():
        shutil.rmtree(
            installed_dir
        )

    shutil.copytree(
        theme_root,
        installed_dir
    )

    return {
        "success": True,
        "theme_id": theme_id,
        "status": "INSTALLED",
        "validation": validation,
    }


# ============================================================
# INSTALLED THEMES
# ============================================================

@router.get("/installed")
def installed_themes():

    themes = []

    if not INSTALLED_THEMES_DIR.exists():
        return {
            "success": True,
            "count": 0,
            "themes": [],
        }

    for theme_dir in INSTALLED_THEMES_DIR.iterdir():

        if not theme_dir.is_dir():
            continue

        validation = (
            _validate_theme_directory(
                theme_dir
            )
        )

        themes.append(
            {
                "id": theme_dir.name,
                "name": theme_dir.name,
                "status": "INSTALLED",
                "validation": validation,
            }
        )

    return {
        "success": True,
        "count": len(themes),
        "themes": themes,
    }


# ============================================================
# INSTALLED THEME PREVIEW
# ============================================================

@router.get(
    "/preview/{theme_id}"
)
def preview_theme(theme_id: str):

    theme_id = _safe_theme_id(
        theme_id
    )

    theme_dir = (
        INSTALLED_THEMES_DIR
        / theme_id
    )

    if not theme_dir.is_dir():
        raise HTTPException(
            status_code=404,
            detail="INSTALLED_THEME_NOT_FOUND",
        )

    preview_file = (
        theme_dir
        / "index.html"
    )

    if not preview_file.is_file():

        preview_file = (
            theme_dir
            / "index.php"
        )

    if not preview_file.is_file():
        raise HTTPException(
            status_code=404,
            detail="THEME_PREVIEW_NOT_AVAILABLE",
        )

    # NOTE:
    # PHP is intentionally NOT executed by FastAPI.
    # HTML preview works directly.
    # PHP themes require a WordPress/PHP runtime.

    if preview_file.suffix.lower() == ".html":

        return FileResponse(
            preview_file,
            media_type="text/html",
        )

    raise HTTPException(
        status_code=501,
        detail=(
            "PHP_THEME_REQUIRES_WORDPRESS_RUNTIME"
        ),
    )


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
