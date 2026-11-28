# DEEPSEEK SEARCH API ECOSYSTEM

Canonical API-family catalog under `deepseek_api_ecosystem/`.

## Scope
Search tool requests where enabled for the account and model.

## Endpoint
`POST /v1/tools/search`

## Authentication
Use the server-side `DEEPSEEK_API_KEY` configured in the deployment secret manager. Never commit or expose credentials.

## Status
This directory is a catalog/documentation scaffold. It is not a separate live connector. Implement the request handler, validation, timeout/retry policy, error handling and authorized smoke test before claiming connectivity.
