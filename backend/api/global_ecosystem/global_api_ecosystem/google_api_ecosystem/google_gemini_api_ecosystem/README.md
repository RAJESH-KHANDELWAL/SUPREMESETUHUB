# Google Gemini API Ecosystem

Adapter for the Gemini Developer API (Google AI Studio API key flow).

## User connection contract
- The application asks the account owner for their own Google AI Studio API key.
- Pass the key to `GeminiAPIService(api_key=...)` at runtime; never put it in Git, a URL, logs, or shared environment variables.
- Call `validate_api_key()` before marking the connection as verified.
- The service deliberately does not persist credentials. Persisting a user's key requires the platform's authenticated tenant identity and an encrypted secret vault; do not accept a caller-supplied tenant ID as authorization.
- The API key owner must enable/accept the relevant Google AI service terms and billing/usage requirements.

## Example
```python
from google_gemini_api_ecosystem.service import GeminiAPIService

gemini = GeminiAPIService(api_key=user_submitted_api_key)
status = gemini.validate_api_key()
response = gemini.generate_content(
    model="gemini-2.5-flash",
    contents="Summarize this text in three bullet points.",
)
```

Install dependency from `backend/requirements.txt` (`google-genai`).

## Security boundary
Never return the submitted key in API responses. Redact request bodies from logs and tracing. Use HTTPS. A verified connection means the supplied key successfully reached the API; it does not imply every model, region, quota, or feature is enabled.
