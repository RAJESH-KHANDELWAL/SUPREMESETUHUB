# SUPREME × HOSTINGER REFERRAL INTEGRATION

**Record date:** Tuesday, 27 October 2026  
**Time zone for application events:** Store timestamps in UTC; display in Asia/Kolkata for the India owner.  
**Status:** Backend registry is configured in GitHub; production deployment, each account's link validity, frontend placement and purchase-level tracking are not verified.

## Owner-supplied program details
- Provider: Hostinger
- Primary referral URL shown in the supplied Hostinger dashboard: https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGLOBAL
- Dashboard states: earn up to USD 180 per eligible referral; referred friend gets 20% off when they make their first qualifying purchase.
- These are account-screen claims and may change. Re-check current Hostinger terms, eligibility, payout conditions, exclusions and tax treatment before promotion.
- Account billing currency shown: INR; advertised reward shown in USD. These are not the same balance.

## Registered owner referral links
The shared registry is `backend/core/global_ecosystem/global_core_ecosystem/hostinger_referrals.py`. All codes must be confirmed in their respective Hostinger accounts before promotion.

| SUPREME identity | Referral code | Link |
|---|---|---|
| DR RAJESH KHANDELWAL IBC | `RAJESHIBCGLOBAL` | https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGLOBAL |
| DR RAJESH KHANDELWAL IBC OFFICIAL | `RAJESHIBCGROWTH` | https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGROWTH |
| RAJESH KHANDELWAL OFFICIAL | `RAJESHGROWTH` | https://www.hostinger.com/in?REFERRALCODE=RAJESHGROWTH |
| RAJESH KHANDELWAL | `RAJESHGLOBAL` | https://www.hostinger.com/in?REFERRALCODE=RAJESHGLOBAL |

## Ecosystem placement
- Registry: `GLOBAL-AFFILIATE-MARKETING-API-ECOSYSTEM`.
- Partner catalog: `backend/core/global_ecosystem/global_core_ecosystem/partner_programs.py`.
- SUPREME-facing referral registry: `backend/core/global_ecosystem/global_core_ecosystem/hostinger_referrals.py`.
- Validation schema: `schemas/partner_program_registry.schema.json`.

Use this link only on relevant hosting/domain/website-builder recommendations, affiliate pages, resource directories and educational content about creating websites. Do not inject it into unrelated pages, private messages, forms or every outgoing link. Keep an affiliate disclosure next to the link.

## Tracking truth
The repository can store the links and public program metadata. This does **not** prove production deployment, implement backend click analytics, or connect to Hostinger purchase/commission data.

Hostinger's referral dashboard is the source of truth for attribution and rewards. A click is not proof of purchase. SUPREME cannot automatically know who purchased, which plan they bought, or the commission status unless Hostinger explicitly exposes those fields through an authorized dashboard/API/callback/export and its terms allow their use.

## Safe future tracking
1. Preserve each exact referral URL.
2. If first-party click analytics are later implemented, collect only necessary event ID, program ID, UTC timestamp, page/campaign identifier and aggregate counters. Avoid fingerprinting and unnecessary personal data.
3. Give clear notice and obtain any consent required for analytics/storage.
4. Keep clicks separate from confirmed purchases and commissions.
5. Import purchase/commission status only through a documented, provider-approved API/callback or official report export; validate authenticity and access scopes.
6. Keep reporting private behind authentication and role-based access; never commit tokens or secrets to Git.
7. Reconcile rewards with Hostinger's official dashboard/statement.

## Affiliate disclosure
> **Affiliate disclosure:** This page contains my Hostinger referral link. If you sign up through it and qualify under Hostinger's current program rules, I may receive a referral reward. Offers and eligibility are controlled by Hostinger and may change. Your account and purchase details remain with Hostinger unless it provides an authorized reporting method.

## Go-live checklist
- [ ] Confirm each referral code is still active in its Hostinger account.
- [ ] Confirm current program terms and intended website/page placement.
- [ ] Validate the exact links in a browser.
- [ ] Test backend and deployed frontend.
- [ ] Complete privacy review before enabling click analytics.
- [ ] Verify whether Hostinger provides an approved purchase/commission reporting interface.
- [ ] Never mark a purchase/commission confirmed from a click alone.

This does not guarantee rewards, establish an agency relationship, provide SUPREME access to Hostinger account data, or certify legal compliance.
