"""Verified MySQL/MariaDB logical backups for the central SUPREME database.

Requires the mysqldump client on the runtime host. Passwords are supplied via
MYSQL_PWD in the child process environment, never in command-line arguments.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from backend.database.gde_connection import SupremeDatabaseConfig


class DatabaseBackupManager:
    def __init__(
        self,
        config: SupremeDatabaseConfig | None = None,
        backup_dir: str | Path | None = None,
        executable: str = "mysqldump",
    ) -> None:
        self.config = config or SupremeDatabaseConfig.from_environment()
        self.backup_dir = Path(
            backup_dir or os.getenv("SUPREME_DB_BACKUP_DIR", "var/backups/database")
        ).expanduser().resolve()
        self.executable = executable

    def create_backup(self) -> dict[str, object]:
        self.config.validate()
        if not shutil.which(self.executable):
            raise RuntimeError("mysqldump executable is not installed on this runtime.")
        if not re.fullmatch(r"[A-Za-z0-9_]+", self.config.database):
            raise ValueError("Unsafe database identifier.")
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        target = (self.backup_dir / f"{self.config.database}-{stamp}.sql").resolve()
        if target.parent != self.backup_dir:
            raise ValueError("Backup path escaped the configured backup directory.")

        command = [
            self.executable,
            "--host", self.config.host,
            "--port", str(self.config.port),
            "--user", self.config.username,
            "--connect-timeout", str(self.config.connect_timeout),
            "--single-transaction",
            "--quick",
            "--routines",
            "--triggers",
            "--hex-blob",
            "--default-character-set=utf8mb4",
            "--result-file", str(target),
            self.config.database,
        ]
        env = os.environ.copy()
        env["MYSQL_PWD"] = self.config.password
        try:
            completed = subprocess.run(
                command, env=env, check=False, capture_output=True, text=True,
                timeout=max(60, self.config.connect_timeout * 12),
            )
            if completed.returncode != 0:
                target.unlink(missing_ok=True)
                raise RuntimeError(
                    "mysqldump failed (" + str(completed.returncode) + "): "
                    + (completed.stderr or "no diagnostic output")[:500]
                )
            if not target.is_file() or target.stat().st_size == 0:
                target.unlink(missing_ok=True)
                raise RuntimeError("mysqldump returned success but produced an empty backup.")
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            manifest = {
                "database": self.config.database,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "file": target.name,
                "size_bytes": target.stat().st_size,
                "sha256": digest,
                "tool": self.executable,
            }
            manifest_path = target.with_suffix(".manifest.json")
            manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            return {"success": True, **manifest, "manifest": manifest_path.name}
        except subprocess.TimeoutExpired as exc:
            target.unlink(missing_ok=True)
            raise RuntimeError("Database backup timed out.") from exc
