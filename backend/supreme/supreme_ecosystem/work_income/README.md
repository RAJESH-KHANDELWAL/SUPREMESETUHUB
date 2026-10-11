# SUPREME ECOSYSTEM — WORK & INCOME

This module is for discovering legitimate freelance and remote-work opportunities and safely directing the owner to official marketplace pages.

## Files

- `catalog.json`: official marketplace entry points, skill matches, verification checks, and anti-scam rules.
- `backend/api/supreme_work_income.py`: API for listing sources and preparing a WhatsApp click-to-chat link.

## API routes

- `GET /api/v1/supreme-ecosystem/work-income/status`
- `GET /api/v1/supreme-ecosystem/work-income/sources`
- `GET /api/v1/supreme-ecosystem/work-income/sources?skill=WordPress`
- `GET /api/v1/supreme-ecosystem/work-income/whatsapp-link?topic=WordPress%20projects`

The existing private-by-default middleware applies. Requests require the configured SUPREME owner session unless an explicit access policy is added.

## Important limits

- The directory contains official search/marketplace entry points, not a claim that any specific job is currently open or verified.
- The API does not scrape job boards or submit applications.
- The WhatsApp route creates a click-to-chat URL. The user must open WhatsApp and press Send.
- It does not send outbound WhatsApp messages, receive messages, or enable AI replies.
- Automatic WhatsApp messaging requires Meta WhatsApp Business Platform setup, an approved business number, access token, HTTPS webhook verification, signature checks, duplicate-event handling, policy-compliant messaging, and end-to-end testing.
- No income or hiring outcome is guaranteed.
- Never pay an employer to unlock a job; never share passwords or OTPs with recruiters.


## WhatsApp AI

See [WHATSAPP_AI_SETUP.md](./WHATSAPP_AI_SETUP.md) for official Cloud API setup, required environment variables, webhook configuration, consent-based approved-template outreach, and deployment/testing limitations.

New endpoints:
- `GET /api/v1/supreme-ecosystem/whatsapp/status`
- `GET /api/v1/supreme-ecosystem/whatsapp/webhook` (Meta verification)
- `POST /api/v1/supreme-ecosystem/whatsapp/webhook` (verified incoming message webhook with AI replies)
- `POST /api/v1/supreme-ecosystem/whatsapp/send-approved-template` (authenticated, one recipient, explicit opt-in, approved template only)

These endpoints are code scaffolding only until credentials are securely configured, Meta webhook subscriptions are completed, and an end-to-end test succeeds.
