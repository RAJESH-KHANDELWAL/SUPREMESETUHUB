"""Safe, provider-neutral backup manifest and integrity verification.

This module inventories files and verifies their SHA-256 digests. It does not
copy data, contact storage providers, encrypt files, or schedule backup jobs.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Iterable

MANIFEST_VERSION = 1
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def _safe_relative_path(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        raise ValueError("Manifest paths must be non-empty strings.")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise ValueError(f"Unsafe relative path: {value!r}")
    if "\\" in value:
        raise ValueError("Manifest paths must use POSIX separators.")
    return path


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(
    source_root: str | Path,
    relative_paths: Iterable[str],
    *,
    created_at: str | None = None,
) -> dict:
    """Build a sorted manifest for explicitly selected files under source_root."""
    root = Path(source_root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("source_root must be a directory.")

    entries = []
    seen = set()
    for raw_path in relative_paths:
        relative = _safe_relative_path(raw_path)
        normalized = relative.as_posix()
        if normalized in seen:
            raise ValueError(f"Duplicate manifest path: {normalized}")
        seen.add(normalized)

        candidate = root.joinpath(*relative.parts)
        if candidate.is_symlink():
            raise ValueError(f"Symbolic links are not accepted: {normalized}")
        resolved = candidate.resolve(strict=True)
        if not resolved.is_relative_to(root):
            raise ValueError(f"Path escapes source_root: {normalized}")
        if not resolved.is_file():
            raise ValueError(f"Manifest entry is not a regular file: {normalized}")

        entries.append({
            "path": normalized,
            "size_bytes": resolved.stat().st_size,
            "sha256": _sha256_file(resolved),
        })

    entries.sort(key=lambda item: item["path"])
    timestamp = created_at or datetime.now(timezone.utc).isoformat()
    return {
        "manifest_version": MANIFEST_VERSION,
        "algorithm": "sha256",
        "created_at": timestamp,
        "files": entries,
    }


def verify_manifest(source_root: str | Path, manifest: dict) -> dict:
    """Verify manifest structure, file presence, sizes, and SHA-256 digests."""
    root = Path(source_root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("source_root must be a directory.")
    if not isinstance(manifest, dict) or manifest.get("manifest_version") != MANIFEST_VERSION:
        raise ValueError("Unsupported or invalid manifest version.")
    if manifest.get("algorithm") != "sha256":
        raise ValueError("Unsupported manifest checksum algorithm.")
    files = manifest.get("files")
    if not isinstance(files, list):
        raise ValueError("Manifest files must be a list.")

    errors = []
    verified = 0
    seen = set()
    for index, entry in enumerate(files):
        if not isinstance(entry, dict):
            errors.append(f"entry[{index}]: invalid entry")
            continue
        try:
            relative = _safe_relative_path(entry.get("path"))
        except ValueError as exc:
            errors.append(f"entry[{index}]: {exc}")
            continue

        normalized = relative.as_posix()
        if normalized in seen:
            errors.append(f"{normalized}: duplicate manifest entry")
            continue
        seen.add(normalized)
        expected_digest = entry.get("sha256")
        expected_size = entry.get("size_bytes")
        if not isinstance(expected_digest, str) or not _SHA256_RE.fullmatch(expected_digest):
            errors.append(f"{normalized}: invalid SHA-256 digest")
            continue
        if isinstance(expected_size, bool) or not isinstance(expected_size, int) or expected_size < 0:
            errors.append(f"{normalized}: invalid size_bytes")
            continue

        candidate = root.joinpath(*relative.parts)
        if candidate.is_symlink():
            errors.append(f"{normalized}: symbolic link is not accepted")
            continue
        try:
            resolved = candidate.resolve(strict=True)
        except FileNotFoundError:
            errors.append(f"{normalized}: missing file")
            continue
        if not resolved.is_relative_to(root) or not resolved.is_file():
            errors.append(f"{normalized}: path is outside root or not a regular file")
            continue
        actual_size = resolved.stat().st_size
        if actual_size != expected_size:
            errors.append(f"{normalized}: size mismatch (expected {expected_size}, got {actual_size})")
            continue
        actual_digest = _sha256_file(resolved)
        if actual_digest != expected_digest:
            errors.append(f"{normalized}: SHA-256 mismatch")
            continue
        verified += 1

    return {
        "valid": not errors,
        "verified_files": verified,
        "total_files": len(files),
        "errors": errors,
    }


def write_manifest(manifest: dict, destination: str | Path) -> Path:
    """Write a manifest as JSON; callers must choose a protected destination."""
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.name + ".tmp")
    temporary.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(target)
    return target
