# InfinityFree temporary frontend deployment

## Intended architecture

- GitHub repository `RAJESH-KHANDELWAL/SUPREMESETUHUB` on `main` remains the source of truth.
- InfinityFree is a temporary static/PHP hosting target for the public SUPREME frontend.
- Render remains the temporary runtime for the FastAPI backend/API. InfinityFree free hosting is not the replacement for the Python backend.
- The workflow builds the public SUPREME home from `frontend/supreme/supreme-ecosystem/home-html.html` and its CSS/JS, then uploads the generated `site/` package over FTP.
- The workflow does not deploy the private owner dashboard as the homepage, does not deploy backend secrets, and does not connect WordPress, Qikink, Shopify or Etsy accounts.

## One-time GitHub repository secrets

In GitHub: repository → Settings → Secrets and variables → Actions → New repository secret.

Add these four secrets using the exact values from InfinityFree's **FTP Details** page:

- `INFINITYFREE_FTP_SERVER`: FTP hostname/server shown by InfinityFree.
- `INFINITYFREE_FTP_USERNAME`: FTP username shown by InfinityFree (do not assume it is the account username).
- `INFINITYFREE_FTP_PASSWORD`: FTP password from InfinityFree.
- `INFINITYFREE_FTP_SERVER_DIR`: exact document-root directory for the target domain, with trailing slash. Get this from the FTP/file manager for the chosen domain; do not guess it.

Never paste FTP credentials into GitHub issues, commits, chat messages or source files.

## Deploy

1. Confirm the intended target domain in InfinityFree. This workflow does not decide among the account's multiple domains.
2. Add all four secrets above.
3. Open GitHub → Actions → **Deploy SUPREME temporary frontend to InfinityFree** → Run workflow.
4. Inspect the workflow log. Do not share secret values; report only success/failure and the redacted error text.
5. Open the selected domain and check home, CSS, JavaScript, navigation and mobile layout.
6. Check HTTPS/SSL separately in InfinityFree. A successful FTP upload does not prove DNS propagation or SSL is ready.

After the first successful manual run, matching changes pushed to `main` trigger an automatic deployment.

## Safety and limitations

- The workflow uploads only the generated static `site/` directory. It does not deploy the FastAPI backend, PHP database services, private dashboard data, payment code or provider credentials.
- API calls continue to use the existing Render/backend URLs currently in the frontend. CORS and the exact production API URL still need live browser verification.
- FTP credentials and the correct remote document-root path are required before any upload can run.
- Do not enable live sales/fulfilment based only on a successful static site deployment.
