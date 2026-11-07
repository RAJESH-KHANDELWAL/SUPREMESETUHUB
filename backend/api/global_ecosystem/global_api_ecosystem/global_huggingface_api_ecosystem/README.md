# GLOBAL HUGGING FACE API ECOSYSTEM

This ecosystem groups Hugging Face Hub and inference-related APIs used by SUPREMESETUHUB.

## Runtime configuration

Set `HF_TOKEN` in the backend deployment's secret/environment-variable manager. The legacy `HUGGINGFACEHUB_API_TOKEN` is also accepted. Never commit a token, place it in frontend code, or paste it into chat.

Use a Hugging Face user access token with only the permissions needed for the selected private/gated resources and inference products. Public model and dataset metadata may be readable without authentication, but this connector deliberately uses a server-side token.

## Implemented backend routes

- `GET /api/v1/connectors/huggingface/status` — checks token configuration and validates it with `/whoami-v2`.
- `GET /api/v1/connectors/huggingface/api/whoami` — authenticated account identity.
- `GET /api/v1/connectors/huggingface/api/models?search=...&limit=20` — search Hub models.
- `GET /api/v1/connectors/huggingface/api/datasets?search=...&limit=20` — search Hub datasets.
- `GET /api/v1/connectors/huggingface/api/spaces?search=...&limit=20` — search Spaces.

## Verification

After adding `HF_TOKEN`, restart/redeploy the backend and call the status route. It reports `CONNECTED` only after Hugging Face confirms the token. Without the secret, the correct status is `NEEDS_CONFIGURATION`; catalog presence is not live connectivity.

## Scope

This implementation provides authenticated identity and Hub search reads. It does not yet implement inference generation, endpoint provisioning, dataset uploads, Space management, or organization administration.
