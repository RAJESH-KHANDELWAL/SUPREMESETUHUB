CATEGORIES=(
    {"id": "scientific_research", "name": "Scientific Research", "subcategories": ["basic_research","applied_research","interdisciplinary_research","field_research"]},
    {"id": "research_institutions", "name": "Research Institutions", "subcategories": ["research_centres","laboratories","universities_research","think_tanks"]},
    {"id": "biotechnology_research", "name": "Biotechnology Research", "subcategories": ["molecular_biology","genomics","bioprocessing","bioinformatics"]},
    {"id": "physical_sciences", "name": "Physical Sciences", "subcategories": ["physics","chemistry","materials_science","astronomy"]},
    {"id": "life_sciences", "name": "Life Sciences", "subcategories": ["biology","ecology","microbiology","neuroscience"]},
    {"id": "engineering_research", "name": "Engineering Research", "subcategories": ["robotics","advanced_materials","electronics_research","systems_engineering"]},
    {"id": "clinical_research", "name": "Clinical & Health Research", "subcategories": ["clinical_trials","public_health_research","medical_devices_research","translational_research"]},
    {"id": "data_research", "name": "Data & Computational Research", "subcategories": ["ai_research","data_science","computational_modelling","high_performance_computing"]},
    {"id": "innovation_incubation", "name": "Innovation & Incubation", "subcategories": ["technology_incubators","research_park","startup_acceleration","prototype_development"]},
    {"id": "intellectual_property", "name": "Intellectual Property & Technology Transfer", "subcategories": ["patents","licensing","technology_transfer","research_commercialization"]},
    {"id": "testing_labs", "name": "Testing & Research Laboratories", "subcategories": ["analytical_testing","calibration","materials_testing","environmental_testing"]},
    {"id": "science_education", "name": "Science Education & Outreach", "subcategories": ["science_museums","public_engagement","stem_outreach","research_training"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
