# DigitalOcean Ecosystem

Provider-specific capability catalog and safe operation-planning package.

## Scope: Bharat to Global, Normal to Supreme
This provider package catalogs DigitalOcean infrastructure capabilities that may support workloads serving India/Bharat and global markets, from basic deployments through enterprise-scale and advanced research workloads. The scope includes cloud infrastructure for lawful applications across AI, software, websites, apps, business, finance, education, healthcare, communication, media, gaming, industry, agriculture, and lawful adult-only services.

Adult-oriented platform infrastructure is limited to lawful adults-only services with age assurance, informed consent, performer rights, privacy, moderation, reporting/takedown, secure payments, and jurisdiction-specific compliance. No minors, exploitation, trafficking, coercion, or non-consensual intimate imagery.

## Actual modules
- `constants.py`: provider identity and references to separately owned architecture layers.
- `models.py`: immutable capability and operation-request models.
- `catalog.py`: compute, Kubernetes, App Platform, serverless, managed databases, object/block storage, registry, networking, security, DNS, backup, monitoring, projects, and account capability metadata.
- `validation.py`: capability/action validation and explicit confirmation for potentially destructive operations.
- `service.py`: catalog facade and non-executing operation plans.
- `health.py`: catalog readiness report.
- `adapters/digitalocean_api.py`: dependency-injected API client protocol and adapter status.
- `tests/`: standard-library tests.

## Architecture boundary
This package does not absorb API, CORE, ENGINE, DATABASE, identity, secrets, or authorization. It owns provider metadata and request planning only. HTTP execution, credential storage, permission enforcement, persistence, retries, and audit logging belong in their separately owned runtime/integration layers.

## Integration status
The catalog is metadata, not a guarantee of account/region/plan availability. No credential check, live DigitalOcean API request, deployment, or resource mutation is performed here.

## Tests
From repository root: `python -m unittest backend.global_ecosystem.digitalocean_ecosystem.tests.test_ecosystem -v`
