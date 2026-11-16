# AWS Product Ecosystem Standard

Each AWS service-family Core package follows the Google Core package boundary while retaining AWS service semantics.

Required package files: README.md, __init__.py, ecosystem_config.py, ecosystem_manifest.json and service.py.

Required subfolders: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests.

Core is metadata-first and read-only. Authentication directories define context and contract boundaries only. AWS credential resolution, SigV4 request signing, SDK clients and HTTP/API calls belong to the AWS API layer. Persistent resource state belongs to Storage/Database. Job execution belongs to Runtime/Engine. User authorization, confirmations and workflows belong to Application.

Every AWS operation must be authorized against the actual IAM principal, account, region, resource ARN and requested action. Elevated and destructive actions require explicit authorization and auditable approval. A family remains catalog-only until independent integration tests verify its deployed adapter and account-level access.
