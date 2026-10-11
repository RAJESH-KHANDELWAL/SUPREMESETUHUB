# WhatsApp AI setup — SUPREME ECOSYSTEM

## What was added

- `GET /api/v1/supreme-ecosystem/whatsapp/status` — reports missing setup variables.
- `GET /api/v1/supreme-ecosystem/whatsapp/webhook` — Meta webhook verification.
- `POST /api/v1/supreme-ecosystem/whatsapp/webhook` — validates Meta's `X-Hub-Signature-256`, receives incoming text messages, asks the configured OpenAI model for a reply, and sends the reply through WhatsApp Cloud API.
- `POST /api/v1/supreme-ecosystem/whatsapp/send-approved-template` — sends one approved template to one recipient only when the caller explicitly confirms recipient opt-in. This route is protected by the app's private-by-default authentication middleware.

## Your current starting point: regular WhatsApp app with a separate AI tool

A normal WhatsApp chat AI is not automatically connected to this repository. The backend cannot read messages from the consumer WhatsApp app unless the number is connected through a supported official integration.

Recommended onboarding sequence:

1. **Protect existing chats first.** In WhatsApp, check Settings → Chats → Chat backup and complete a backup before changing apps or account setup. Do not uninstall the existing app until you have confirmed the backup.
2. **Choose the number strategy.** If you want to keep using the same number, review Meta's current WhatsApp Business Platform onboarding/coexistence eligibility. A supported Business App + Platform coexistence option is available to some businesses, but availability and onboarding requirements can vary. Do not assume a normal consumer account is already API-enabled.
3. **If prompted to convert to WhatsApp Business, read the in-app instructions carefully** and confirm the backup is available first. Keep the same number only if the official flow explicitly supports it for your account.
4. **Create/configure the Meta developer app and WhatsApp Business Account** and use the official Cloud API getting-started flow. Start with a Meta-provided test number and a phone you control if you want to validate the code before changing your personal number.
5. Only after the Meta app, number, permissions, and webhook are configured should this SUPREMESETUHUB backend receive incoming messages and send AI replies.

Official Meta guidance: https://faq.whatsapp.com/5773272372736965/ and https://about.fb.com/news/2025/09/bringing-new-tools-to-help-businesses-boost-engagement-customer-support-and-discoverability/

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
