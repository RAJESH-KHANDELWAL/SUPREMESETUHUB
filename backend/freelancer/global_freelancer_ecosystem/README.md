# GLOBAL FREELANCER ECOSYSTEM — Research Engine

The engine searches public web-index APIs for freelance work, prospective clients, and business opportunities in Bharat (India) or the global market. It returns source URLs, snippets, provider provenance, and a keyword relevance score.

## Configure one search provider

- Brave Search API: `BRAVE_SEARCH_API_KEY`
- Google Programmable Search: `GOOGLE_CSE_API_KEY` and `GOOGLE_CSE_CX`

Set secrets in the deployment environment (for example Render Environment), never in source control. Without at least one provider configured, the API returns a clear configuration-required status rather than fabricated results.

## API

Authenticated endpoint: `GET /api/v1/global-freelancer-ecosystem/research/search?q=translation&market=bharat&category=freelance_work&limit=10`

- `market`: `bharat` or `global`
- `category`: `freelance_work`, `clients`, `business`, or `research`
- `limit`: 1–20

Status endpoint: `GET /api/v1/global-freelancer-ecosystem/research/status`

Search results are leads, not proof of a genuine person, client, job, or payment. The relevance score measures keyword overlap only; it is not a trust score. Always inspect the original source and independently verify counterparties. The engine does not scrape login-gated sites or harvest private personal details.

## Current boundaries

This implementation searches public indexes via official APIs. It does not autonomously create accounts, message people, apply for jobs, pay fees, or guarantee income. Real provider credentials and a deployed environment are required for live search.
