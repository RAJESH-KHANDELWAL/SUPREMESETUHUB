# SUPREMESETUHUB — INTIMACY + RELATIONSHIP PRODUCT ARCHITECTURE

## 1. Product decision

The product owner has clarified that **INTIMACY** is intended as an adult-only explicit-content entertainment platform, comparable in product category to established adult video subscription/user-generated-content services. This architecture describes platform systems and safety controls, not explicit sexual content itself.

**RELATIONSHIP** is a separate product for relationship guidance, communication, couples resources and consensual adult intimacy education/wellbeing. They must work independently and may also be presented together as a bundle. Shared identity, CORE, API gateway, provider registry and infrastructure do not mean their content, permissions, recommendation history or private records should be merged.

This document is a design specification only. It does not mean adult-content features are implemented, lawful in every jurisdiction, approved by hosting/payment providers, or available in production.

## 2. Product boundaries and navigation

- `INTIMACY`: adult-only media discovery, licensed/authorized video catalog, creator/studio pages, subscriptions where supported, captions/audio-language tracks, user library, content reports and creator/content rights workflows.
- `RELATIONSHIP`: educational resources, communication tools, optional couple spaces, wellbeing information and independently consented partner messaging.
- `SUPREME PLUS` (optional bundle concept): one purchase/access plan that can include both products only where law, payment provider terms and user eligibility allow it. Separate product access flags, policies, receipts, cancellation controls and entitlements must remain explicit.
- Keep the two products visually and functionally distinct. Users must know which product they are entering and which terms/data policy apply. No automatic sharing of activity or sensitive data between them.
- No content involving minors, sexual exploitation, trafficking, coercion, non-consensual intimate imagery, hidden-camera material, or content lacking verifiable performer consent and distribution rights. Any suspected illegal content requires a defined safety escalation and legally compliant reporting process.
- Do not bypass DRM, scrape protected services, or republish third-party content without authorization. Creator uploads require rights/consent attestations plus verification and review controls; attestations alone are not sufficient for high-risk content.
- Applicable age/identity/consent checks must be designed with qualified legal and compliance review for every launch region. Do not treat a simple self-declared birthday as universally sufficient age assurance.

## 3. Shared architecture across existing SUPREMESETUHUB layers

### API / gateway

Create separate, authenticated, versioned API namespaces only after policy, migrations, provider contracts and authorization tests are ready:

**INTIMACY namespace (proposed, not implemented)**
- `GET /api/v1/intimacy/catalog` — list only reviewed, region-eligible catalog metadata.
- `GET /api/v1/intimacy/titles/{title_id}` — authorized title details and available language tracks.
- `GET /api/v1/intimacy/titles/{title_id}/playback` — issue a short-lived playback grant only after entitlement, age/region, rights and session checks.
- `GET /api/v1/intimacy/library` — current user's saved items only.
- `POST /api/v1/intimacy/reports` — report a title/creator or rights/safety concern.
- `POST /api/v1/intimacy/creator-submissions` — submit a content/rights review package, not instant publication.
- `GET /api/v1/intimacy/localization/{job_id}` and related job endpoints — only for media the platform has permission to process and distribute.

**RELATIONSHIP namespace (proposed, not implemented)**
- `GET /api/v1/relationships/resources` and `GET /api/v1/relationships/resources/{resource_id}` — reviewed localized resources.
- `POST /api/v1/relationships/consent` and `DELETE /api/v1/relationships/consent/{consent_id}` — record/revoke the caller's consent for a stated purpose.
- `POST /api/v1/couples/invitations`, `POST /api/v1/couples/invitations/{token}/accept`, `GET /api/v1/couples/spaces/{space_id}/messages`, `POST /api/v1/couples/spaces/{space_id}/messages`, and `POST /api/v1/couples/spaces/{space_id}/leave` — two-sided, private couple functionality.
- `POST /api/v1/relationships/reports` — report abuse or unsafe content.

Never add these paths to a public unauthenticated allowlist. Playback grants and invitations must be short-lived and unguessable. Enforce authorization at the resource/service layer, not only by checking a route prefix. Avoid logging sensitive query strings, tokens or private message bodies.

### CORE / policy orchestration

Use the existing CORE and security conventions; do not create a parallel identity system or second CORE.

CORE must decide whether an operation is allowed based on user/session status, age/eligibility result, region, product entitlement, content classification, distribution rights, performer consent status, account restrictions, consent scope, and provider policy. It orchestrates upload review, media processing, playback grants, subscription entitlements, takedowns, reports, consent revocation, export and deletion.

Fail closed if verification, rights, region, entitlement, consent or moderation state is missing. Never allow an engine or UI to override policy decisions. Keep INTIMACY access flags separate from RELATIONSHIP access flags; bundle access is an explicit entitlement mapping, not an implicit permission escalation.

### ENGINES / provider adapters

Register provider-neutral capabilities through the existing engine conventions:
- catalog search and metadata indexing;
- media validation, transcoding and adaptive playback packaging;
- speech recognition, translation, subtitle generation, dubbed audio and timestamp alignment for authorized media;
- age/identity assurance adapters selected after legal/provider review;
- content safety classification, human-review queues and rights/takedown processing;
- subscriptions/entitlement checks and payment adapters only for processors whose written terms permit the business category;
- relationship resource search, relationship-guidance assistance and optional opt-in message translation;
- moderation/report triage and privacy-minimal notifications.

Do not assume a general-purpose hosting, AI, payment, app-store or CDN provider permits adult-content use. Obtain and document approval for the exact service, geography, storage/streaming pattern and payment flow. Never send private couple messages, identity documents, payment data or intimate media to an AI/translation provider unless the processing is necessary, contractually permitted, disclosed and explicitly authorized. Provider capability metadata may be stored in the registry; credentials belong in deployment secret management.

### DATABASE

Reuse the repository's existing database/migration conventions after reviewing the actual schema. Logical entities to consider (not yet created):

**INTIMACY**
- `intimacy_titles`: title metadata, classification, publication/review state, region availability, duration and language metadata.
- `intimacy_assets`: private storage references, track type, codec, language, checksum, processing state and retention/rights status.
- `intimacy_creators`: verified creator/studio identity reference and account state; isolate highly sensitive verification data from general profile data.
- `performer_verifications`: restricted verification provider/reference, status, reviewer, timestamps and audit reference; store as little raw identity evidence as possible and apply strict retention.
- `content_rights`: title/asset, rights-holder, territory, license window, permitted distribution and takedown state.
- `performer_consents`: content/production scope, participant reference, evidence reference, verification state, timestamps and revocation/legal-review workflow.
- `intimacy_entitlements`: user, plan/product, region, status, start/end dates and provider transaction reference (never card data).
- `intimacy_reports` and `moderation_cases`: restricted report/case state, evidence references, reviewer actions, legal hold and retention.
- `media_localization_jobs` and `media_tracks`: authorized source reference, source/target languages, transcript/caption/audio track references, job state, provider usage and costs.

**RELATIONSHIP**
- `relationship_resources`, `relationship_consents`, `couple_spaces`, `couple_memberships`, `couple_invitations`, `couple_messages`, `message_translations`, `relationship_reports` and privacy-minimal `privacy_audit_events`.

**Shared platform**
- Reuse existing users, authentication, provider registry and entitlement foundations where possible. Add explicit `product_id`/scope to entitlements and consent records where needed. Do not combine adult-viewing history with relationship records or use it for relationship recommendations by default.

Use migrations, foreign keys, least-privilege access, owner-scoped queries, indexes, retention jobs and documented deletion semantics. Never store payment-card details directly. Do not copy private message bodies, identity documents or raw verification evidence into logs or analytics.

### STORAGE / CDN

- Reuse the existing storage abstraction but place adult media assets in a separately policy-controlled private namespace/bucket and use an approved CDN/streaming provider only after written policy review.
- Keep original uploads, review evidence, public catalog thumbnails, subtitle tracks and generated dubbed audio in distinct storage classes with different access/retention rules.
- Use encryption, checksums, malware scanning, content-type validation, short-lived signed URLs/playback grants, watermarking where appropriate, download restrictions and access logs that do not expose secrets.
- Private verification evidence and moderation evidence must never be placed in public asset storage. Restrict operator access and audit it.
- Provide verified rights-holder takedown and emergency disable workflows. Expired rights must block new playback grants and trigger the defined distribution/retention policy.
- Do not promise that every platform can dub every movie. Media localization is available only for content the service is authorized to process, with supported providers and valid source assets.

### SERVER / operations

- Run transcoding, speech-to-text, translation, dubbing and caption alignment as asynchronous queue/worker jobs with quotas, idempotency, retries, cancellation, dead-letter handling and usage/cost tracking.
- Enforce TLS, secret management, secure session handling, rate limits, anti-bot controls, abuse detection, backup retention and incident response.
- Isolate media-processing workloads from the API process and restrict access to original assets. Add monitoring for failed verification, suspicious uploads, report spikes, rights expiry, provider-policy changes, data exfiltration and unusual playback scraping.
- Publish privacy notices, retention schedules, user export/deletion processes, moderation appeals and a rights-holder contact workflow before launch.

### SUPREME ECOSYSTEM

- Register INTIMACY and RELATIONSHIP as separate product capabilities connected to the same platform foundation.
- Registry metadata should include provider capabilities, approved business category, permitted regions, supported languages, data residency, costs, latency, reliability, contractual status and last review date.
- Changes to hosting, payments, CDN, AI, identity verification or media processing that affect adult-content handling require explicit owner/compliance approval and a rollback plan.
- Do not expose private owner-control ecosystem APIs to end users. Product-facing APIs use regular authentication and per-resource authorization.

## 4. Consent, safety, and legal readiness gates

Before accepting any adult upload or making any adult title playable, require a region-specific, legally reviewed policy covering age assurance, creator/studio onboarding, performer age and consent verification, rights and releases, prohibited content, moderation, complaint/takedown timelines, record retention, law-enforcement requests, privacy/data protection, payment processing and incident response. Requirements differ by jurisdiction; this document is not legal advice.

At minimum:
- no publication until required age/identity, consent, rights and safety reviews are complete;
- no upload-to-publication automatic path;
- report/block/appeal and emergency disable controls;
- documented access controls for restricted identity and consent evidence;
- region-aware access restrictions and entitlement checks;
- independent, explicit consent for each couple-space participant;
- separate consent for third-party processing and optional message translation;
- deletion/export/revocation behavior documented, including any lawful retention exceptions;
- adult-content product must not be marketed or exposed to minors.

## 5. Product experience: separate, together, or bundle

- Main navigation may show separate entries: **INTIMACY 18+** and **RELATIONSHIP**.
- INTIMACY must display age/eligibility gating and region-specific availability before adult catalog access.
- RELATIONSHIP remains available as a distinct product with its own resources, privacy settings and content policy.
- A combined landing page or optional bundle can introduce both products, but users must select/consent to each product's terms and data usage separately.
- Do not cross-recommend adult titles based on private relationship messages, relationship difficulties, health disclosures or couple-space activity.
- Language settings can localize interface, captions and authorized dubbed tracks. Keep original audio and source-language labels available; show when audio/subtitles are machine-generated.

## 6. Phased delivery plan

**Phase A — feasibility and compliance:** inventory current repo database/storage/auth patterns; confirm legal regions, age-assurance requirements, rights workflows, hosting/CDN and payment-provider eligibility. Do not build around providers that prohibit the business category.

**Phase B — separated product foundations:** product registry, product-specific access flags, policies, age/region gate design, resource catalog and admin review workflow. No public adult uploads yet.

**Phase C — licensed catalog MVP:** ingest only rights-cleared content; implement verified metadata, private storage, playback authorization, reports/takedowns and audit controls.

**Phase D — creator submissions and monetization:** only after verification, consent, rights, moderation, payment-provider approval and abuse-response testing are complete.

**Phase E — authorized media localization:** add subtitle translation and dubbed audio jobs with approved speech providers, rights checks, privacy disclosures and end-to-end media tests.

**Phase F — RELATIONSHIP features and optional bundle:** implement reviewed resources first, then two-sided-consent couple spaces, optional translation, independent entitlements and explicit bundle mapping.

## 7. Acceptance criteria

- No minor, unverified/unauthorized performer, rights-ineligible title, restricted region or missing entitlement can access or publish adult content.
- Cross-user authorization tests prove one account cannot read another account's private data or verification evidence.
- Expired rights and revoked content states block new playback grants.
- Takedown and emergency disable workflows are auditable and tested.
- Payment, hosting, CDN and AI providers are documented as approved for the intended business category before production configuration.
- Relationship data and adult-viewing history remain isolated by default.
- Consent revocation blocks future optional processing and initiates documented cleanup.
- Translation/dubbing APIs never report ready until output assets are actually generated and validated.
- Tests cover authentication, age/region gates, entitlement, rights expiry, consent, upload validation, provider failure, takedown, deletion, rate limits and cross-account access.
- Production release is blocked until legal/compliance review, security review, migrations, provider approval, incident response and end-to-end tests pass.

## 8. Current implementation status

This is architecture documentation only. It does not create the proposed API routers, migrations, adult catalog, verification provider, media workers, payment integrations, CDN configuration, moderation console or user-facing product screens. No production readiness or provider approval is implied. Implement and test these components in small reviewed changes against the existing SUPREMESETUHUB foundations before deployment.
