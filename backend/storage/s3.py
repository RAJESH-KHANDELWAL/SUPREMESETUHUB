"""Private AWS S3 object storage adapter for SUPREME shared storage.

The bucket must be private and credentials must come from the AWS default
credential chain (environment, workload role, or instance role). Never commit
credentials. Objects are uploaded with SHA-256 metadata and server-side
encryption enabled.
"""
from __future__ import annotations

import hashlib
import os
import tempfile
from uuid import uuid4
from io import BytesIO
from typing import BinaryIO


class S3StorageConfigurationError(RuntimeError):
    """Raised when AWS S3 storage is not configured or reachable."""


class S3ObjectStorage:
    def __init__(self, *, bucket: str | None = None, region: str | None = None, client=None):
        self.bucket = (bucket or os.getenv("AWS_S3_BUCKET", "")).strip()
        self.region = (region or os.getenv("AWS_REGION", "") or os.getenv("AWS_DEFAULT_REGION", "") or "us-east-1").strip()
        self._client = client
        self._client_error_types = ()
        if self._client is None and self.bucket:
            try:
                import boto3
                from botocore.exceptions import BotoCoreError, ClientError
                self._client = boto3.client("s3", region_name=self.region)
                self._client_error_types = (BotoCoreError, ClientError)
            except ImportError:
                self._client = None

    def health(self) -> dict:
        if not self.bucket:
            return {"configured": False, "writable": False, "connected": False, "status": "NOT_CONFIGURED", "backend": "AWS_S3"}
        if self._client is None:
            return {"configured": True, "writable": False, "connected": False, "status": "AWS_SDK_UNAVAILABLE", "backend": "AWS_S3"}
        probe_key = f".supreme-health-check/{uuid4().hex}"
        try:
            self._client.head_bucket(Bucket=self.bucket)
            # Confirm write + delete permissions with a tiny temporary object.
            self._client.put_object(
                Bucket=self.bucket, Key=probe_key, Body=b"ok",
                ServerSideEncryption="AES256",
            )
            self._client.delete_object(Bucket=self.bucket, Key=probe_key)
            return {"configured": True, "writable": True, "connected": True, "status": "READY", "backend": "AWS_S3", "bucket": self.bucket, "region": self.region}
        except Exception:
            # Do not expose cloud error details, bucket existence, or credentials.
            try:
                self._client.delete_object(Bucket=self.bucket, Key=probe_key)
            except Exception:
                pass
            return {"configured": True, "writable": False, "connected": False, "status": "AWS_S3_CONNECTION_FAILED", "backend": "AWS_S3", "bucket": self.bucket, "region": self.region}

    @staticmethod
    def _validate_key(storage_key: str) -> str:
        key = str(storage_key or "").replace("\\", "/")
        parts = key.split("/")
        if not key or key.startswith("/") or any(part in {"", ".", ".."} for part in parts):
            raise ValueError("INVALID_STORAGE_KEY")
        return key

    def save_stream_at_key(self, stream: BinaryIO, storage_key: str, max_bytes: int | None = None) -> tuple[int, str]:
        key = self._validate_key(storage_key)
        if not self.health()["writable"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        size = 0
        digest = hashlib.sha256()
        # Spool to disk to avoid loading an entire user upload into memory.
        with tempfile.TemporaryFile(mode="w+b") as body:
            while True:
                chunk = stream.read(1024 * 1024)
                if not chunk:
                    break
                size += len(chunk)
                if max_bytes is not None and size > max_bytes:
                    raise ValueError("MAX_UPLOAD_SIZE_EXCEEDED")
                body.write(chunk)
                digest.update(chunk)
            checksum = digest.hexdigest()
            body.seek(0)
            self._client.put_object(
                Bucket=self.bucket,
                Key=key,
                Body=body,
                Metadata={"sha256": checksum},
                ServerSideEncryption="AES256",
            )
        return size, checksum

    def open_key(self, storage_key: str):
        key = self._validate_key(storage_key)
        if not self.health()["writable"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        response = self._client.get_object(Bucket=self.bucket, Key=key)
        return BytesIO(response["Body"].read())

    def exists_key(self, storage_key: str) -> bool:
        key = self._validate_key(storage_key)
        if not self.health()["writable"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        try:
            self._client.head_object(Bucket=self.bucket, Key=key)
            return True
        except Exception as exc:
            # A missing object is false; authorization/network errors fail closed.
            response = getattr(exc, "response", {}) or {}
            code = str(response.get("Error", {}).get("Code", ""))
            if code in {"404", "NoSuchKey", "NotFound"}:
                return False
            raise RuntimeError("AWS_S3_OBJECT_CHECK_FAILED") from exc

    def copy_key(self, source_storage_key: str, target_storage_key: str) -> tuple[int, str]:
        source = self._validate_key(source_storage_key)
        target = self._validate_key(target_storage_key)
        if not self.health()["writable"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        head = self._client.head_object(Bucket=self.bucket, Key=source)
        self._client.copy_object(
            Bucket=self.bucket,
            Key=target,
            CopySource={"Bucket": self.bucket, "Key": source},
            MetadataDirective="COPY",
            ServerSideEncryption="AES256",
        )
        metadata = head.get("Metadata", {})
        checksum = metadata.get("sha256", "")
        if not checksum:
            with self.open_key(target) as handle:
                digest = hashlib.sha256()
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
                checksum = digest.hexdigest()
        return int(head.get("ContentLength", 0)), checksum

    def delete_key(self, storage_key: str) -> bool:
        key = self._validate_key(storage_key)
        if not self.health()["writable"]:
            raise RuntimeError("STORAGE_BACKEND_NOT_CONFIGURED_OR_WRITABLE")
        existed = self.exists_key(key)
        if existed:
            self._client.delete_object(Bucket=self.bucket, Key=key)
        return existed
