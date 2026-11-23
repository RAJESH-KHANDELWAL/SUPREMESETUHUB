"""Education-related commercial capabilities mapped to canonical Global CORE IDs."""
BUSINESS_DOMAINS=(
{"domain_id":"school_tutoring_coaching_services","name":"School Tutoring and Coaching Services","core_domain_id":"school_education","description":"Tutoring, subject coaching and academic support."},
{"domain_id":"higher_education_admissions_guidance","name":"Higher Education and Admissions Guidance","core_domain_id":"higher_education","description":"Admissions information and academic pathway guidance."},
{"domain_id":"vocational_skill_training_businesses","name":"Vocational and Skill Training Businesses","core_domain_id":"vocational_technical_education","description":"Trade training, practical workshops and job skills."},
{"domain_id":"professional_corporate_training","name":"Professional and Corporate Training","core_domain_id":"professional_continuing_education","description":"Workforce upskilling, leadership and corporate learning."},
{"domain_id":"online_courses_learning_platforms","name":"Online Courses and Learning Platforms","core_domain_id":"digital_online_distance_learning","description":"Course production, LMS operations and virtual classrooms."},
{"domain_id":"teacher_training_faculty_development","name":"Teacher Training and Faculty Development","core_domain_id":"teacher_educator_development","description":"Pedagogy workshops and educator development."},
{"domain_id":"career_coaching_employability_services","name":"Career Coaching and Employability Services","core_domain_id":"career_guidance_employability","description":"Career coaching, job readiness and employability workshops."},
{"domain_id":"assessment_exam_preparation","name":"Assessment and Exam Preparation Services","core_domain_id":"assessment_credentialing","description":"Exam preparation, mock assessments and assessment content."},
{"domain_id":"language_literacy_training","name":"Language and Literacy Training","core_domain_id":"language_literacy_communication","description":"Language instruction, literacy and communication workshops."},
{"domain_id":"inclusive_learning_accessibility_services","name":"Inclusive Learning and Accessibility Services","core_domain_id":"inclusive_special_needs_learning","description":"Accessible learning design and accommodation coordination."},
{"domain_id":"education_consulting_advisory","name":"Education Consulting and Advisory","core_domain_id":"learning_policy_quality_governance","description":"Institutional strategy, education operations and quality advisory."},
{"domain_id":"research_content_curriculum_development","name":"Research, Content and Curriculum Development","core_domain_id":"research_academic_knowledge","description":"Curriculum design, instructional content and academic research support."},
{"domain_id":"student_parent_institution_support","name":"Student, Parent and Institution Support","core_domain_id":"school_education","description":"Student success support, parent engagement and institutional coordination."},
{"domain_id":"education_franchises_learning_centres","name":"Education Franchises and Learning Centres","core_domain_id":"professional_continuing_education","description":"Learning-centre operations, franchise models and business development."},
{"domain_id":"education_marketplaces_distribution","name":"Education Marketplaces and Distribution","core_domain_id":"digital_online_distance_learning","description":"Course marketplaces and educational-resource distribution."},)
def list_business_domains(): return [dict(x,capabilities=["SERVICE","WORK","BUSINESS"]) for x in BUSINESS_DOMAINS]
def get_business_domain(domain_id):
 key=domain_id.strip().casefold()
 return next((dict(x,capabilities=["SERVICE","WORK","BUSINESS"]) for x in BUSINESS_DOMAINS if x["domain_id"].casefold()==key),None)
def validate_business_domains():
 ids=[x["domain_id"] for x in BUSINESS_DOMAINS]
 return {"valid":len(ids)==len(set(ids)) and all(x["core_domain_id"] for x in BUSINESS_DOMAINS),"count":len(ids)}
