"""Live API adapters for freelancer ecosystem external providers.

These adapters perform real provider API calls when invoked with authorized
credentials. They do not store access tokens. OAuth initiation/callback, encrypted
refresh-token vaulting, consent screens, and production credential provisioning
must be wired by the application before exposing user-facing connection flows.
"""
from __future__ import annotations

import os
from typing import Any
from urllib.parse import quote

import httpx


class ProviderConfigurationError(RuntimeError):
    """Raised when a required provider setting is missing."""


class ProviderRequestError(RuntimeError):
    """Raised when a provider API call fails."""


def _required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ProviderConfigurationError(f"CONFIGURATION_REQUIRED:{name}")
    return value


class GoogleDriveAdapter:
    """Google Drive REST API operations using a user-authorized OAuth access token."""

    base_url = "https://www.googleapis.com/drive/v3"

    @staticmethod
    def authorization_url(state: str, redirect_uri: str) -> str:
        from urllib.parse import urlencode

        client_id = _required_env("GOOGLE_CLIENT_ID")
        params = {
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "scope": "openid email https://www.googleapis.com/auth/drive.file",
            "access_type": "offline",
            "include_granted_scopes": "true",
            "state": state,
        }
        return "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode(params)

    @classmethod
    def list_files(cls, access_token: str, *, page_size: int = 25) -> dict[str, Any]:
        if not access_token.strip():
            raise ValueError("GOOGLE_ACCESS_TOKEN_REQUIRED")
        response = httpx.get(
            f"{cls.base_url}/files",
            headers={"Authorization": f"Bearer {access_token}"},
            params={
                "pageSize": max(1, min(page_size, 100)),
                "fields": "files(id,name,mimeType,modifiedTime,webViewLink),nextPageToken",
                "orderBy": "modifiedTime desc",
            },
            timeout=15.0,
        )
        if response.is_error:
            raise ProviderRequestError(f"GOOGLE_DRIVE_API_ERROR:{response.status_code}")
        return response.json()


class MicrosoftOneDriveAdapter:
    """Microsoft Graph OneDrive REST operations with delegated user access."""

    base_url = "https://graph.microsoft.com/v1.0"

    @staticmethod
    def authorization_url(state: str, redirect_uri: str) -> str:
        from urllib.parse import urlencode

        client_id = _required_env("MICROSOFT_CLIENT_ID")
        tenant = os.getenv("MICROSOFT_TENANT_ID", "common").strip() or "common"
        params = {
            "client_id": client_id,
            "response_type": "code",
            "redirect_uri": redirect_uri,
            "response_mode": "query",
            "scope": "openid profile email offline_access Files.ReadWrite",
            "state": state,
        }
        return f"https://login.microsoftonline.com/{quote(tenant, safe='')}/oauth2/v2.0/authorize?" + urlencode(params)

    @classmethod
    def list_root_children(cls, access_token: str, *, top: int = 25) -> dict[str, Any]:
        if not access_token.strip():
            raise ValueError("MICROSOFT_ACCESS_TOKEN_REQUIRED")
        response = httpx.get(
            f"{cls.base_url}/me/drive/root/children",
            headers={"Authorization": f"Bearer {access_token}"},
            params={"$top": max(1, min(top, 100)), "$select": "id,name,size,lastModifiedDateTime,webUrl,file,folder"},
            timeout=15.0,
        )
        if response.is_error:
            raise ProviderRequestError(f"MICROSOFT_GRAPH_API_ERROR:{response.status_code}")
        return response.json()


class AwsS3Adapter:
    """AWS S3 operations using boto3's standard credential chain or IAM role."""

    @staticmethod
    def list_objects(*, prefix: str = "", max_keys: int = 25) -> dict[str, Any]:
        import boto3
        from botocore.exceptions import BotoCoreError, ClientError

        bucket = _required_env("AWS_S3_BUCKET")
        region = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION") or None
        client = boto3.client("s3", region_name=region)
        try:
            result = client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefix,
                MaxKeys=max(1, min(max_keys, 1000)),
            )
        except (BotoCoreError, ClientError) as exc:
            # Do not return exception text that may contain request internals.
            raise ProviderRequestError("AWS_S3_LIST_FAILED") from exc
        return {
            "bucket": bucket,
            "key_count": int(result.get("KeyCount", 0)),
            "is_truncated": bool(result.get("IsTruncated", False)),
            "objects": [
                {
                    "key": item.get("Key"),
                    "size": item.get("Size"),
                    "last_modified": item.get("LastModified").isoformat()
                    if item.get("LastModified") else None,
                    "etag": item.get("ETag"),
                }
                for item in result.get("Contents", [])
            ],
        }


class AppleSignInAdapter:
    """Validate Sign in with Apple identity tokens against Apple's public keys."""

    issuer = "https://appleid.apple.com"
    jwks_url = "https://appleid.apple.com/auth/keys"

    @classmethod
    def verify_identity_token(cls, identity_token: str, *, audience: str | None = None) -> dict[str, Any]:
        if not identity_token.strip():
            raise ValueError("APPLE_IDENTITY_TOKEN_REQUIRED")
        client_id = audience or _required_env("APPLE_CLIENT_ID")
        try:
            import jwt
            jwks_client = jwt.PyJWKClient(cls.jwks_url, timeout=10)
            signing_key = jwks_client.get_signing_key_from_jwt(identity_token)
            claims = jwt.decode(
                identity_token,
                signing_key.key,
                algorithms=["RS256"],
                audience=client_id,
                issuer=cls.issuer,
                options={"require": ["exp", "iat", "sub", "iss", "aud"]},
                leeway=60,
            )
        except Exception as exc:
            # Keep token material and library internals out of API error messages.
            raise ProviderRequestError("APPLE_IDENTITY_TOKEN_INVALID") from exc
        return {
            "provider": "apple_sign_in",
            "subject": claims["sub"],
            "email": claims.get("email"),
            "email_verified": claims.get("email_verified"),
            "issuer": claims["iss"],
            "audience": claims["aud"],
        }
