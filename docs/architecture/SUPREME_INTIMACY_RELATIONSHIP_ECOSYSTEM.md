# SUPREMESETUHUB Intimacy, Relationship Guidance and Couples Privacy Architecture

## 1. Purpose and scope

This design covers all three owner-selected areas:
1. Relationship guidance, communication skills and couple-counselling resources.
2. Consensual adult intimacy education and wellbeing information.
3. Private partner/couple communication features with explicit consent and privacy controls.

This is an architecture proposal, not a claim that these product features or their database/API implementations are already live. SUPREMESETUHUB remains the single foundation. Reuse the existing authentication, CORE, database, storage, security and provider registry; do not create a duplicate core, user system, database or storage service.

## 2. Product boundaries

- Educational material is general information, not a diagnosis, medical treatment, legal opinion or substitute for a qualified professional.
- Adult intimacy education must be age-gated according to applicable law and platform policy. Do not target minors with sexual content. Keep general healthy-relationship and safety education age-appropriate.
- Partner features require separate, explicit, revocable consent from each participant. One partner cannot grant consent for another.
- Do not expose a partner's private messages, preferences, relationship history, health disclosures or usage to the other partner by default. A shared space must show exactly what is shared before submission.
- No covert tracking, forced account linking, secret recording, non-consensual intimate imagery, coercion tools, or impersonation/voice cloning.
- Offer report, block, disconnect, delete/export, privacy and safety controls. Make leaving a shared space possible without the other partner's permission.
- Crisis, abuse, coercion or immediate danger disclosures should be handled with supportive, safety-first guidance and region-appropriate referral information; do not promise confidentiality beyond the actual service policy or legal obligations.

## 3. Layer-by-layer architecture

### API layer

Add a versioned, authenticated router only after the underlying owner-scoped services and migrations exist. Suggested route groups:

- `GET /api/v1/relationships/resources` — list published relationship communication and wellbeing resources with locale and age-appropriate filtering.
- `GET /api/v1/relationships/resources/{resource_id}` — fetch a published resource.
- `POST /api/v1/relationships/consent` — record a user's own consent choice for a clearly described purpose and version of terms.
- `GET /api/v1/relationships/consent` — read the caller's consent records only.
- `DELETE /api/v1/relationships/consent/{consent_id}` — revoke the caller's revocable consent; trigger downstream access revocation and applicable data cleanup.
- `POST /api/v1/couples/invitations` — create a short-lived, single-use invitation initiated by an authenticated adult account where required.
- `POST /api/v1/couples/invitations/{token}/accept` — the invitee independently accepts after seeing the data-sharing scope.
- `GET /api/v1/couples/spaces/{space_id}` — read only a space the caller is an active member of.
- `POST /api/v1/couples/spaces/{space_id}/messages` and `GET .../messages` — private communication with per-member authorization, abuse controls and clear retention rules.
- `POST /api/v1/couples/spaces/{space_id}/leave` — leave/revoke membership without partner approval.
- `POST /api/v1/safety/reports` — submit a safety/abuse report with minimal necessary evidence.

Do not mark these routes public in the application's public-path allowlist. Use the existing authentication dependency and enforce authorization in the service layer for every object, not just at the route prefix. Invitation tokens must be random, short-lived, single-use, stored hashed, and never logged.

### CORE layer

Create a domain service (for example `RelationshipSafetyService`) within the existing CORE patterns. It should:

- apply age/eligibility gates, account status, per-user permissions and regional policy;
- evaluate explicit consent per purpose, content category, partner space and provider transfer;
- enforce per-resource and per-message ownership/membership checks;
- orchestrate revocation, disconnect, retention, export and deletion workflows;
- use idempotent operations and audit events without recording intimate message content in audit logs;
- fail closed when identity, consent, membership or policy state is missing.

CORE is the policy authority. API handlers and engines must not invent their own consent rules.

### ENGINES layer

Use pluggable adapters behind existing engine/provider conventions:

- `relationship_resource_search`: search and rank reviewed educational resources by locale and topic;
- `relationship_guidance`: generate general communication prompts and reflective exercises, with clear AI disclosure and safety filters;
- `content_moderation`: detect threats, harassment, coercion, abuse, non-consensual intimate imagery attempts and policy violations;
- `translation`: localize resources and, only with explicit user action, translate a message for the recipient's chosen language;
- `notification`: send privacy-minimal notifications without revealing message contents on lock screens or email subject lines by default.

Engines must receive only the minimum data required for a task. External AI or translation providers are disabled until their data retention, training use, region, cost, supported languages and contractual terms are reviewed. Do not send intimate messages or sensitive relationship/health disclosures to a provider by default. Prefer local processing or an explicitly disclosed opt-in flow. Generated guidance must not present itself as a licensed therapist or clinician.

### DATABASE layer

Use the existing `DatabaseService`/migration conventions after inspecting them; do not add a parallel database. Proposed logical entities (exact schema is subject to repository migration conventions):

- `relationship_resources`: resource id, locale, topic, age category, content, review status, source/reviewer, publication state and version.
- `relationship_consents`: user id, purpose, scope, policy/terms version, consent state, captured/revoked timestamps and optional expiry.
- `couple_spaces`: id, status, creation time, policy version and deletion/retention deadline.
- `couple_memberships`: space id, user id, role, invite/accept timestamps, membership state and revocation time. Enforce unique active membership rules.
- `couple_invitations`: token hash, inviter id, intended scope, expiry, use timestamp and revocation state.
- `couple_messages`: space id, sender id, encrypted or otherwise protected content, creation time, deletion state and retention deadline. Do not duplicate plaintext into analytics tables.
- `message_translations`: message id, target user/language, translated body, provider/model, status and expiry; keep original content authoritative and allow deletion of translations.
- `safety_reports`: reporter id, restricted case state, minimum necessary evidence reference, access policy and timestamps.
- `privacy_audit_events`: actor, action, object reference, policy result, timestamp and request correlation id; never log message body, intimate images, access tokens or secrets.

Apply foreign keys, indexes, migrations, data minimization, encryption at rest where supported, and strict per-user/per-space access checks. Sensitive fields require documented retention and deletion semantics. Use pseudonymous identifiers in logs/metrics.

### STORAGE layer

- Reuse the existing private storage abstraction; no public bucket or public media URL for private relationship data.
- Intimate images/videos should not be part of the initial release. If future scope is approved, require strong age/consent checks, upload scanning, private access, short-lived signed URLs, strict download auditing and a separate abuse-response process.
- Store resource illustrations separately from private user content.
- Never put storage keys, invitation tokens or signed URLs in public frontend code, logs or analytics.
- Deletion jobs must remove derived translations, exports and provider copies where contractually possible; accurately disclose copies that cannot be recalled from an external provider.

### SERVER / operations layer

- Enforce TLS, secure cookies/token handling, secret management, request size limits, rate limits, anti-spam controls, CSRF protections where cookie auth is used, and safe error messages.
- Run deletion/export/consent-revocation workflows asynchronously when necessary, with durable job status and retries.
- Keep private message content out of application logs, traces, crash reports and analytics. Restrict operator access and audit privileged access.
- Configure backups with retention and documented deletion limitations; test restore and deletion workflows.
- Add alerts for invitation abuse, mass scraping, repeated harassment reports, unexpected provider data transfer and unusual access patterns.

### SUPREME ECOSYSTEM layer

- Register relationship guidance, moderation, translation and notification capabilities in the existing provider/engine registry rather than binding the product to one vendor.
- Evaluate provider compatibility, language coverage, privacy terms, region/data residency, latency, quality, availability and cost.
- Provider changes require review and explicit approval when they alter sensitive-data handling, regions, cost ceilings or retention.
- The ecosystem registry stores capability metadata and references to secret-managed configuration only; never store provider credentials in source code or client-visible responses.
- Integrate with the existing CORE, security, database and storage services. Do not make the private owner-control SUPREME ECOSYSTEM endpoints into public relationship APIs.

## 4. User experience and consent flow

1. Explain the feature and privacy model in the user's selected language.
2. Apply applicable age/eligibility gates before adult intimacy education is displayed.
3. Keep general educational browsing separate from private couple spaces.
4. Before creating a shared space, show what can be shared, who can see it, what AI/translation providers may receive, and how to leave/delete.
5. Require the invitee to accept independently. No implicit linking through contacts or a partner's assertion.
6. Keep message translation opt-in and recipient-language-specific; show the original text and label machine translation. Never silently alter the authoritative original.
7. Make block/report, disconnect, export and delete controls discoverable.
8. Provide a neutral notification mode that does not expose intimate topics or message text on shared devices.

## 5. Security and privacy acceptance criteria

- A user cannot read, edit, export or delete another user's private records without explicit authorized shared scope.
- An invitation cannot be reused, guessed, or accepted after expiry/revocation.
- Consent revocation immediately blocks future processing and starts applicable cleanup; status is visible to the user.
- A partner leaving a space loses access; the remaining member does not inherit private content outside the documented shared-space policy.
- Logs and analytics contain no raw intimate messages, sexual/health disclosures, invitation tokens or credentials.
- Translation/provider transfer is opt-in, disclosed, minimized and auditable without storing sensitive message content in audit records.
- API tests cover unauthenticated access, cross-user IDOR, revoked membership, expired invitations, revoked consent, deletion, rate limits and provider failure.
- Resource content has provenance/review status and does not make unsupported clinical claims.
- Production deployment remains blocked until migrations, authorization tests, abuse handling, privacy notice, retention/deletion policies and legal/platform review are complete.

## 6. Phased implementation plan

**Phase A — foundation and policy:** review existing database, security, CORE and engine conventions; document data map, threat model, age policy, retention, provider review and resource editorial standards.

**Phase B — low-risk resources:** publish reviewed relationship communication/wellbeing resources with localization and feedback/reporting. No private messages or intimate media.

**Phase C — consent and couple spaces:** implement migrations, invitations, two-sided consent, private messages, membership authorization, block/report, deletion/export and security tests.

**Phase D — optional AI and translation:** add provider adapters behind explicit opt-in, disclosure, budget/rate controls and data-processing review; keep original messages visible and authoritative.

**Phase E — production readiness:** security review, cross-account authorization tests, abuse drills, accessibility/localization review, data deletion verification, provider failure tests and staged rollout.

## 7. Implementation status

This file is an architecture design only. It does not create API routes, database tables, storage buckets, background workers, adult verification, moderation engines, provider connections or user-facing intimacy screens. Those require deliberate implementation, tests, migrations and deployment verification. Do not claim the feature is live until those steps pass.
