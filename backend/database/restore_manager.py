"""Explicitly gated restore for a verified central SUPREME database backup.

Restore is destructive. It requires a deliberate confirmation phrase, validates
the backup path and SHA-256 manifest, and refuses the configured WordPress DB.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

from backend.database.gde_connection import SupremeDatabaseConfig


class DatabaseRestoreManager:
    CONFIRMATION = "RESTORE SUPREMESETUHUB"

    def __init__(
        self,
        config: SupremeDatabaseConfig | None = None,
        backup_dir: str | Path | None = None,
        executable: str = "mysql",
    ) -> None:
        self.config = config or SupremeDatabaseConfig.from_environment()
        self.backup_dir = Path(
            backup_dir or os.getenv("SUPREME_DB_BACKUP_DIR", "var/backups/database")
        ).expanduser().resolve()
        self.executable = executable

    def restore_backup(
        self,
        backup_file: str,
        *,
        confirmation: str,
    ) -> dict[str, object]:
        self.config.validate()
        if confirmation != self.CONFIRMATION:
            raise PermissionError("Exact restore confirmation phrase is required.")
        if not shutil.which(self.executable):
            raise RuntimeError("mysql client executable is not installed on this runtime.")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+\.sql", backup_file):
            raise ValueError("Invalid backup filename.")
        source = (self.backup_dir / backup_file).resolve()
        if source.parent != self.backup_dir or not source.is_file() or source.is_symlink():
            raise FileNotFoundError("Backup file is missing or outside the approved backup directory.")
        manifest_path = source.with_suffix(".manifest.json")
        if not manifest_path.is_file():
            raise ValueError("Backup manifest is missing; refusing an unverified restore.")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("database") != self.config.database:
            raise ValueError("Backup belongs to a different database.")
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != manifest.get("sha256"):
            raise ValueError("Backup SHA-256 verification failed.")
        wordpress_database = os.getenv("WORDPRESS_DB_NAME", "").strip()
        if wordpress_database and self.config.database.casefold() == wordpress_database.casefold():
            raise PermissionError("Restore is blocked for the WordPress database.")

        command = [
            self.executable,
            "--host", self.config.host,
            "--port", str(self.config.port),
            "--user", self.config.username,
            "--connect-timeout", str(self.config.connect_timeout),
            self.config.database,
        ]
        env = os.environ.copy()
        env["MYSQL_PWD"] = self.config.password
        with source.open("rb") as stream:
            completed = subprocess.run(
                command, env=env, stdin=stream, check=False, capture_output=True,
                timeout=max(120, self.config.connect_timeout * 30),
            )
        if completed.returncode != 0:
            raise RuntimeError(
                "mysql restore failed (" + str(completed.returncode) + "): "
                + (completed.stderr or b"no diagnostic output").decode("utf-8", "replace")[:500]
            )
        return {
            "success": True,
            "database": self.config.database,
            "backup_file": source.name,
            "sha256_verified": True,
            "restore_completed": True,
        }
