# SUPREMESETUHUB Global Language, Translation and Speech Foundation

## What this change adds
- A separate human-language catalogue (regional language variants included) and programming-language catalogue.
- `GET /api/v1/languages/catalog` to load both catalogues.
- `POST /api/v1/languages/translate` for one text and `POST /api/v1/languages/translate/batch` for up to 40 interface strings.
- The SUPREME frontend language selector loads the catalogue and attempts to translate page text after the user selects a target language.
- A browser speech-recognition UI that sends final recognized utterances through the translation API and can read translated text aloud with browser speech synthesis.
- Automated tests for catalogue separation, missing provider configuration, unsupported targets and batch limits.

## Configure a translation provider
The translation service is deliberately not hard-coded to a vendor. Configure a trusted HTTPS endpoint that implements the LibreTranslate-compatible `POST /translate` request/response contract:

- `SUPREME_TRANSLATION_API_URL=https://your-approved-provider.example`
- `SUPREME_TRANSLATION_API_KEY=...` (only if your provider requires it)

The service appends `/translate` to the configured base URL. Keep credentials in deployment environment secrets, never in frontend code or Git. Confirm the provider's supported language codes, data retention, privacy policy, rate limits, pricing and terms before production use. The catalogue is a discovery list, **not a guarantee that every provider supports every listed language**.

## Important scope boundaries
- The catalogues cover many widely used human and programming languages; no static list can truthfully promise every language, dialect, framework, legacy language or future language worldwide.
- Programming languages are catalogued separately. They are not machine-translated like human languages; code must be preserved, syntax-highlighted, documented or localized carefully.
- Browser speech recognition/synthesis availability varies by browser, operating system and language. Speech recognition often uses a browser/platform service and may send audio to that provider.
- The current microphone feature translates speech heard by the user's microphone. It does **not** connect to remote participants' WebRTC audio, translate an entire live video-call audio stream, dub video audio tracks, or provide lip-synced translated voices. Those require an explicit WebRTC/media pipeline, streaming speech-to-text, streaming translation, text-to-speech, latency management, consent, and a provider configured for each stage.
- Selecting a target language translates text nodes in the loaded page when a provider is configured. Content loaded later by other apps, canvas-rendered text, images, embedded third-party pages, PDFs, and media audio require their own integrations.
- Translation submits selected page text and recognized speech to the configured provider. Disclose this clearly to visitors and obtain any required consent. Do not send passwords, private messages, payment details or other sensitive fields for translation.
- Machine translation may be wrong. Keep original text available for review; critical, legal, financial and medical content requires human review.

## Production readiness still required
Before enabling globally for all visitors, test the provider's actual supported language pairs and regional codes, add rate limiting and abuse controls, cache repeated static UI translations, avoid translating secrets or private content, validate privacy/data residency requirements, and test in supported browsers. For video calls, design a dedicated consent-aware WebRTC integration instead of claiming the microphone demo already translates remote call audio.
