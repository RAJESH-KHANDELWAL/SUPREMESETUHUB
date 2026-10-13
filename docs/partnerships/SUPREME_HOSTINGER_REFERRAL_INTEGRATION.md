# SUPREME × HOSTINGER REFERRAL INTEGRATION

**Record date:** Tuesday, 13 October 2026  
**Time zone for application events:** Store timestamps in UTC; display in Asia/Kolkata for the India owner.  
**Status:** Repository configuration and frontend CTA proposed in this branch; production deployment and purchase-level tracking are not verified.

## Owner-supplied program details
- Provider: Hostinger
- Exact referral URL: https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGLOBAL
- Account screenshot states: up to USD 180 per eligible referral; friend gets 20% off the first plan.
- These are account-screen claims and may change. Re-check current Hostinger terms, eligibility, payout conditions, exclusions and tax treatment before promotion.
- Account billing currency shown: INR; reward shown in USD. These are not the same balance.

## Ecosystem placement
- Registry: `GLOBAL-AFFILIATE-MARKETING-API-ECOSYSTEM`.
- Partner registry: `backend/core/global_ecosystem/global_core_ecosystem/partner_programs.py`.
- Frontend CTA: `frontend/supreme/index.html`.
- Validation schema: `schemas/partner_program_registry.schema.json`.

Place this link only on relevant hosting/domain/website-builder recommendations, affiliate pages, resource directories and educational content about creating websites. Do not inject it into unrelated pages, private messages, forms or every outgoing link. Keep an affiliate disclosure next to the link.

## Tracking truth
The repository can store the link and public program metadata. This change does **not** prove production deployment, implement backend click analytics, or connect to Hostinger purchase/commission data.

Hostinger's referral dashboard is the source of truth for attribution and rewards. A click is not proof of purchase. SUPREME cannot automatically know who purchased, which plan they bought, or the commission status unless Hostinger explicitly exposes those fields through an authorized dashboard/API/callback/export and its terms allow their use.

## Safe future tracking
1. Preserve the exact referral URL.
2. If first-party click analytics are later implemented, collect only necessary event ID, program ID, UTC timestamp, page/campaign identifier and aggregate counters. Avoid fingerprinting and unnecessary personal data.
3. Give clear notice and obtain any consent required for analytics/storage.
4. Keep clicks separate from confirmed purchases and commissions.
5. Import purchase/commission status only through a documented, provider-approved API/callback or official report export; validate authenticity and access scopes.
6. Keep reporting private behind authentication and role-based access; never commit tokens or secrets to Git.
7. Reconcile rewards with Hostinger's official dashboard/statement.

## Affiliate disclosure
> **Affiliate disclosure:** This page contains my Hostinger referral link. If you sign up through it and qualify under Hostinger's current program rules, I may receive a referral reward. Offers and eligibility are controlled by Hostinger and may change. Your account and purchase details remain with Hostinger unless it provides an authorized reporting method.

## Go-live checklist
- [ ] Confirm current program status and terms.
- [ ] Confirm intended website/page and disclosure placement.
- [ ] Validate the exact link in a browser.
- [ ] Test frontend build and deployed page.
- [ ] Complete privacy review before enabling click analytics.
- [ ] Verify whether Hostinger provides an approved purchase/commission reporting interface.
- [ ] Never mark a purchase/commission confirmed from a click alone.

This does not guarantee rewards, establish an agency relationship, provide SUPREME access to Hostinger account data, or certify legal compliance.
