# SUPREME CONSENTED BEHAVIOURAL INSIGHTS & TIMELY ENGAGEMENT

**Status:** Product/engineering design proposal. This is not an active connector, a dataset of people's activity, or proof that SUPREME can access third-party social/search/purchase data.

## 1. Product objective

Help users discover relevant content, services and offers at useful times by combining:
1. signals they intentionally share with SUPREME;
2. first-party activity within SUPREME;
3. purchase/order events from an authorised merchant integration;
4. aggregate or user-authorised platform insights returned through official APIs;
5. explicit feedback, preferences and survey answers.

The goal is relevance and user benefit—not to claim that a system can know 90% of someone's mind. Likes, comments, shares, searches and purchases are incomplete and ambiguous signals: people can interact for humour, research, criticism, gifts, work, curiosity or by accident. Treat each as evidence with uncertainty, not as truth about a person's personality or intent.

## 2. Data access boundary: do not assume global visibility

SUPREME cannot automatically see an individual's private search history, purchases, likes, comments, shares, private messages or browsing activity across the internet. A public profile or visible post does not automatically grant permission to collect it, infer sensitive traits, or use it for direct marketing.

Allowed input paths must be documented per provider:
- **SUPREME first-party events:** activity inside SUPREME, disclosed in the privacy notice and collected only for the stated purpose.
- **Merchant/order integrations:** only the merchant's authorised order/customer data within the contracted scope and with a lawful basis; do not ingest full payment-card data.
- **Official social/platform APIs:** only permitted scopes, approved app access, platform terms and required user/organisation authorisation. Respect rate limits, revocation and platform restrictions.
- **User-provided connections/imports:** explain which fields are imported and what they will be used for before the user connects.
- **Research/surveys:** voluntary, purpose-limited and separated from unrelated marketing unless the person separately opts in.
- **Aggregate trend data:** use sufficiently aggregated data; do not attempt to re-identify people or target a tiny cohort.

Do not scrape behind login, bypass API restrictions, use leaked/bought dossiers, fingerprint people across services, or collect third-party private activity. If a provider does not permit a use, the connector must not offer it.

## 3. Signal registry and confidence

Every event should contain: event ID; pseudonymous user ID where practical; event type; first-party/provider source; provider and scope; timestamp and timezone; stated purpose; consent/authorisation reference; data freshness; retention deadline; confidence; and deletion/revocation status.

Example event types:
- 'interest_selected' — explicit interest chosen by the user (high confidence for that stated preference, not a permanent trait).
- 'search_on_supreme' — search typed inside SUPREME (intent may be exploratory; short-lived).
- 'product_view_on_supreme' — a view inside SUPREME (weak purchase intent).
- 'add_to_cart_on_supreme' — stronger shopping intent but not a purchase.
- 'verified_purchase' — completed merchant order event from an authorised source (evidence of a transaction, not proof of future interest).
- 'content_like_on_supreme' / 'share_on_supreme' — interaction inside SUPREME; low-confidence preference signal.
- 'survey_answer' / 'feedback_submitted' — explicit self-report; store with study purpose and consent.
- 'provider_aggregate_trend' — provider-generated aggregate insight, not an individual profile.

Do not treat events from different sources as equally reliable. A click or like should never alone trigger a high-impact decision. Use recency decay and allow users to correct the profile.

## 4. Personalisation pipeline

1. **Authorise:** verify purpose-specific consent, connector scopes, age/safety rules, jurisdiction and provider terms.
2. **Minimise:** collect only the fields needed; discard irrelevant raw text and sensitive content as early as possible.
3. **Normalise:** map allowed events into the event registry; validate source, timestamp, scope and deletion state.
4. **Build a short-lived interest estimate:** derive broad, non-sensitive categories only (for example, "website building" after repeated relevant first-party activity). Keep provenance and confidence. Do not infer health, religion, political beliefs, sexuality, relationship hardship, financial distress or other sensitive traits for ad targeting.
5. **Rank candidates:** compare permitted content against user-selected interests, active task, language, availability, budget explicitly supplied for that task, recency and content quality.
6. **Explain:** show why something is suggested (e.g., "Shown because you selected website-building tips"). Provide "not interested", "hide", "why this?" and "reset recommendations".
7. **Choose channel and timing:** prefer the SUPREME feed/inbox first. External email, push, SMS or social DMs require separate channel opt-in and a valid sending mechanism.
8. **Frequency and safety checks:** apply user-set frequency caps, quiet hours, per-campaign limits, duplicate suppression, opt-out/suppression lists, age rules, platform rules and legal requirements.
9. **Deliver only when permitted:** never auto-post to a person's personal social account, comment/like/share as them, or send unsolicited platform DMs. For external social posts, the user or authorised page admin must explicitly approve the exact content and destination unless a documented official API workflow permits a different narrowly scoped action.
10. **Measure outcomes:** use aggregate, privacy-aware measures; do not optimise solely for clicks, watch time or compulsive engagement.
11. **Delete/revoke:** stop future collection and delivery when consent is withdrawn, a connector is revoked, or the legal/policy basis ends. Propagate deletion to derived profiles and queued messages where required.

## 5. Timely messaging policy

A "right time" is a user-controlled delivery preference, not an invitation to monitor a person's life continuously.
- Ask for timezone, channels, categories and frequency preference; allow "only when I open SUPREME".
- Use quiet hours by default and respect local time.
- Use event-triggered messages only for clear, disclosed actions (e.g., an order status update or a reminder explicitly requested by the user).
- Marketing messages need their own valid permission/opt-in where required and must include the applicable unsubscribe/stop mechanism.
- Never exploit inferred vulnerability, grief, loneliness, health conditions, financial distress or intimate/sexual interests to pressure a user to buy.
- Do not infer that a person wants contact with someone else from their browsing, viewing, likes or purchase history.
- Never send a message on another person's behalf without explicit, scoped authorization.

## 6. Feedback and survey loop

After a recommendation, offer lightweight optional feedback: useful/not useful; show less/more; wrong interest; don't personalize this category. Surveys should be voluntary, neutral, available in the user's chosen language and explain purpose, data collected, retention and withdrawal. Keep research participation separate from marketing permission.

Use survey answers to correct recommendations, not to secretly expand profiling. Report aggregate results only when cohort size and privacy protections are adequate. Never claim that a small opt-in sample represents a whole country.

## 7. Sensitive-data and fairness safeguards

- No sensitive-trait inference or sensitive-category advertising based on browsing, purchases, social engagement or survey free text.
- Treat relationship/intimacy, health, religion, politics, sexuality, financial hardship and similar topics as restricted; do not build a persuasion profile from them. Users can seek content directly, but that does not automatically authorise marketing use.
- Do not profile children for targeted marketing; apply age-appropriate defaults and jurisdiction-specific safeguards.
- Avoid proxy discrimination and exclusion from employment, housing, finance, essential services or opportunities based on inferred interests.
- Use minimum cohort thresholds for analytics and prohibit re-identification.
- Provide a no-personalisation option with core features still usable.
- Provide access, correction, export and deletion routes where applicable.
- Review model outputs for false assumptions, disparate outcomes and manipulative timing.

## 8. External channel and provider capability registry

For every integration, maintain:
- provider name and official API documentation;
- supported data and actions;
- permitted purposes and prohibited uses;
- approved scopes and app review status;
- consent/authorisation requirements;
- message/post destination type (user account vs business/page account);
- rate limits, review status and revocation behaviour;
- data residency/retention details;
- owner, security review and last verification date.

If official API access does not support an individual-level action, mark it 'UNAVAILABLE'; do not silently fall back to scraping or simulated sending. Drafting a suggested post is different from publishing it.

## 9. Rollout plan

**Phase 1 — first-party, opt-in:** SUPREME preferences, in-product search/view/cart events, recommendation explanations, hide/reset controls, quiet hours and frequency caps.

**Phase 2 — merchant integrations:** order status and purchased-product data only through authorised connectors and a reviewed privacy notice; no card details.

**Phase 3 — official social insights:** start with permitted page/business-level aggregate metrics. Add individual-level integrations only where the provider explicitly supports the intended purpose and user authorisation.

**Phase 4 — controlled delivery:** in-product recommendations first; opt-in notifications next; external posts/messages only through official APIs, approved scopes, exact previews and audit logs.

**Phase 5 — independent review:** security/privacy review, platform-policy review, local legal review, accessibility testing, abuse testing and rollback drills for every market and channel.

## 10. Acceptance tests

- Missing consent or API scope -> no collection, profile update or delivery.
- Revoked connector/consent -> queued marketing cancelled and future ingestion stopped.
- Expired/old signal -> decays or is removed according to documented retention.
- Like/view/search alone -> never labelled a confirmed purchase or stable personal trait.
- Sensitive-category signal -> excluded from marketing profile and targeting.
- User opts out -> no marketing delivery through any integrated channel covered by that opt-out.
- Quiet hours/frequency cap -> message is delayed or dropped safely.
- External post/DM -> requires an authorised API path, correct destination, and required preview/approval.
- Provider returns no permission -> integration state is unavailable, not bypassed.
- User requests correction/deletion -> profile, derived interests and queued content are updated/deleted according to applicable requirements.
- Every profile update and send decision records a minimal audit event without logging secret tokens or unnecessary raw content.

## 11. Research and policy references

- India's DPDP Rules 2025 explanatory note: clear, standalone notice should describe personal data, purpose, enabled uses and withdrawal/rights/complaint paths. Applicability and commencement must be reviewed for each feature: https://www.meity.gov.in/writereaddata/files/Explanatory-Note-DPDP-Rules-2025.pdf
- Google personalised advertising policy: sensitive interest categories have targeting restrictions, and advertiser data use is subject to policy and law: https://support.google.com/adspolicy/answer/143465?hl=en
- Google Ads Data Hub policies: require necessary consents, prohibit re-identification and impose restrictions on sensitive information: https://developers.google.com/ads-data-hub/resources/policies
- Google Privacy Policy / personalisation controls illustrate that users can control activity use and ad personalisation: https://policies.google.com/privacy and https://safety.google/intl/en_us/settings/ad-settings/

These sources illustrate constraints and design patterns; they do not establish permissions for Meta, TikTok, X, LinkedIn, Google or any other platform. Verify each provider's current official API and business messaging policies before implementation.
