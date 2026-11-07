"""Unified personal, family, relationship and adult-wellness taxonomy.

Adult categories are separately classified and excluded from default discovery.
"""
CATEGORIES=(
    {"id":"personal_care","name":"Personal Care Services","subcategories":["salons","barber_services","skincare_services","nail_care"],"access_class":"general"},
    {"id":"fitness_training","name":"Fitness & Training","subcategories":["personal_training","gyms","group_fitness","strength_conditioning"],"access_class":"general"},
    {"id":"yoga_meditation","name":"Yoga & Meditation","subcategories":["yoga_studios","meditation","breathwork","mindfulness"],"access_class":"general"},
    {"id":"nutrition_diet","name":"Nutrition & Diet Services","subcategories":["nutrition_coaching","diet_planning","sports_nutrition","healthy_eating"],"access_class":"general"},
    {"id":"spa_massage","name":"Spa & Massage Services","subcategories":["day_spas","massage_therapy","wellness_retreats","relaxation_services"],"access_class":"general"},
    {"id":"mental_wellbeing","name":"Mental Wellbeing Services","subcategories":["stress_management","wellbeing_coaching","mindfulness_programs","peer_support"],"access_class":"general"},
    {"id":"home_personal_services","name":"Home & Personal Assistance","subcategories":["home_cleaning","laundry","personal_assistance","organizing_services"],"access_class":"general"},
    {"id":"pet_care","name":"Pet Care Services","subcategories":["pet_grooming","pet_sitting","pet_training","boarding"],"access_class":"general"},
    {"id":"events_celebrations","name":"Events & Celebrations","subcategories":["event_planning","wedding_services","photography","decoration"],"access_class":"general"},
    {"id":"hobbies_recreation","name":"Hobbies & Recreation","subcategories":["arts_crafts","music_lessons","dance_classes","outdoor_recreation"],"access_class":"general"},
    {"id":"senior_lifestyle","name":"Senior Lifestyle Support","subcategories":["companionship","nonmedical_support","active_aging","daily_living_assistance"],"access_class":"general"},
    {"id":"lifestyle_coaching","name":"Lifestyle Coaching","subcategories":["habit_coaching","time_management","personal_development","life_skills"],"access_class":"general"},
    {"id":"personal_health_wellness","name":"Personal Health & Wellness Services","subcategories":["healthy_lifestyle_support","preventive_wellness_education","nonclinical_health_coaching","wellbeing_routines"],"access_class":"general"},
    {"id":"relatives_extended_family","name":"Relatives & Extended-Family Relationships","subcategories":["extended_family_communication","in_law_relationships","family_boundaries_education","intergenerational_connections"],"access_class":"general"},
    {"id":"friends_social_relationships","name":"Friends & Social Relationships","subcategories":["friendship_building","social_connection","peer_relationships","social_skills_education"],"access_class":"general"},
    {"id":"family_relationships","name":"Family & Household Relationships","subcategories":["family_support","family_communication","intergenerational_relationships","family_life_education"],"access_class":"general"},
    {"id":"marriage_partnership","name":"Marriage & Long-term Partnerships","subcategories":["premarital_education","marriage_enrichment","partnership_communication","separation_support_information"],"access_class":"general"},
    {"id":"couple_relationships","name":"Couple & Relationship Support","subcategories":["couple_communication","relationship_coaching","conflict_resolution","dating_relationship_education"],"access_class":"general"},
    {"id":"parenting_parenthood","name":"Parenting & Parenthood","subcategories":["parenting_education","positive_parenting","co_parenting_support","parent_child_communication"],"access_class":"general"},
    {"id":"relationship_counselling","name":"Relationship Counselling & Mediation","subcategories":["couple_counselling","family_counselling","relationship_mediation","referral_to_licensed_professionals"],"access_class":"general"},
    {"id":"sexual_health_education","name":"Sexual Health & Intimacy Education","subcategories":["consent_education","sexual_health_information","intimacy_communication","reproductive_health_education"],"access_class":"general"},
    {"id":"adult_sexual_wellness_18_plus","name":"Adult Intimacy, Sexual Health & Wellness (18+)","subcategories":["adult_intimacy_education","adult_sexual_wellness_education","adult_health_information","intimacy_wellness_products","adult_relationship_resources","age_gated_wellness_information"],"access_class":"18_plus_restricted"},
    {"id":"adult_porn_media_18_plus","name":"Adult Media, Pornography & Publishing (18+)","subcategories":["lawful_adult_content_production","consensual_adult_performer_services","adult_publishing_and_distribution","age_verification_and_access_controls","consent_and_content_rights_management"],"access_class":"18_plus_restricted"},
)
def list_categories(*,include_adult=False):
    return [dict(x,subcategories=list(x["subcategories"])) for x in CATEGORIES
            if include_adult or x["access_class"]!="18_plus_restricted"]
def get_category(category_id,*,include_adult=False):
    for item in CATEGORIES:
        if item["id"]==category_id:
            if item["access_class"]=="18_plus_restricted" and not include_adult: return None
            return dict(item,subcategories=list(item["subcategories"]))
    return None
