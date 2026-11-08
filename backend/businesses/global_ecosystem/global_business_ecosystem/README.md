# Global Business Ecosystem — Intelligence & AI Layer

A general-purpose, India-first and global-ready Business domain intelligence
package. It extends the established Business domain; it does not create a
parallel record store or duplicate the existing API.

## Capabilities

- **Explainable profile intelligence:** completeness, readiness bands and
  transparent rule-based risk signals.
- **Action planning:** prioritized operational follow-up tasks.
- **Portfolio comparison:** documentation-readiness comparison, not market ranking.
- **LLM business analysis:** optional OpenAI Responses API integration for
  business strategy, growth planning, operational analysis, opportunity and
  risk review, and business Q&A.
- **Provider boundary:** explicit provider contract and registry. OpenAI is
  registered by default; it is enabled only when `OPENAI_API_KEY` is present
  in the server environment. A successful model request is required before
  the provider is reported as live-verified.

## Architecture and ownership

- Existing domain model: `backend/businesses/model.py`
- Existing persistence/service: `backend/businesses/service.py` and
  `backend/businesses/connection.py`
- Existing authenticated API and owner checks:
  `backend/api/businesses.py`
- Shared persistence remains the `business_profiles` table through
  `backend.database.service.DatabaseService`.
- This package owns business intelligence and AI-provider orchestration only.
  It does not own API transport, CORE orchestration, ENGINE execution,
  DATABASE, STORAGE, SECURITY or SERVER infrastructure.
- No new database or API route is created by this package change.

## Service methods

Import `GlobalBusinessEcosystemService` and call:

- `health()`
- `assess(business_id)`
- `action_plan(business_id)`
- `analyze_with_ai(business_id, task, provider_id="openai")`
- `compare(business_ids)`
- `provider_capabilities()`

Example:

```python
service.analyze_with_ai(
    business_id="BUSINESS_ID",
    task="Prepare a 90-day growth plan. Separate evidence from assumptions.",
)
```

Callers must enforce the existing business ownership/authorization checks
before exposing assessment, analysis or comparison results.

## Configuration

Set `OPENAI_API_KEY` as a server-side deployment secret. Optionally set
`GLOBAL_BUSINESS_AI_MODEL` to an available model permitted for the API project.
The OpenAI SDK is already listed in `backend/requirements.txt`.

Never commit API keys, pass them from the browser, or log them. Without the
key, deterministic intelligence remains available and the OpenAI provider is
reported as disabled. No provider call is made automatically.

## Data handling and limitations

The OpenAI adapter sends only an allow-listed set of business profile fields.
Public contact details and arbitrary metadata are excluded. User-supplied
business data remains unverified. The LLM does not independently verify legal
compliance, financial health, creditworthiness, fraud, market size, or business
success. AI output is advisory and must be checked by a qualified professional
where legal, tax, financial or regulatory decisions are involved.

The rule-based readiness score remains a deterministic documentation heuristic,
not an AI prediction. Live market data and government/registry integrations are
not included.
