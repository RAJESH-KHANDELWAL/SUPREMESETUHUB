# Technology Intelligence — Operations and API Integration Policy

## First release scope
A scheduled workflow reads three configured public RSS/Atom feeds and publishes a downloadable GitHub Actions artifact. It needs no API credentials, performs no database writes, and cannot update production. A successful run does not mean all global technology news was discovered.

## API groups to consider, not yet configured
- Code/dependencies: GitHub API, releases, Dependabot, dependency review, CodeQL, secret scanning and SBOM tooling.
- Core frameworks: official Python, FastAPI, WordPress security/news, PHP supported versions, PostgreSQL and MySQL/MariaDB release notes.
- Cloud/hosting: the selected host's status, release notes, deployment API and metrics APIs.
- AI providers: official OpenAI API changelog/model docs and other vendor changelogs; track deprecations, pricing, regions, data retention and terms.
- Commerce: official WooCommerce, Printify and Qikink docs/changelogs, webhooks and sandbox status. Do not sync catalogs/orders until provider ownership and permissions are reviewed.
- Domain/security: registrar/DNS APIs, TLS expiry, renewal reminders, uptime and security advisories.
- Business operations: email, analytics, payment and CRM APIs only after data access, consent, cost and compliance review.

These are a roadmap, not a claim that integrations are configured. Prefer official sources and provider-supported APIs. Never treat an AI model as the source of truth.

## Future finding data model
Use UUID, provider_id, product, component, source_url, canonical_url, version, published_at, observed_at, source_type, severity, affected_versions, summary, evidence_hash, benefits, risks, breaking_changes, compatibility_notes, cost_notes, privacy_notes, recommendation, confidence, unknowns, reviewer, decision_at, status, duplicate_of and retention_until. Store concise summaries and source URLs by default; respect source terms and keep customer data out.

## Future API design
- GET /api/v1/tech-intelligence/findings — authenticated, paginated, filterable.
- GET /api/v1/tech-intelligence/findings/{id} — finding and evidence links.
- POST /api/v1/tech-intelligence/findings/{id}/decision — authorized reviewer decision, reason and audit event.
- GET /api/v1/tech-intelligence/health — non-sensitive health only.
Ingest endpoints must authenticate providers, verify webhook signatures, validate schemas, apply idempotency keys and rate limits. Separate read-only scanner identity from admin decision identity. The first release must not expose an endpoint that deploys updates.

## Rollout gates
1. Inventory actual deployment, DNS, host, WordPress version/plugins, database type, backups and current FastAPI entrypoint.
2. Run scanner tests and inspect report/feed errors.
3. Review source licensing, terms and privacy implications.
4. Choose durable DB/migrations; do not point this tool at the production WordPress DB.
5. Add dashboard after access-control tests, retention policy and observability exist.
6. Add AI summaries only as evidence-linked drafts with confidence and explicit unknowns.
7. Add staging automation only after rollback and test coverage are demonstrated.
8. Production updates require human approval, tested backup/restore, staged rollout and monitored rollback.

## Security
- HTTPS everywhere; no public database ports.
- Secrets belong in hosting environment or GitHub Actions secrets, never committed source or reports.
- Least privilege, short-lived tokens where possible, credential rotation and revocation.
- Validate inputs; escape output; enforce WordPress capabilities/nonces and FastAPI authentication/authorization.
- Rate limits, request size limits, timeouts, dependency pinning, vulnerability scanning and audit logging.
- Back up WordPress files and database separately, encrypt backup copies, keep multiple copies in separate locations and test restoration.
- Maintain privacy notice, retention/deletion process, incident response and region-specific compliance review.

## Not configured by this change
No hosting plan, DNS, SSL, production database, WordPress plugin, private provider API, LLM API, alert destination or deployment secret is connected. These require access to actual provider accounts and a separate reviewed setup. Never paste credentials into chat or commit them to GitHub.
