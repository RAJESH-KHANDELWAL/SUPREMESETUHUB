# Google AI API Ecosystem

Provider-level entry point for Google's AI developer services. The Gemini Developer API is implemented in the sibling `google_gemini_api_ecosystem` package; Vertex AI is implemented in `google_vertex_ai_api_ecosystem`.

## Responsibilities
- Present one consistent Google AI provider catalog to the application.
- Route Gemini Developer API usage to the Gemini adapter.
- Route Google Cloud Vertex AI usage to the Vertex AI adapter (Google Cloud project, IAM/service-account or supported OAuth credentials, region and model access are required).
- Keep credentials supplied by each account owner isolated. Do not treat a Gemini API key as a Vertex AI credential or vice versa.

## Current connection boundary
This package is a provider registry and adapter facade. It does not create Google Cloud projects, enable APIs, accept terms, grant IAM roles, or store user secrets. A production "Connect" flow must be mounted behind the platform's authenticated account system and backed by encrypted per-tenant secret storage. Never trust a tenant/account ID supplied only in the request body.
