# GOOGLE GEMINI API ECOSYSTEM

Dedicated Google-owned generative AI API child under the canonical Google API ecosystem.

## Scope
- Gemini Developer API through the official `google-genai` Python SDK.
- API-key connection validation and explicit content-generation calls.
- Supports either a per-request user-supplied key (BYOK) or a deployment-managed key.
- Never logs, returns, commits, or persists API keys in this adapter.
- Vertex AI remains a separate sibling integration under `google_vertex_ai_api_ecosystem/`; do not conflate Gemini Developer API keys with Google Cloud IAM credentials.

## User experience target
1. User signs in to SUPREMESETUHUB.
2. User opens Google Gemini and chooses **Connect**.
3. The platform validates the supplied key, or uses the platform-managed credential if the product owner has enabled shared billing.
4. The UI displays the result of a real connection test.
5. User invokes Gemini features only after an explicit action.

A successful key test is not a persistent account connection. This scaffold intentionally reports `credential_persisted: false`. Before enabling a durable per-user **Connected** state, implement a production secret-store adapter that encrypts credentials at rest, scopes each record to the authenticated user/tenant, supports rotation/revocation, and never exposes plaintext in status responses. Do not use the in-memory Vault service as durable production storage.

## Deployment owner setup (one-time)
- Create/choose a Google AI Studio / Google Cloud project.
- Enable the Gemini API for the project and review applicable billing, quotas, regional availability, and terms.
- Configure `GOOGLE_GEMINI_API_KEY` in the hosting provider's secret manager (never in Git, frontend code, or a committed `.env`).
- Configure `GOOGLE_GEMINI_MODEL` to a model enabled for that project.
- Ensure outbound HTTPS access and install the repository's backend requirements (`google-genai` is already declared in `backend/requirements.txt`).

If the product uses a shared platform key, SUPREMESETUHUB pays for and rate-limits usage. Apply per-user quotas, abuse controls, usage metering, and cost limits before opening shared access.

## BYOK versus platform-managed credentials
- **BYOK:** each user supplies their own Gemini API key. The current service accepts it per request and discards it after the call; persistent storage is not implemented.
- **Platform-managed:** the owner configures one server-side key. Users do not enter a key, but usage is billed to the platform project and must be protected with quotas and abuse prevention.

## Python usage
```python
from ...google_gemini_api_ecosystem import GoogleGeminiAPIService

gemini = GoogleGeminiAPIService()
connection = gemini.test_connection(api_key="USER_KEY")  # key is not saved
result = gemini.generate_content(
    "Summarize this text.",
    api_key="USER_KEY",
    model="MODEL_CONFIGURED_FOR_PROJECT",
)
```

## Status and security boundary
- Adapter code: scaffold implemented.
- Live connection: not verified until a real deployment key is tested.
- Per-user persistent connection: not implemented.
- OAuth: not required for Gemini Developer API key access. Vertex AI uses a separate Google Cloud identity/authentication setup.
- Never ask users to paste API keys into public support chats or store them in source control.
