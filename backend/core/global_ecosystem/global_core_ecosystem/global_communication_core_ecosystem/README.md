# Global Communication Core Ecosystem

Provider-level, read-only control plane for communication capabilities in SUPREMESETUHUB.

## Source boundaries
- API catalog contract: `backend/api/global_ecosystem/global_api_ecosystem/global_communication_api_ecosystem/service.py`.
- Core owns provider identity, package mapping, capability policy, lifecycle contracts, health metadata and orchestration.
- Core MUST NOT import the API layer. API routes, schemas, provider adapters and network transport remain in the API/runtime layer.
- This Core catalog is a reviewed metadata mirror of the API provider list, not a second live integration registry.

## Canonical provider packages
- `aws_communication_provider_core_ecosystem` — Amazon Web Services Communication
- `aws_ses_provider_core_ecosystem` — Amazon SES
- `aws_sns_provider_core_ecosystem` — Amazon SNS
- `google_workspace_provider_core_ecosystem` — Google Workspace APIs
- `google_chat_provider_core_ecosystem` — Google Chat API
- `google_meet_provider_core_ecosystem` — Google Meet API
- `meta_provider_core_ecosystem` — Meta Platform APIs
- `meta_whatsapp_provider_core_ecosystem` — WhatsApp Business Platform
- `microsoft_provider_core_ecosystem` — Microsoft Graph APIs
- `microsoft_graph_provider_core_ecosystem` — Microsoft Graph
- `microsoft_teams_provider_core_ecosystem` — Microsoft Teams APIs
- `slack_provider_core_ecosystem` — Slack API
- `twilio_provider_core_ecosystem` — Twilio APIs
- `zoom_provider_core_ecosystem` — Zoom APIs
- `telegram_provider_core_ecosystem` — Telegram APIs

## Categories
The 15 category IDs are mirrored from the API service: messaging, email, sms, voice, video_meetings, social_messaging, customer_support, notifications, dating_relationships, sexual_wellness_education, adult_platform_directory, adult_creator_business, age_verification_safety, moderation_trust_safety, privacy_security.

The pre-existing category/capability directories are preserved as domain namespaces. They are not provider packages and are not automatically promoted to provider integrations.

## Integration truth
All 15 providers are `CORE_CATALOG_ONLY`; live connections are unverified. No credentials, API calls, message sending, SMS/OTP delivery, email sending, calling, video sessions, payments, content hosting or persistence are implemented here.

## Safety
Adult-only categories remain disabled by default. Restricted adult services require verified 18+ access, explicit consent, lawful content, regional legal review, privacy controls, reporting and appeals. Sexual-wellness education is not automatically classified as adult entertainment. Minors, non-consensual or exploitative content, and illegal content are prohibited.

## Google Product Core package standard
Each provider package contains README, manifest, config, contracts and the ten responsibility folders: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests. These are architecture scaffolds, not claims of completed provider adapters.
