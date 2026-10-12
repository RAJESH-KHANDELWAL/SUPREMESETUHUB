# SUPREMESETUHUB launch gates: backend, WordPress, CORE and POD

## Current verified repository state

- The FastAPI backend is the primary application runtime.
- The WordPress connector plugin is in `wordpress-plugin/supremesetuhub-connector/`.
- The public POD endpoint provides a read-only catalog and estimated pricing.
- Authenticated CORE/database/storage endpoints are implemented in the backend.
- CI verifies Python core/database tests, WordPress PHP syntax/API checks and the Android build.
- Repository merges do not deploy a service, install a WordPress plugin, set production secrets, or activate payments.

## Deployment decision required

Choose the runtime based on the Hostinger product actually purchased:

- **Hostinger shared WordPress hosting:** use it for WordPress and the connector plugin. Run FastAPI on a separate supported Python host with a stable HTTPS URL. Do not assume shared PHP hosting can keep a FastAPI process running.
- **Hostinger VPS:** the backend can run on the VPS using the repository's Docker configuration, but the VPS ID/API key or a secure SSH deployment setup must be configured in GitHub Actions secrets/variables first.

Do not publish a guessed backend URL. Verify `GET /health` returns HTTP 200 over HTTPS before entering the URL in WordPress.

## Persistent database and file storage

Configure these variables in the backend host's private environment:

- `SUPREME_DB_PATH`: an absolute path on persistent storage for the SQLite database.
- `SUPREME_FILE_STORAGE_DIR`: an absolute, writable path on persistent storage for uploaded files.
- `SUPREME_ADMIN_API_KEY` and the deployment's control/authentication secrets: long, unique secrets stored only in the host's secret manager.

The backend must be able to write to both directories after restart/redeploy. Test a database record and a file upload/download across a restart before declaring persistence ready. Back up the database and uploaded files. Never commit real secrets.

## WordPress activation

1. Download the `supremesetuhub-wordpress-plugin` ZIP artifact from the successful **Package WordPress Connector** GitHub Actions run.
2. In WordPress Admin, go to Plugins → Add New Plugin → Upload Plugin, upload the ZIP and activate it.
3. Open Settings → SUPREMESETUHUB, enter the verified HTTPS API base URL and save.
4. Use **Test Backend Connection**.
5. Put one shortcode on a draft page, test desktop/mobile, then publish:
   - `[supremesetuhub_status]`
   - `[supremesetuhub_pod_catalog market="IN"]`
   - `[supremesetuhub_digital_catalog market="IN"]`

The plugin calls the public read-only catalog endpoints. It does not currently expose checkout, paid digital delivery, or supplier order submission.

## Print-on-demand monetization gates

Before accepting real money, implement and test all of the following:

1. A chosen print provider with a real account, current product/variant catalogue, production costs, shipping costs, serviceable countries and API credentials.
2. A persisted order state machine and idempotent order creation.
3. A payment gateway account in live mode with verified webhook signatures, reconciliation, refunds and failure handling.
4. A supplier submission workflow that runs only after verified payment and can recover safely from retries.
5. Tax/shipping disclosure, privacy/returns policy, customer support details and a test purchase from checkout through fulfillment and refund.
6. Private digital download authorization and expiring access where applicable.

The current catalog's prices are estimates, not guaranteed margins or live supplier quotes. Do not label checkout or fulfillment as live until these gates pass.
