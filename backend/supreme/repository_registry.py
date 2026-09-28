
"""Repository role registry for the SUPREMESETUHUB central API."""

from __future__ import annotations

from copy import deepcopy

from supreme_config import CONNECTED_REPOS

ROLE_NAMES = ("SUPREME", "ADMIN", "OWNER")


def list_repository_roles() -> list[dict]:
    """Return each configured branch repository and its role slots."""
    rows = []

    for repo_key, repo in CONNECTED_REPOS.items():
        if repo_key == "SUPREMESETUHUB":
            continue

        rows.append({
            "repo_key": repo_key,
            "name": repo.get("name", repo_key),
            "owner": repo.get("owner"),
            "url": repo.get("url"),
            "homepage": repo.get("homepage"),
            "repo_type": repo.get("type"),
            "connection_status": repo.get("status", "UNKNOWN"),
            "roles": [
                {
                    "role": role,
                    "status": "UNCONFIGURED",
                    "identity": None,
                }
                for role in ROLE_NAMES
            ],
        })

    return rows


def get_repository_roles(repo_key: str) -> dict | None:
    """Return role slots for one branch repository."""
    key = repo_key.strip().upper()

    for row in list_repository_roles():
        if row["repo_key"].upper() == key:
            return deepcopy(row)

    return None
