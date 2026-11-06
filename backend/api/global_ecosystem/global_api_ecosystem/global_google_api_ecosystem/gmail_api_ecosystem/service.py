"""Single-mailbox Gmail API adapter using Google OAuth 2.0.

Tokens are stored outside the repository. Never commit OAuth credentials or tokens.
"""
from __future__ import annotations

import base64
import json
import os
from email.message import EmailMessage
from pathlib import Path
from typing import Any

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


class GmailConfigurationError(RuntimeError):
    pass


class GmailNotConnectedError(RuntimeError):
    pass


class GmailAPIService:
    """Gmail send adapter for one explicitly authorized Google mailbox."""

    def __init__(self, token_path: str | None = None) -> None:
        self.client_id = os.getenv("GOOGLE_CLIENT_ID", "").strip()
        self.client_secret = os.getenv("GOOGLE_CLIENT_SECRET", "").strip()
        self.redirect_uri = os.getenv("GOOGLE_GMAIL_REDIRECT_URI", os.getenv("GOOGLE_REDIRECT_URI", "")).strip()
        self.token_path = Path(token_path or os.getenv(
            "GOOGLE_GMAIL_TOKEN_PATH", "/var/lib/supremesetuhub/google/gmail/token.json"
        ))

    def _require_config(self) -> None:
        missing = [name for name, value in (
            ("GOOGLE_CLIENT_ID", self.client_id),
            ("GOOGLE_CLIENT_SECRET", self.client_secret),
            ("GOOGLE_GMAIL_REDIRECT_URI or GOOGLE_REDIRECT_URI", self.redirect_uri),
        ) if not value]
        if missing:
            raise GmailConfigurationError("Missing Google OAuth configuration: " + ", ".join(missing))

    def _flow(self, state: str | None = None):
        self._require_config()
        try:
            from google_auth_oauthlib.flow import Flow
        except ImportError as exc:
            raise GmailConfigurationError(
                "Install google-auth-oauthlib and google-api-python-client from backend/requirements.txt"
            ) from exc
        config = {"web": {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [self.redirect_uri],
        }}
        flow = Flow.from_client_config(config, scopes=SCOPES, state=state)
        flow.redirect_uri = self.redirect_uri
        return flow

    def authorization_url(self) -> dict[str, str]:
        flow = self._flow()
        url, state = flow.authorization_url(
            access_type="offline", include_granted_scopes="true", prompt="consent"
        )
        return {"authorization_url": url, "state": state}

    def complete_authorization(self, code: str, state: str, expected_state: str) -> dict[str, Any]:
        if not state or not expected_state or state != expected_state:
            raise GmailConfigurationError("OAuth state validation failed")
        flow = self._flow(state=state)
        flow.fetch_token(code=code)
        credentials = flow.credentials
        self.token_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.token_path.with_suffix(self.token_path.suffix + ".tmp")
        temporary.write_text(credentials.to_json(), encoding="utf-8")
        try:
            os.chmod(temporary, 0o600)
        except OSError:
            pass
        temporary.replace(self.token_path)
        return {"connected": True, "scopes": list(credentials.scopes or SCOPES)}

    def _credentials(self):
        self._require_config()
        if not self.token_path.is_file():
            raise GmailNotConnectedError("Gmail mailbox is not connected. Complete the OAuth consent flow first.")
        try:
            from google.oauth2.credentials import Credentials
            from google.auth.transport.requests import Request
        except ImportError as exc:
            raise GmailConfigurationError("Google authentication libraries are not installed") from exc
        credentials = Credentials.from_authorized_user_file(str(self.token_path), SCOPES)
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
            self.token_path.write_text(credentials.to_json(), encoding="utf-8")
            try:
                os.chmod(self.token_path, 0o600)
            except OSError:
                pass
        if not credentials.valid:
            raise GmailNotConnectedError("Gmail authorization expired; reconnect the mailbox")
        return credentials

    def status(self) -> dict[str, Any]:
        return {
            "provider": "Google Gmail API",
            "configured": bool(self.client_id and self.client_secret and self.redirect_uri),
            "connected": self.token_path.is_file(),
            "scopes": SCOPES,
            "token_storage": "external_file_not_in_repository",
        }

    def send_email(self, to: str, subject: str, body: str, *, cc: str | None = None) -> dict[str, str]:
        if not to or not subject or not body:
            raise ValueError("to, subject and body are required")
        try:
            from googleapiclient.discovery import build
        except ImportError as exc:
            raise GmailConfigurationError("Install google-api-python-client") from exc
        message = EmailMessage()
        message["To"] = to
        message["Subject"] = subject
        if cc:
            message["Cc"] = cc
        message.set_content(body)
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode("ascii")
        service = build("gmail", "v1", credentials=self._credentials(), cache_discovery=False)
        result = service.users().messages().send(userId="me", body={"raw": raw}).execute()
        return {"message_id": str(result.get("id", "")), "thread_id": str(result.get("threadId", ""))}
