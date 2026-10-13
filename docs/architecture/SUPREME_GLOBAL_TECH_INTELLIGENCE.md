# SUPREMESETUHUB — Global Technology Intelligence Architecture

## Mission
Create a source-grounded technology watch system that finds releases and advisories, records evidence, explains likely benefits and risks, and recommends REVIEW / PILOT / DEFER / REJECT. It must not silently update production systems, install packages, publish WordPress content, or submit commerce orders.

## System map
- DOMAIN / DNS: domain registrar owns registration; DNS routes the apex and subdomains. DNS is not hosting or a database.
- EDGE / TLS: HTTPS certificates, CDN/WAF and rate limiting where available.
- WORDPRESS + WOOCOMMERCE: PHP, JavaScript/TypeScript, HTML/CSS. Use WordPress APIs and official plugins for CMS and commerce. WordPress data usually lives in MySQL/MariaDB.
- BACKEND: Python + FastAPI for shared APIs, registry, identity, authorization, integration adapters and technology intelligence.
- DATABASE: PostgreSQL for production API data; SQLite for local development/tests or small single-process deployments. WordPress keeps its own database unless a reviewed integration explicitly needs cross-system data.
- ASYNC JOBS/CACHE: add a queue only when workload warrants it; scheduled GitHub Actions is the first low-cost scanner scheduler.
- FILES: store media and reports separately from relational records; private by default.
- CLIENTS: web, Android (Kotlin/Java) and iOS (Swift) call authenticated APIs, never connect directly to databases.
- SOURCE CONTROL/CI: GitHub branches, pull requests, tests and security checks. Deploy from reviewed commits.
- OBSERVABILITY: structured logs, metrics, health checks, alerts and audit events; never log secrets or sensitive payloads.

## Languages and responsibilities
| Area | Default | Notes |
|---|---|---|
| WordPress plugin/theme | PHP, JS/TS, CSS, HTML | Use WordPress hooks, capabilities, nonces, sanitization/escaping, REST API. |
| Core API | Python + FastAPI | Version routes, validate input and enforce permissions. |
| Browser UI | TypeScript/JavaScript | Build a separate UI only when needed; avoid needless duplication of WordPress. |
| Android / iOS | Kotlin/Java / Swift | Call backend APIs; keep provider keys server-side. |
| Production API DB | PostgreSQL | Migrations, least-privilege DB user, backups and tested restores. |
| WordPress DB | MySQL/MariaDB | Separate credentials and backup/restore procedure. |
| Contracts | OpenAPI + JSON | Version APIs and document breaking changes. |
| CI | GitHub Actions | Tests and read-only scanning; secrets only when strictly required. |

## Integration registry
Every provider integration records provider ID, official docs URL, product/service scope, API version, authentication method and secret reference (never the secret itself), requested scopes, data categories/owner/retention, rate limits, cost model, regional availability, webhook requirements, health, last successful check/error, owner, kill switch, sandbox mode and production approval.

Google, OpenAI, WordPress, WooCommerce, Printify, Qikink and future providers retain ownership of their catalogs, credentials, orders and rules. The central registry routes and observes; it must not merge provider data or assume one provider's permissions authorize another provider's data.

## Technology Intelligence lifecycle
1. DISCOVER: official release feeds, security advisories, vendor changelogs and supported APIs. Community posts are leads, not proof.
2. NORMALIZE: source, URL, product/version, published and retrieval times, release type, affected versions and evidence hash.
3. DEDUPLICATE: canonical URL + provider + version.
4. ASSESS: relevance, security severity, breaking changes, compatibility, migration effort, cost, regional/privacy impact, rollback path and confidence.
5. EXPLAIN: what changed; why it matters; benefits; risks/losses; who is affected; where/how to test; when to adopt or avoid; evidence and unknowns.
6. RECOMMEND: REVIEW, PILOT, DEFER or REJECT with explicit reasons. Missing evidence must be labelled unknown.
7. HUMAN APPROVAL: production changes require a reviewed PR, passing CI, backup/restore check, staging test and named approver.
8. LEARN: track decision, deployed version, outcome and rollback incidents.

## Non-negotiable safety rules
- Discovery/reporting can be automated; production changes cannot be automatic by default.
- Never auto-update WordPress plugins/themes, OS packages, dependencies, database schemas, provider APIs or live products based only on an AI recommendation.
- Never put API keys, passwords, tokens, customer records or private URLs in source code, reports, logs, issues or public artifacts.
- Use least-privilege credentials and environment-scoped GitHub secrets. Public-feed scanning should work without secrets.
- Do not send personal/customer data to an LLM unless purpose, provider terms, consent/legal basis, retention and data-processing controls are reviewed.
- Do not scrape behind login or bypass rate limits/terms. Prefer official APIs/feeds.
- Maintain dependency/license scanning, secret scanning, vulnerability alerts, and an incident process.
- Keep 3–5 recent backups in separate locations and test restore. Back up both WordPress files and its database before upgrades.
- Global readiness includes data minimization, privacy notices/consent where applicable, retention/deletion, localization, accessibility, tax/payment rules, residency obligations and India/global legal review.

## Deployment stages
1. Inventory actual repo, hosting, DNS, WordPress DB, deployment target, data flows and owners.
2. Run a read-only scanner against public release/security feeds and generate a report artifact.
3. Add persistence/dashboard only after schema, access-control and retention review.
4. Add source-specific rules and optional AI summaries grounded in citations; require human review.
5. Open proposed dependency-update PRs and test in isolated staging.
6. Production rollout only with backup, approval, monitoring, canary/rollback and post-deploy verification.

## Scope of the initial implementation
The initial scanner checks configured public RSS/Atom sources and writes a Markdown report. It is read-only. It does not connect to production WordPress, PostgreSQL, private provider APIs, nor claim to know every technology update on the internet.
