"""Taxonomy catalog for Personal, Lifestyle & Wellness Services."""
CATEGORIES=(
    {"id": "personal_care", "name": "Personal Care Services", "subcategories": ["salons","barber_services","skincare_services","nail_care"]},
    {"id": "fitness_training", "name": "Fitness & Training", "subcategories": ["personal_training","gyms","group_fitness","strength_conditioning"]},
    {"id": "yoga_meditation", "name": "Yoga & Meditation", "subcategories": ["yoga_studios","meditation","breathwork","mindfulness"]},
    {"id": "nutrition_diet", "name": "Nutrition & Diet Services", "subcategories": ["nutrition_coaching","diet_planning","sports_nutrition","healthy_eating"]},
    {"id": "spa_massage", "name": "Spa & Massage Services", "subcategories": ["day_spas","massage_therapy","wellness_retreats","relaxation_services"]},
    {"id": "mental_wellbeing", "name": "Mental Wellbeing Services", "subcategories": ["stress_management","wellbeing_coaching","mindfulness_programs","peer_support"]},
    {"id": "home_personal_services", "name": "Home & Personal Assistance", "subcategories": ["home_cleaning","laundry","personal_assistance","organizing_services"]},
    {"id": "pet_care", "name": "Pet Care Services", "subcategories": ["pet_grooming","pet_sitting","pet_training","boarding"]},
    {"id": "events_celebrations", "name": "Events & Celebrations", "subcategories": ["event_planning","wedding_services","photography","decoration"]},
    {"id": "hobbies_recreation", "name": "Hobbies & Recreation", "subcategories": ["arts_crafts","music_lessons","dance_classes","outdoor_recreation"]},
    {"id": "senior_lifestyle", "name": "Senior Lifestyle Support", "subcategories": ["companionship","nonmedical_support","active_aging","daily_living_assistance"]},
    {"id": "lifestyle_coaching", "name": "Lifestyle Coaching", "subcategories": ["habit_coaching","time_management","personal_development","life_skills"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
