# SUPREME — HOSTINGER, WORDPRESS, PRINT-ON-DEMAND & PLUGIN BLUEPRINT

## Owner identity rule

Both owner-supplied Gmail accounts are **co-primary SUPREME owner/admin identities**. The current environment-variable names `SUPREME_OWNER_PRIMARY_EMAIL` and `SUPREME_OWNER_SECONDARY_EMAIL` are retained for backwards compatibility only; the second variable does **not** mean a lower authority level. Store both actual addresses only in private deployment settings. Do not commit real email addresses, passwords, OAuth secrets, or API tokens to this repository.

Recommended private environment configuration:
- `SUPREME_OWNER_PRIMARY_EMAIL` — first co-primary owner/admin Gmail
- `SUPREME_OWNER_SECONDARY_EMAIL` — second co-primary owner/admin Gmail
- `SUPREME_OWNER_EMAILS` — optional comma-separated owner email registry, if the runtime uses it
- `SUPREME_OWNER_RECOVERY_EMAIL` — optional dedicated recovery address, only if one is explicitly chosen
- `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI` — required for Google OAuth, configured privately

An email address in the registry does not itself grant login or admin rights. Authentication must verify the Google identity, match an allowlisted owner email, enforce server-side authorization, and use secure sessions/tokens. Recovery contact is separate from owner identity.

## Hostinger

- Hostinger account/provider: registered in the SUPREME partner/integration documentation.
- Referral URL to use: https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGROWTH
- Referral configuration is repository-level until deployed and verified.
- Hostinger purchase, commission, and referral conversion records must be confirmed in the Hostinger partner dashboard or an approved reporting API.
- For WordPress hosting, choose a plan that supports the actual expected traffic, backups, staging, SSL, and resource needs; verify current plan limits in Hostinger before purchase.

## WordPress platform baseline

Use WordPress as the content/site layer and SUPREME as the central registry/orchestration layer. Connect through documented, authenticated APIs or WordPress REST API/Application Passwords with least privilege. Do not store WordPress administrator passwords in GitHub.

WordPress database environment placeholders already exist in `backend/.env.example`:
- `WORDPRESS_DB_HOST`
- `WORDPRESS_DB_NAME`
- `WORDPRESS_DB_USER`
- `WORDPRESS_DB_PASSWORD`
- `WORDPRESS_DB_PORT`
- `WORDPRESS_TABLE_PREFIX`

These are placeholders only; a live database connection is not implied.

## WordPress plugin list — preserved from the prior planning list

Install only the plugins required by the actual site features. Avoid activating overlapping membership, community, messaging, or caching plugins together without compatibility tests.

### Community, member profiles, groups and messaging
- BuddyPress — community and member profiles
- BuddyPress Reorder Tabs — reorder BuddyPress profile tabs
- BP Better Messages — community messaging
- BuddyBoss Platform — **alternative** community platform; evaluate instead of stacking it with BuddyPress if features overlap
- Youzify — profile/community UI enhancement; check compatibility with the chosen community stack
- bbPress — forums
- rtMedia **or** MediaPress — member media/gallery features; choose one after testing
- Ultimate Member **or** WP Ulike — membership/profile or engagement use cases differ; do not treat them as interchangeable
- MemberPress **or** Paid Memberships Pro **or** Restrict Content Pro — choose one membership/paywall system

### Jobs, pages and visual builder
- WP Job Manager — job listings
- Elementor — page builder
- Crocoblock — optional Elementor add-ons; validate license and needed widgets before use

### Operations and reliability
- WP Super Cache — page caching; check compatibility with hosting/server cache
- WP Mail SMTP — transactional email delivery setup
- UpdraftPlus — backups; configure off-site storage and test restore

### Installation guardrails
- Verify each plugin's current maintenance status, WordPress/PHP compatibility, license, pricing, security advisories, and support before installation.
- Keep WordPress core, theme, and plugins updated; use staging and backups before updates.
- Install one plugin per feature where practical; don't enable competing cache, membership, or community stacks by default.
- Configure SMTP credentials, backup destination credentials, payment keys, and other secrets only in the private WordPress/hosting dashboard.

## Print-on-demand (POD)

### Provider options already discussed
- Qikink — WooCommerce order bridge foundation is recorded in the repository; production order submission remains gated on provider approval, correct product/SKU mapping, authorized credentials, and sandbox/test orders.
- Printify — setup documentation exists; live store connection, product publishing, order sync, and fulfillment are not confirmed.

### Required end-to-end path
1. Set up WooCommerce and the approved POD provider account.
2. Connect the provider using its official plugin/API and private credentials.
3. Map every WooCommerce product/variation to the provider's exact catalog item, size, color, print area, and SKU.
4. Test product publishing, shipping/tax display, payment success, order creation, provider submission, tracking updates, cancellation/refund handling, and failure retries.
5. Keep automatic live order submission disabled until sandbox/staging tests and provider authorization pass.
6. Verify a real low-risk order only when the account owner explicitly authorizes it.
7. Track product cost, shipping, platform/payment fees, taxes, refunds, and margin; do not claim a successful fulfillment until the provider confirms it.

## Readiness status

| Area | Repository status | What is still needed |
|---|---|---|
| Hostinger referral | Link/configuration documented in PR #34 | Merge, deploy, click-test and verify partner dashboard attribution |
| Google owner identities | Private env configuration proposed in PR #35 | Merge, set both owner emails privately, configure OAuth, authorize and test |
| WordPress database | Environment placeholders exist | Real private DB values and tested connection |
| WordPress plugins | Planning list documented here | Choose compatible stack, install/configure on staging, test and deploy |
| Qikink | WooCommerce bridge foundation previously merged | Provider approval, credentials, SKU map, sandbox and authorized end-to-end test |
| Printify | Setup documentation recorded | Connect store and verify publishing, sync and fulfillment |
| Production | Not claimed | CI, staging, security review, backup/restore, and production smoke tests |

This file is a blueprint and registry document. It does not install WordPress plugins into a live site or prove that external services are connected.
