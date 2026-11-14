"""Scoped explicit-FTPS file uploader for Hostinger shared web hosting.

The deployer only writes beneath a configured site subdirectory. It uploads to
a temporary filename and swaps it into place with rollback protection. It never
performs a recursive clean-slate delete and refuses path traversal.
"""
from __future__ import annotations

import ftplib
import os
import posixpath
import ssl
import uuid
from pathlib import Path, PurePosixPath
from typing import Mapping

from .profiles import get_ftp_profile


class FtpDeploymentManager:
    def __init__(self, environ: Mapping[str, str] | None = None) -> None:
        self.environ = os.environ if environ is None else environ

    @staticmethod
    def _safe_relative_path(value: str) -> str:
        path = PurePosixPath(value.replace("\\", "/"))
        if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
            raise ValueError("Remote path must be a safe relative path beneath the FTP account root.")
        return str(path)

    def deploy_directory(
        self,
        profile_id: str,
        local_directory: str | Path,
        remote_subdirectory: str,
        *,
        allowed_subdirectory: str = "supremesetuhub",
    ) -> dict[str, object]:
        profile = get_ftp_profile(profile_id)
        values = profile.resolve(self.environ)
        if not values["configured"]:
            raise ValueError("FTP profile is not fully configured.")
        allowed = self._safe_relative_path(allowed_subdirectory)
        target = self._safe_relative_path(remote_subdirectory)
        if target != allowed and not target.startswith(allowed + "/"):
            raise PermissionError("Deployment target is outside the approved site subdirectory.")

        source = Path(local_directory).resolve()
        if not source.is_dir():
            raise NotADirectoryError(str(source))
        files = sorted(path for path in source.rglob("*") if path.is_file())
        if not files:
            raise ValueError("Refusing to deploy an empty directory.")
        for path in files:
            if path.is_symlink():
                raise ValueError("Symlinks are not allowed in deployment artifacts.")

        client = ftplib.FTP_TLS(context=ssl.create_default_context(), timeout=int(values["timeout"]))
        uploaded = 0
        try:
            client.connect(str(values["server"]), int(values["port"]), timeout=int(values["timeout"]))
            client.login(str(values["username"]), str(values["password"]))
            client.prot_p()
            for part in target.split("/"):
                try:
                    client.cwd(part)
                except ftplib.error_perm:
                    client.mkd(part)
                    client.cwd(part)
            for local_file in files:
                relative = local_file.relative_to(source).as_posix()
                remote_dir = posixpath.dirname(relative)
                for part in remote_dir.split("/") if remote_dir else []:
                    try:
                        client.cwd(part)
                    except ftplib.error_perm:
                        client.mkd(part)
                        client.cwd(part)
                final_name = posixpath.basename(relative)
                temporary_name = final_name + ".uploading"
                previous_name = final_name + ".previous-" + uuid.uuid4().hex
                with local_file.open("rb") as stream:
                    client.storbinary("STOR " + temporary_name, stream)

                had_previous = False
                try:
                    client.rename(final_name, previous_name)
                    had_previous = True
                except ftplib.error_perm:
                    pass
                try:
                    client.rename(temporary_name, final_name)
                except Exception:
                    if had_previous:
                        client.rename(previous_name, final_name)
                    raise
                if had_previous:
                    try:
                        client.delete(previous_name)
                    except ftplib.error_perm:
                        # Keep the prior copy if the server denies cleanup.
                        pass
                uploaded += 1
                for _ in remote_dir.split("/") if remote_dir else []:
                    client.cwd("..")
            for _ in target.split("/"):
                client.cwd("..")
            return {
                "success": True,
                "profile_id": profile.profile_id,
                "target": target,
                "files_uploaded": uploaded,
                "clean_slate": False,
                "remote_deletions": False,
                "credentials_returned": False,
            }
        finally:
            try:
                client.quit()
            except Exception:
                client.close()


__all__ = ["FtpDeploymentManager"]
