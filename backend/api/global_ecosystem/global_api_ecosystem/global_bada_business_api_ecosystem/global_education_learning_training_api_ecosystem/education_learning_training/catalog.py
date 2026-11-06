"""Education, Learning & Training category taxonomy."""
from __future__ import annotations

EDUCATION_CATEGORIES = (
    {"id": "early_childhood_and_school_education", "name": "Early Childhood & School Education", "subcategories": ["preschools_and_kindergartens", "primary_schools", "secondary_schools", "senior_secondary_schools", "international_schools", "alternative_and_montessori_schools"]},
    {"id": "higher_education", "name": "Higher Education", "subcategories": ["universities", "colleges", "degree_programmes", "open_and_distance_universities", "research_institutions", "community_colleges"]},
    {"id": "competitive_exam_preparation", "name": "Competitive & Entrance Exam Preparation", "subcategories": ["engineering_entrance", "medical_entrance", "civil_services", "banking_and_insurance_exams", "staff_selection_exams", "international_admissions_tests"]},
    {"id": "coaching_and_tutoring", "name": "Coaching, Tuition & Academic Tutoring", "subcategories": ["school_subject_tuition", "one_to_one_tutoring", "group_coaching", "home_tutoring", "test_preparation", "academic_counselling"]},
    {"id": "online_learning_and_edtech", "name": "Online Learning & EdTech", "subcategories": ["learning_management_systems", "lms_interoperability_and_learning_records", "learning_content_standards", "online_course_platforms", "virtual_classrooms", "education_apps", "adaptive_learning", "digital_learning_content"]},
    {"id": "professional_and_corporate_training", "name": "Professional & Corporate Training", "subcategories": ["employee_upskilling", "leadership_development", "sales_training", "compliance_training", "corporate_learning", "train_the_trainer"]},
    {"id": "vocational_and_skill_development", "name": "Vocational & Skill Development", "subcategories": ["industrial_skills", "technical_trade_training", "beauty_and_wellness_training", "hospitality_training", "retail_and_customer_service_skills", "apprenticeships"]},
    {"id": "technical_and_it_education", "name": "Technical, IT & Computer Education", "subcategories": ["software_development_training", "data_and_ai_training", "cybersecurity_training", "networking_and_cloud", "computer_fundamentals", "it_certifications"]},
    {"id": "language_and_communication_learning", "name": "Language & Communication Learning", "subcategories": ["english_language_training", "foreign_language_courses", "spoken_english", "business_communication", "ielts_toefl_and_language_tests", "translation_and_interpreting_training"]},
    {"id": "study_abroad_and_admissions", "name": "Study Abroad & Admissions Services", "subcategories": ["international_admissions_guidance", "application_support", "scholarship_guidance", "student_visa_guidance", "credential_evaluation", "education_pathway_advisory"]},
    {"id": "certification_and_assessment", "name": "Certifications, Testing & Assessment", "subcategories": ["professional_certifications", "internationally_recognised_credential_reference", "micro_credentials_and_digital_badges", "credential_issuer_and_verification_metadata", "skill_assessments", "language_proficiency_tests", "online_proctoring", "exam_content_and_delivery", "credential_verification"]},
    {"id": "special_and_inclusive_education", "name": "Special & Inclusive Education", "subcategories": ["inclusive_classrooms", "specialist_learning_support", "assistive_learning_technology", "dyslexia_and_learning_support", "gifted_education", "accessibility_services"]},
    {"id": "early_career_and_lifelong_learning", "name": "Career Learning & Lifelong Education", "subcategories": ["career_re_skilling", "adult_education", "continuing_education", "return_to_work_programmes", "career_transition_learning", "personal_development_courses"]},
    {"id": "education_services_and_infrastructure", "name": "Education Services & Infrastructure", "subcategories": ["school_management_services", "education_consulting", "library_and_learning_resources", "laboratories_and_equipment", "campus_management", "education_transport_and_facilities"]},
    {"id": "research_and_academic_services", "name": "Research & Academic Services", "subcategories": ["research_methods_training", "academic_writing_support", "research_data_services", "scholarly_publishing_services", "institutional_research_support", "academic_conferences"]},

    {"id": "ai_and_data_literacy_education", "name": "AI, Generative AI & Data Literacy Education", "subcategories": ["artificial_intelligence_fundamentals", "generative_ai_and_prompt_literacy", "machine_learning_fundamentals", "data_literacy_and_analytics", "responsible_ai_and_ai_safety_education", "ai_output_evaluation_and_human_review", "privacy_safe_ai_learning_practice", "applied_ai_tools_and_workflows", "ai_for_students_and_teachers"]},
    {"id": "digital_skills_freelancing_and_remote_work", "name": "Digital Skills, Freelancing & Remote Work Training", "subcategories": ["digital_literacy_and_productivity", "freelancing_business_fundamentals", "client_communication_and_proposals", "remote_work_tools_and_workflows", "portfolio_and_personal_brand_building", "work_sample_and_portfolio_evidence", "freelance_scope_and_contract_literacy", "project_and_time_management", "online_work_safety_and_scam_awareness"]},
    {"id": "entrepreneurship_and_business_education", "name": "Entrepreneurship, MSME & Business Education", "subcategories": ["entrepreneurship_fundamentals", "startup_and_business_model_education", "msme_business_management_training", "sales_and_customer_relationship_skills", "business_finance_and_bookkeeping_literacy", "business_planning_and_market_research", "leadership_and_team_management_education"]},
    {"id": "digital_marketing_and_creator_economy_training", "name": "Digital Marketing & Creator Economy Training", "subcategories": ["search_engine_optimisation_training", "social_media_marketing_training", "content_writing_and_copywriting", "video_and_audio_content_production", "performance_marketing_fundamentals", "analytics_and_conversion_optimisation", "creator_business_and_audience_development"]}

)



# Related domains own their respective source records; this package only links stable identifiers.
CROSS_ECOSYSTEM_LINKS = {
    "students_education_skills_business_api_ecosystem": {
        "relationship": "Student profiles, learner pathways and student community records remain in the core student ecosystem.",
        "purpose": "Link education programmes to learner-facing records without copying student data.",
    },
    "jobs_careers_employment": {
        "relationship": "Vacancies, employers and employment outcomes remain in the jobs ecosystem.",
        "purpose": "Connect learning outcomes to relevant occupation and vacancy taxonomies; never imply guaranteed placement.",
    },
    "science_research_innovation": {
        "relationship": "AI research, model development and scientific R&D remain in the science ecosystem.",
        "purpose": "Reference research topics as curriculum inputs; this package owns teaching and learning records.",
    },
    "technology_it_telecommunications": {
        "relationship": "Software, platforms and technology products remain in their technology ecosystems.",
        "purpose": "Reference tools used in courses without duplicating product or vendor catalogs.",
    },
    "classification_standards_business_api_ecosystem": {
        "relationship": "Occupation, skill and qualification standards remain versioned in the classification standards package.",
        "purpose": "Map learning outcomes to sourced skill and occupation codes only when a reviewed crosswalk exists.",
    },
}

def list_education_categories() -> list[dict[str, object]]:
    """Return a defensive copy of the education category catalog."""
    return [dict(item, subcategories=list(item["subcategories"])) for item in EDUCATION_CATEGORIES]

def get_education_category(category_id: str) -> dict[str, object] | None:
    """Return one category by its stable identifier."""
    for item in EDUCATION_CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None
