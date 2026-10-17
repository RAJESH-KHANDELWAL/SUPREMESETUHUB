# Run GLOBAL FREELANCER RESEARCH in GitHub

This repository includes a manual GitHub Actions workflow that runs the existing public-source research engine and saves a downloadable report.

## One-time setup

In the repository, open **Settings → Secrets and variables → Actions → New repository secret** and add at least one provider:

- **Brave Search:** `BRAVE_SEARCH_API_KEY`
- **Google Programmable Search:** both `GOOGLE_CSE_API_KEY` and `GOOGLE_CSE_CX`

Do not put keys in code, workflow inputs, commits, or logs. The workflow reads them from GitHub Actions secrets. If no provider is configured, the run exits with a clear configuration error rather than inventing results.

## Run a search

1. Open the repository's **Actions** tab.
2. Select **GLOBAL FREELANCER RESEARCH**.
3. Click **Run workflow**.
4. Enter a query such as `translation retyping copywriting`.
5. Select the market (`bharat` or `global`), category, and result limit.
6. Open the completed run and download the `freelancer-research-report` artifact.

The artifact contains:
- `freelancer-research.md` — readable links and summaries
- `freelancer-research.json` — structured source results and metadata

## What this does and does not do

The workflow searches public web indexes through configured official APIs. It does not log in to job platforms, scrape private pages, send applications/messages, or guarantee that listings or payment claims are genuine. Results are **unverified leads**. Confirm the original listing, the client/employer, scope, deadline, and payment method before doing work. Never pay a registration fee to unlock a job or share passwords/OTPs.

This workflow runs only when manually triggered. It does not change the production backend or expose the provider keys.
