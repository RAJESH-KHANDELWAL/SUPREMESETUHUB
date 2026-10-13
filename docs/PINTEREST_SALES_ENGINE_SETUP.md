# Pinterest — PICS & VIDEO KHAJANA + Sales Engine Setup

**Purpose:** Pinterest is the ecosystem's visual discovery and distribution channel for photos, videos, designs, inspiration, and product/service Pins. It is not a separate media-storage platform and Pins are not a substitute for retaining owned original files and usage rights.

## Status
- Planning/implementation checklist prepared in GitHub.
- Pinterest account ownership, Business account status, claimed domains, catalog eligibility, API access, and live analytics are not yet verified.
- No live Pinterest settings were changed by this repository documentation.

## Target flow
Owned/rights-cleared visual asset → Pinterest board and Pin → relevant brand-gate landing page or WooCommerce product → consent-aware analytics and attribution → lead/order → payment and cost reconciliation → revenue/profit dashboard.

Pinterest is a discovery channel, not a guarantee of sales. Measure outbound clicks, sessions, leads, carts, paid orders, refunds, fees, provider cost and net contribution.

## Phase 0 — Establish account ownership and destination
1. Identify the owner's existing Pinterest account. Prefer converting/using the owner-controlled account as a Pinterest Business account rather than creating duplicates.
2. Secure owner-controlled email, recovery and MFA. Never place passwords, access tokens, client secrets or recovery codes in GitHub or chat.
3. Confirm which of the four approved brand gates the Pinterest profile represents. Keep brand content and destination links consistent; do not claim all domains until the owner has verified control and the selected profile strategy is clear.
4. Claim the chosen owned domain through the verification method Pinterest provides (HTML tag, file, or DNS record as available). Never invent verification values.
5. Confirm public HTTPS landing pages work on mobile and the storefront's coming-soon state is understood before sending public traffic.

## Phase 1 — Visual treasure taxonomy
Use Pinterest boards as the organized discovery catalogue:
- Digital Dukan & Products
- Website & Digital Business Services
- Business Growth & Skills
- Real Estate & Property Education (only relevant content)
- Personal Development & Relationships (responsible, relevant content)
- Bharat, Travel & Visual Inspiration
- Video Ideas & Tutorials

Board names should be keyword-led and reflect real content. Create only the boards needed for the actual available asset library; avoid thin or duplicate boards.

## Phase 2 — Asset and Pin quality
For every asset, track:
- asset ID, original file location, owner/creator, licence/permission, publish status, and content category;
- Pin title, natural keyword-led description, board, destination URL, alt text where supported, publication date, and UTM campaign;
- product/variant SKU only when it actually maps to a WooCommerce product and the chosen POD workflow.

Use high-quality vertical creative (commonly 2:3), readable text, clear CTA, accurate claims, and one relevant destination per Pin. Use only rights-cleared photos, videos, music, fonts and artwork. Do not scrape other users' media or mass-publish repetitive duplicates.

## Phase 3 — Commerce
- Begin with a small, manually reviewed set of Pins and confirm every destination link.
- If the account and region are eligible, investigate Pinterest catalog/shopping connection to WooCommerce. Validate feed approval, product IDs, price, currency, stock, image and URL; do not assume approval.
- Qikink remains the selected print-on-demand provider. Ensure WooCommerce SKU/variant and fulfillment settings are verified before promoting a product.
- Do not enable ads or incur paid spend without explicit owner approval.

## Phase 4 — Attribution
Use stable UTMs, for example:
- utm_source=pinterest
- utm_medium=organic_social
- utm_campaign=<approved_campaign_slug>
- utm_content=<pin_or_creative_id>

Avoid personally identifiable information in URLs. Verify analytics events and prevent duplicate events. Report Pinterest impressions/saves separately from outbound clicks, qualified leads, paid orders, refunds, collected revenue, costs and net contribution.

## Phase 5 — Publishing automation (only after manual validation)
Assess the official Pinterest API (currently versioned API, verify current docs and access requirements before implementation) for authorized Pin/board creation. Do not assume API access is approved.
- Use OAuth/app authorization and least-privilege scopes.
- Keep tokens in the hosting secret store, not the repository or frontend.
- Use a durable queue, scheduled publishing, deduplication/idempotency, rate-limit handling, bounded retries, error/dead-letter queue, logs and alerts.
- Provide manual review/publish fallback.
- Respect platform terms, rate limits, copyright, privacy and consent.
- Test against a small approved batch before scheduling at scale.

## Acceptance checklist
- [ ] Owner confirms account and Business status.
- [ ] Profile identity, bio, logo and destination are consistent with the approved brand gate.
- [ ] Chosen domain successfully claimed; verification method documented without exposing secrets.
- [ ] Initial relevant boards created.
- [ ] A small quality-controlled Pin batch is published with working HTTPS destinations.
- [ ] UTM attribution and analytics events are verified end-to-end.
- [ ] WooCommerce catalog status is confirmed if commerce features are used.
- [ ] One test lead and (where safe/authorized) test order are attributed and reconciled.
- [ ] API automation is authorized, secure, retry-safe, rate-limited and observable before scheduled publishing.
- [ ] Original files and asset rights are retained outside Pinterest.

## Next required owner input
Only the minimum needed to proceed:
1. Does an existing Pinterest account already exist, and is it Business?
2. Which first destination is intended: RAJESHKHANDELWALOFFICIAL.COM, DRRAJESHKHANDELWALIBC.COM, SUPREMESETUHUB, or relevant links across all approved brand gates?
3. Where are the existing photos/videos currently stored (computer/phone, cloud, or existing social platforms)?

Do not claim account setup, domain verification, catalog approval, API connection, automation, or revenue tracking is complete until direct evidence verifies it.
