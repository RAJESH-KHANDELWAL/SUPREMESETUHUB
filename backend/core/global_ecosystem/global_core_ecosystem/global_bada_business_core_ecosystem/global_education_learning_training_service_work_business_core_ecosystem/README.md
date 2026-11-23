# Global Education Learning Training Service Work Business CORE Ecosystem

Commercial classification and metadata for education-related services, professional work and business models. It consumes the canonical taxonomy from the sibling Global Education CORE rather than duplicating it.

## Coverage
Tutoring/coaching; admissions guidance; vocational and professional training; corporate learning; online courses/LMS; teacher development; career services; exam preparation; language training; accessibility; education consulting; curriculum/research services; student/parent support; franchises and learning marketplaces.

## Architecture
- `domain_catalog.py`: 15 business domains mapped to canonical `core_domain_id` values and tagged SERVICE, WORK and BUSINESS.
- `catalog.py`: business-layer identity and metadata.
- `contracts.py`: typed business capability contract.
- `policy.py`: allowed/prohibited operations.
- `service.py`: search, filtering and validation.
- `orchestrator.py`: inventory and dependency metadata.
- `manager.py`: public Python entry point (`get_manager()`).
- `manager.php`: PHP metadata facade.
- `tests/`: executable unit tests.

No accreditation, credential issuance, learner enrollment, payment processing, sensitive student-record storage, job/admission guarantees or training execution is provided. Operators must independently verify legal and safeguarding requirements.
