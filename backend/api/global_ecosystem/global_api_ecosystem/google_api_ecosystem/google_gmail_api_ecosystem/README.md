# GLOBAL GOOGLE GMAIL API ECOSYSTEM

A provider-owned Gmail API adapter under the canonical Global Google API Ecosystem. The existing Google Business category folder is a business taxonomy/catalog entry; Gmail is a Google Workspace communication API and must not be represented as Google Business Profile API.

## Scope
- OAuth 2.0 authorization-code flow for one explicitly consented mailbox.
- Least-privilege scope: `https://www.googleapis.com/auth/gmail.send` only.
- Send plain-text email with optional CC.
- Refresh OAuth access tokens when possible.
- Store token JSON outside the repository with restrictive file permissions.
- No Gmail password, client secret, or token is stored in source control.

## Google Cloud setup
1. Create/select a Google Cloud project and enable **Gmail API**.
2. Configure the OAuth consent screen and add the mailbox as a test user while the app is in testing.
3. Create an OAuth Client ID of type **Web application**.
4. Add the exact deployed callback URL to Authorized redirect URIs.
5. Configure server environment variables:
   - `GOOGLE_CLIENT_ID`
   - `GOOGLE_CLIENT_SECRET`
   - `GOOGLE_GMAIL_REDIRECT_URI` (or existing `GOOGLE_REDIRECT_URI`)
   - optional `GOOGLE_GMAIL_TOKEN_PATH` (default: `/var/lib/supremesetuhub/google/gmail/token.json`)
6. Ensure the token directory is private, persistent, backed up securely, and excluded from Git. For multi-user production, replace the single-mailbox file store with an encrypted per-user token store and bind OAuth state to the initiating user/session.
7. Install backend dependencies and run the application's OAuth callback through a trusted, authenticated route. Do not expose an unauthenticated arbitrary-email sending endpoint.

## Python usage

```python
from ...gmail_api_ecosystem import GmailAPIService

gmail = GmailAPIService()
# First: send authorization_url() to the signed-in administrator and retain state
# securely in that user's server-side session.
# After callback: complete_authorization(code, state, expected_state)
# Then, after explicit user action/confirmation:
result = gmail.send_email(to="recipient@example.com", subject="Hello", body="Message")
```

## Important integration boundary
ChatGPT's connected Gmail app, GitHub Actions, and this backend OAuth client are separate authorization contexts. Connecting one does not automatically authorize the others. ChatGPT can use its Gmail connection where supported; GitHub Actions/backend can send only after this server-side OAuth setup is completed. Never put OAuth secrets in commits, frontend code, logs, or chat messages.

## Status
Adapter scaffold implemented; live connection is **not verified** until Google Cloud OAuth configuration and mailbox consent are completed in the deployment environment.
