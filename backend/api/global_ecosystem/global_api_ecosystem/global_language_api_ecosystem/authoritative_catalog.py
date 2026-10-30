"""Optional source-backed language catalog readers.

The application never downloads third-party datasets at request time. Operators
must obtain source files from their official publishers, review the applicable
terms, and configure local file paths through environment variables.

Environment variables:
- GLOBAL_LANGUAGE_ISO6393_PATH: path to the official ISO 639-3 tab-delimited code set.
- GLOBAL_LANGUAGE_CLDR_LOCALES_PATH: path to Unicode CLDR availableLocales.json.

ISO 639-3 source: https://iso639-3.sil.org/code_tables/download_tables
Unicode CLDR JSON: https://github.com/unicode-org/cldr-json
"""
from __future__ import annotations

import csv
import json
import os
from pathlib import Path
from typing import Any

ISO6393_ENV = "GLOBAL_LANGUAGE_ISO6393_PATH"
CLDR_ENV = "GLOBAL_LANGUAGE_CLDR_LOCALES_PATH"

SOURCE_METADATA = {
    "iso639_3": {
        "publisher": "ISO 639-3 Registration Authority (SIL)",
        "url": "https://iso639-3.sil.org/code_tables/download_tables",
        "format": "UTF-8 tab-delimited code set",
        "environment_variable": ISO6393_ENV,
        "notes": "Use the official current code table and preserve identifiers exactly.",
    },
    "cldr": {
        "publisher": "Unicode Consortium",
        "url": "https://github.com/unicode-org/cldr-json",
        "format": "availableLocales.json",
        "environment_variable": CLDR_ENV,
        "notes": "Use CLDR locale identifiers; locale availability is not provider API support.",
    },
}


def _configured_path(env_name: str) -> Path | None:
    raw = os.environ.get(env_name, "").strip()
    return Path(raw).expanduser() if raw else None


def get_authoritative_catalog_status() -> dict[str, Any]:
    """Report whether optional source datasets are configured and readable."""
    result: dict[str, Any] = {}
    for key, metadata in SOURCE_METADATA.items():
        path = _configured_path(metadata["environment_variable"])
        readable = bool(path and path.is_file() and os.access(path, os.R_OK))
        result[key] = {
            **metadata,
            "status": "READY" if readable else "NOT_CONFIGURED",
            "configured": bool(path),
            "readable": readable,
        }
    return {
        "catalog_mode": "LOCAL_SOURCE_FILES_OPTIONAL",
        "built_in_catalog_status": "CURATED_STARTER",
        "sources": result,
        "iso639_3": result["iso639_3"],
        "cldr": result["cldr"],
        "live_provider_integrations": False,
    }


def list_iso6393_languages(query: str | None = None, limit: int = 100) -> list[dict[str, str]]:
    """Search a locally configured ISO 639-3 tab-delimited code table."""
    path = _configured_path(ISO6393_ENV)
    if not path or not path.is_file():
        return []

    needle = (query or "").strip().casefold()
    cap = max(1, min(int(limit), 250))
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\\t")
        required = {"Id", "Ref_Name"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError("ISO 639-3 table is missing required Id or Ref_Name columns")
        for source_row in reader:
            code = (source_row.get("Id") or "").strip()
            name = (source_row.get("Ref_Name") or "").strip()
            if not code or not name:
                continue
            if needle and needle not in code.casefold() and needle not in name.casefold():
                continue
            rows.append({
                "id": code,
                "name": name,
                "scope": (source_row.get("Scope") or "").strip(),
                "language_type": (source_row.get("Language_Type") or "").strip(),
                "source": "ISO 639-3",
            })
            if len(rows) >= cap:
                break
    return rows


def list_cldr_locales(query: str | None = None, limit: int = 100) -> list[dict[str, str]]:
    """Search locale identifiers in a locally configured CLDR availableLocales.json."""
    path = _configured_path(CLDR_ENV)
    if not path or not path.is_file():
        return []

    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    available = payload.get("availableLocales", {})
    locale_ids = available.get("full", [])
    if not isinstance(locale_ids, list):
        raise ValueError("CLDR availableLocales.json has an invalid availableLocales.full list")

    needle = (query or "").strip().casefold()
    cap = max(1, min(int(limit), 250))
    results = []
    for locale_id in locale_ids:
        if isinstance(locale_id, str) and (not needle or needle in locale_id.casefold()):
            results.append({"id": locale_id, "source": "Unicode CLDR"})
            if len(results) >= cap:
                break
    return results
