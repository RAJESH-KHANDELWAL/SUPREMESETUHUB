CATEGORIES=(
    {"id":"scientific_research","name":"Scientific Research & Development","subcategories":["basic_research","applied_research","interdisciplinary_research","field_research","experimental_research","research_methodology"]},
    {"id":"research_institutions","name":"Research Institutions & Laboratories","subcategories":["research_centres","laboratories","universities_research","think_tanks","national_research_institutes","private_research_centres"]},
    {"id":"ai_ml_research","name":"Artificial Intelligence & Machine Learning Research","subcategories":["machine_learning","deep_learning","neural_networks","computer_vision","natural_language_processing","reinforcement_learning","explainable_ai","responsible_ai","ai_safety","edge_ai"]},
    {"id":"generative_ai_research","name":"Generative AI & Foundation Model Research","subcategories":["large_language_models","multimodal_models","generative_image_audio_video","retrieval_augmented_generation","ai_agents","model_evaluation","model_alignment","synthetic_data"]},
    {"id":"biotechnology_research","name":"Biotechnology, Genomics & Bioinformatics","subcategories":["molecular_biology","genomics","gene_editing_research","bioprocessing","bioinformatics","synthetic_biology"]},
    {"id":"physical_sciences","name":"Physical Sciences, Chemistry & Materials","subcategories":["physics","chemistry","materials_science","nanotechnology","astronomy","quantum_science"]},
    {"id":"life_sciences","name":"Life Sciences & Environmental Biology","subcategories":["biology","ecology","microbiology","neuroscience","biodiversity_research","climate_science"]},
    {"id":"engineering_research","name":"Engineering, Robotics & Advanced Technology Research","subcategories":["robotics","advanced_materials","electronics_research","systems_engineering","industrial_research","semiconductor_research"]},
    {"id":"clinical_research","name":"Clinical, Medical & Public Health Research","subcategories":["clinical_trials","public_health_research","medical_devices_research","translational_research","epidemiology","health_data_research"]},
    {"id":"data_research","name":"Data, Computational & High-Performance Research","subcategories":["data_science","computational_modelling","high_performance_computing","scientific_computing","research_data_engineering","simulation"]},
    {"id":"innovation_incubation","name":"Innovation, Incubation & Prototyping","subcategories":["technology_incubators","research_parks","startup_acceleration","prototype_development","proof_of_concept","deep_tech_ventures"]},
    {"id":"intellectual_property","name":"Intellectual Property & Technology Transfer","subcategories":["patents","licensing","technology_transfer","research_commercialization","spin_offs","prior_art_research"]},
    {"id":"testing_labs","name":"Testing, Certification & Research Laboratories","subcategories":["analytical_testing","calibration","materials_testing","environmental_testing","instrument_validation","laboratory_quality_systems"]},
    {"id":"research_funding_grants","name":"Research Funding, Grants & Fellowships","subcategories":["government_research_grants","industry_sponsored_research","research_fellowships","innovation_grants","research_funding_calls","grant_management"]},
    {"id":"scientific_equipment","name":"Scientific Equipment, Instruments & Research Infrastructure","subcategories":["laboratory_instruments","scientific_imaging","research_compute_infrastructure","equipment_facilities","instrument_maintenance","research_infrastructure"]},
    {"id":"open_science_data","name":"Open Science, Publications & Research Data","subcategories":["open_access_research","scientific_publications","research_repositories","research_data_management","reproducibility","meta_research"]},
    {"id":"science_education","name":"Science Education, Training & Outreach","subcategories":["science_museums","public_engagement","stem_outreach","research_training","doctoral_training","scientific_communication"]},
)

def list_categories(): return [dict(x) for x in CATEGORIES]

def get_category(category_id):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item)
    return None

def validate_catalog():
    ids=[item["id"] for item in CATEGORIES]
    return {"valid":len(ids)==len(set(ids)),"category_count":len(CATEGORIES),"duplicate_ids":sorted({x for x in ids if ids.count(x)>1})}
