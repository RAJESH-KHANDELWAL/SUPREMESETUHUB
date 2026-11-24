# Global Education Learning Training Service Work Business CORE Ecosystem

Commercial capability taxonomy for the education economy. This layer classifies services delivered, work performed and business models; it consumes canonical domain IDs from the sibling Global Education Learning Training CORE.

## Coverage
Includes early-years and school services; tutoring; open schooling; colleges and universities; research and publishing; ITI, trades and vocational learning; engineering, medical, law and agriculture training; business and STEM education; arts and sports academies; teacher development; corporate learning; apprenticeships; skills; EdTech, LMS, AI and computing; language and accessibility services; special-needs learning; assessment and exam preparation; accreditation advisory; career and placement services; entrepreneurship; adult literacy; study abroad; education supplies and infrastructure; franchises; marketplaces; counselling/support; events; software and incubation.

## Service / Work / Business classification
Every business-domain record is tagged with all three capability dimensions. The catalog is metadata only: it does not imply that a provider is licensed, accredited, verified or operational.

## Architecture
- `domain_catalog.py`: business capabilities and explicit canonical `core_domain_id` mappings.
- `catalog.py`: ecosystem identity and dependency metadata.
- `contracts.py`: typed business capability contract.
- `policy.py`: allowed and prohibited operations.
- `service.py`: search, filtering and integrity validation.
- `orchestrator.py`: inventory and dependency metadata.
- `manager.py`: public Python entry point (`get_manager()`).
- `manager.php`: PHP metadata facade.
- `tests/`: executable unit tests.

No payments, enrollment, credential issuance, admission/job guarantee, sensitive learner-record storage or training delivery is performed here. Operators must independently verify applicable laws, child safeguarding, privacy, accessibility and professional licensing.
