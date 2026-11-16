"""Healthcare, wellness and fitness category taxonomy."""
from __future__ import annotations

HEALTHCARE_WELLNESS_FITNESS_CATEGORIES = [
    {"id":"gym_and_fitness_centres","name":"Gym & Fitness Centres","subcategories":["gyms","fitness_studios","strength_training","group_fitness"]},
    {"id":"yoga_and_meditation","name":"Yoga & Meditation","subcategories":["yoga_studios","meditation_centres","mindfulness_classes","breathwork"]},
    {"id":"nutrition_and_diet","name":"Nutrition & Diet","subcategories":["registered_dietitians","nutrition_coaching","meal_planning","sports_nutrition"]},
    {"id":"weight_management","name":"Weight Management","subcategories":["healthy_weight_programmes","medical_weight_management_referrals","behaviour_change_coaching","nutrition_support"]},
    {"id":"personal_training_and_coaching","name":"Personal Training & Coaching","subcategories":["personal_trainers","online_fitness_coaching","strength_and_conditioning","fitness_assessments"]},
    {"id":"sports_fitness_and_recovery","name":"Sports Fitness & Recovery","subcategories":["athletic_training","mobility_training","recovery_services","injury_prevention_education"]},
    {"id":"beauty_and_personal_care_wellness","name":"Beauty & Personal Care Wellness","subcategories":["skin_care_services","body_care","salon_wellness","personal_grooming"]},
    {"id":"spa_and_massage_services","name":"Spa & Massage Services","subcategories":["licensed_spa_services","therapeutic_massage","relaxation_services","body_treatments"]},
    {"id":"mental_wellness_and_stress_management","name":"Mental Wellness & Stress Management","subcategories":["stress_management","mindfulness_support","wellbeing_coaching","licensed_mental_health_referrals"]},
    {"id":"wellness_products_and_equipment","name":"Wellness Products & Equipment","subcategories":["fitness_equipment","wellness_accessories","personal_care_products","recovery_equipment"]},
    {"id":"adult_sexual_wellness_education","name":"Adult Sexual Wellness Education","subcategories":["adult_sexual_wellness_education","consent_and_communication","sexual_wellbeing_resources","qualified_clinical_referrals"],"canonical_ecosystem":"global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem","canonical_category_id":"adult_sexual_education","relationship":"cross_reference_only"},
    {"id":"couples_intimacy_and_wellness","name":"Couples Intimacy & Wellness","subcategories":["consensual_adult_intimacy_education","couples_communication","relationship_wellbeing","professional_counselling_referrals"],"canonical_ecosystem":"global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem","canonical_category_id":"couple_intimacy_romance","relationship":"cross_reference_only"},
    {"id":"adult_relationship_wellness","name":"Adult Relationship Wellness","subcategories":["dating_and_relationship_education","healthy_relationship_skills","boundaries_and_consent","relationship_coaching"],"canonical_ecosystem":"global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem","canonical_category_id":"adult_relationships_compatibility","relationship":"cross_reference_only"},
    {"id":"family_wellness_and_counselling","name":"Family Wellness & Counselling","subcategories":["parenting_support","family_communication","non_sexual_family_counselling","caregiver_wellbeing"]},
    {"id":"friends_and_social_wellness","name":"Friends & Social Wellness","subcategories":["friendship_skills","community_wellbeing","social_connection_groups","peer_support"]},
    {"id":"body_wellness_and_lifestyle","name":"Body Wellness & Lifestyle","subcategories":["healthy_lifestyle_education","body_mobility","sleep_hygiene_education","daily_wellbeing_habits"]},
    {"id":"donor_health_and_wellbeing_support","name":"Donor Health & Wellbeing Support","subcategories":["donor_counselling_referrals","donor_wellbeing_information","post_donation_support_resources","regulated_clinic_referrals"]},
    {"id":"wellness_coaches_and_consultants","name":"Wellness Coaches & Consultants","subcategories":["fitness_coaches","wellness_consultants","nutrition_educators","mindfulness_coaches"]},
    {"id":"wellness_jobs_and_careers","name":"Wellness Jobs & Careers","subcategories":["fitness_instructor_jobs","personal_trainer_jobs","spa_and_wellness_jobs","wellness_business_opportunities"]},
    {"id":"corporate_and_community_wellness","name":"Corporate & Community Wellness","subcategories":["employee_wellness_programmes","community_fitness","workplace_wellbeing","public_wellness_events"]}
]

def list_categories() -> list[dict[str, object]]:
    """Return defensive copies of all categories."""
    return [dict(item, subcategories=list(item["subcategories"])) for item in HEALTHCARE_WELLNESS_FITNESS_CATEGORIES]

def get_category(category_id: str) -> dict[str, object] | None:
    """Return one category by stable identifier."""
    for item in HEALTHCARE_WELLNESS_FITNESS_CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None
