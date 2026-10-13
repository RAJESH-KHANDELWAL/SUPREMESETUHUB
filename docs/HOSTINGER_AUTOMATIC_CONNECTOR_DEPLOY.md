# Hostinger automatic WordPress connector deployment

This workflow deploys **only** the SUPREMESETUHUB Connector plugin files to an already-installed plugin directory on the Hostinger WordPress site. It does not install/activate the plugin, deploy the FastAPI backend, configure the API URL, or connect Qikink.

## One-time GitHub configuration

In **Repository → Settings → Secrets and variables → Actions**, create these repository/environment secrets under the `production` environment:

- `HOSTINGER_FTP_SERVER`: the FTP server hostname shown in Hostinger hPanel.
- `HOSTINGER_FTP_USERNAME`: the FTP username shown in hPanel.
- `HOSTINGER_FTP_PASSWORD`: the FTP password (never commit or paste it into chat).
  
Create this Actions variable under the same scope:

- `HOSTINGER_WP_PLUGIN_DIR`: the exact remote directory from the FTP account's root, ending in `/wp-content/plugins/supremesetuhub-connector/`. Example only: `public_html/wp-content/plugins/supremesetuhub-connector/`. Use the actual path shown by Hostinger; do not assume the example is correct.

Use FTPS where supported. Do not enable this workflow until a current WordPress backup exists and the FTP path has been confirmed to be the correct site's plugin directory.

## Run and verify

1. Merge this workflow only after reviewing it and configuring the production environment protections.
2. Open **Actions → Deploy SUPREME WordPress Connector to Hostinger → Run workflow**.
3. Verify the run succeeds, then open WordPress Admin → Plugins and confirm **SUPREMESETUHUB Connector** remains active.
4. In WordPress Admin → Settings → SUPREMESETUHUB, enter the real public HTTPS API base URL and run the connector test.

## Important boundaries

- Push-to-main changes under the connector directory trigger automatic file deployment after setup; this removes repeated manual ZIP uploads for that plugin.
- The workflow intentionally does not delete remote files and does not install/activate plugins.
- It does not deploy the FastAPI backend. That backend needs a supported persistent Python host (for example, an owner-configured Render service or Hostinger VPS), a real HTTPS URL, and persistent storage.
- A green GitHub workflow means files were uploaded; the WordPress-to-API connection is not proven until the in-dashboard connection test succeeds.
- Never put hosting credentials, API keys, Qikink credentials, or payment secrets in repository files or chat.
