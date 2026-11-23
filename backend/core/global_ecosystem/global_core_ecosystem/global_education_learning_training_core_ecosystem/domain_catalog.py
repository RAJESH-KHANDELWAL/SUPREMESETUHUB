"""Canonical vendor-neutral education taxonomy."""
DOMAINS=(
{"domain_id":"early_childhood_education","name":"Early Childhood Education","description":"Early learning and foundational development."},
{"domain_id":"school_education","name":"School Education","description":"Primary through higher-secondary education."},
{"domain_id":"higher_education","name":"Higher Education","description":"Universities, colleges, academic disciplines and research education."},
{"domain_id":"vocational_technical_education","name":"Vocational and Technical Education","description":"Trades, technical education and applied learning."},
{"domain_id":"professional_continuing_education","name":"Professional and Continuing Education","description":"Continuing professional development and lifelong learning."},
{"domain_id":"digital_online_distance_learning","name":"Digital, Online and Distance Learning","description":"E-learning, virtual classrooms and distance education."},
{"domain_id":"skills_competency_development","name":"Skills and Competency Development","description":"Foundational, transferable and occupational competencies."},
{"domain_id":"teacher_educator_development","name":"Teacher and Educator Development","description":"Teacher education, pedagogy and faculty development."},
{"domain_id":"research_academic_knowledge","name":"Research and Academic Knowledge","description":"Research methods, scholarly communication and knowledge creation."},
{"domain_id":"assessment_credentialing","name":"Assessment and Credentialing","description":"Assessment, examinations and qualification frameworks."},
{"domain_id":"inclusive_special_needs_learning","name":"Inclusive and Special Needs Learning","description":"Accessible education and inclusive learning environments."},
{"domain_id":"career_guidance_employability","name":"Career Guidance and Employability Learning","description":"Career exploration, work readiness and learning-to-work transitions."},
{"domain_id":"language_literacy_communication","name":"Language, Literacy and Communication","description":"Language learning, literacy and multilingual education."},
{"domain_id":"ethics_civic_global_citizenship","name":"Ethics, Civic and Global Citizenship Education","description":"Ethics, civic understanding and global awareness."},
{"domain_id":"learning_policy_quality_governance","name":"Learning Policy, Quality and Governance","description":"Education policy, institutional quality and governance."},)
def list_domains(): return [dict(x) for x in DOMAINS]
def get_domain(domain_id):
 key=domain_id.strip().casefold()
 return next((dict(x) for x in DOMAINS if x["domain_id"].casefold()==key),None)
