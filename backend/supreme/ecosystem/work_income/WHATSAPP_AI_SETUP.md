# WhatsApp AI setup — SUPREME ECOSYSTEM

## What was added

- `GET /api/v1/supreme-ecosystem/whatsapp/status` — reports missing setup variables.
- `GET /api/v1/supreme-ecosystem/whatsapp/webhook` — Meta webhook verification.
- `POST /api/v1/supreme-ecosystem/whatsapp/webhook` — validates Meta's `X-Hub-Signature-256`, receives incoming text messages, asks the configured OpenAI model for a reply, and sends the reply through WhatsApp Cloud API.
- `POST /api/v1/supreme-ecosystem/whatsapp/send-approved-template` — sends one approved template to one recipient only when the caller explicitly confirms recipient opt-in. This route is protected by the app's private-by-default authentication middleware.

## Required deployment environment variables

Set these in the backend hosting provider's secret/environment settings. Never commit real values to GitHub.

- `WHATSAPP_ACCESS_TOKEN` — Meta WhatsApp Business Platform access token.
- `WHATSAPP_PHONE_NUMBER_ID` — the Cloud API phone-number ID (not merely the visible phone number).
- `WHATSAPP_APP_SECRET` — Meta app secret, used to verify webhook signatures.
- `WHATSAPP_VERIFY_TOKEN` — a private string you choose and enter in Meta webhook setup.
- `WHATSAPP_GRAPH_API_VERSION` — a currently supported Graph API version, e.g. the version shown in Meta's current setup instructions.
- `WHATSAPP_OUTREACH_TEMPLATE_NAME` — the exact name of an approved WhatsApp message template for proactive outreach.
- `OPENAI_API_KEY` — OpenAI API key for AI-generated replies.
- Optional: `OPENAI_MODEL` — defaults to `gpt-4.1-mini`.

## Setup checklist

1. Create/configure a Meta business portfolio and WhatsApp Business Account, then enable the official WhatsApp Cloud API for the business number.
2. Confirm the number can be registered with Cloud API. A number already being used in the WhatsApp consumer/business app may need an official migration or supported coexistence setup; do not assume the same number can be used by both without checking Meta's current options.
3. Deploy this backend to a public HTTPS URL and add the environment variables in the hosting dashboard.
4. In Meta's developer dashboard, configure the callback URL as `https://YOUR_BACKEND_HOST/api/v1/supreme-ecosystem/whatsapp/webhook` and use the same `WHATSAPP_VERIFY_TOKEN`. Subscribe the WhatsApp Business Account to message webhooks.
5. Set up and get approval for the outbound message template whose exact name is `WHATSAPP_OUTREACH_TEMPLATE_NAME`.
6. Check `GET /api/v1/supreme-ecosystem/whatsapp/status` and `GET /api/v1/supreme-ecosystem/integrations`.
7. Test using a number you control and have opted in. Confirm webhook verification, incoming AI reply, provider message ID, and delivery-status webhooks before relying on it.

## Important safety and current limitations

- This code has been committed but has **not** been deployed or end-to-end tested. It must not be described as live yet.
- It does not discover phone numbers, scrape job posts, or send bulk messages.
- Proactive template sending requires explicit recipient opt-in. The endpoint is single-recipient, requires owner authentication, and requires the approved template name to match server configuration.
- AI replies only to incoming text messages in this initial implementation. It ignores media-only messages and does not yet persist conversation history or message deduplication across restarts/instances.
- Contact saving and screenshot sharing cannot be performed by an API; the recipient must do those actions on their own phone.
- Use WhatsApp's current messaging policies, template rules, opt-in requirements, and applicable privacy law. Do not message scraped or unwilling recipients.
- Never put access tokens, app secrets, or API keys in source code, frontend JavaScript, GitHub commits, or chat messages.
