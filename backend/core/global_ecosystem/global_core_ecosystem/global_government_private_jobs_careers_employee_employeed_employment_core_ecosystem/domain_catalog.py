"""Canonical global employment domains and topic taxonomy."""
DOMAINS = {
"GOVERNMENT_PUBLIC_SERVICE": {"name":"Government and Public Service","topics":["central_federal_government","state_provincial_government","district_municipal_local_government","civil_services","public_administration","public_sector_enterprises","defence_uniformed_services","public_health_education","regulators_commissions","government_contractual_roles"]},
"PRIVATE_SECTOR": {"name":"Private Sector Employment","topics":["multinational_companies","large_enterprises","mid_market_companies","msme_sme","startups","family_businesses","cooperatives","nonprofits_social_enterprises"]},
"JOBS_VACANCIES": {"name":"Jobs and Vacancies","topics":["permanent_jobs","temporary_jobs","fixed_term_jobs","contract_roles","seasonal_jobs","project_roles","entry_level","experienced_hiring","executive_roles","internal_mobility"]},
"CAREERS_PROFESSIONS": {"name":"Careers and Professions","topics":["career_paths","occupation_families","professional_roles","technical_roles","skilled_trades","management_leadership","career_transition","returnships"]},
"EMPLOYERS_EMPLOYEES_WORKERS": {"name":"Employers, Employees and Workers","topics":["government_employers","private_employers","public_enterprises","employees","workers","officers","agency_workers","apprentices","interns","trainees","contractors_reference_only"]},
"WORK_ARRANGEMENTS": {"name":"Work Arrangements","topics":["on_site","remote","hybrid","work_from_home","field_work","distributed_teams","shift_work","flexible_schedule","travel_required"]},
"EMPLOYMENT_TYPES": {"name":"Employment Types","topics":["full_time","part_time","permanent","temporary","fixed_term","casual","seasonal","apprenticeship","internship","returnship","job_sharing"]},
"INDUSTRIES_OCCUPATIONS": {"name":"Industries and Occupations","topics":["agriculture","manufacturing","construction","technology_it_ai","finance","healthcare","education","retail","hospitality","transport_logistics","energy","public_administration","professional_services"]},
"RECRUITMENT_LIFECYCLE": {"name":"Recruitment Lifecycle","topics":["workforce_planning","job_requisition","job_description","application","screening","assessment","interview","selection","offer","onboarding"]},
"EMPLOYEE_LIFECYCLE": {"name":"Employee Lifecycle","topics":["joining_onboarding","probation","employment_records","attendance","leave","performance","learning_development","promotion","transfer","retention","separation","alumni"]},
"COMPENSATION_BENEFITS": {"name":"Compensation and Benefits","topics":["salary_bands","wages","pay_frequency","allowances","incentives","benefits","retirement_benefits","statutory_contributions_reference","total_rewards"]},
"WORKPLACE_RELATIONS": {"name":"Workplace Relations and Wellbeing","topics":["employee_relations","grievances","workplace_safety","accessibility","reasonable_accommodation","wellbeing","workplace_respect","whistleblowing_channels"]},
"GEOGRAPHY_MOBILITY": {"name":"Geography and Mobility","topics":["global_regions","countries","india_states_union_territories","districts","cities","towns","villages","postal_areas","work_authorization_reference","cross_border_mobility"]},
"SKILLS_EDUCATION_CREDENTIALS": {"name":"Skills, Education and Credentials","topics":["school_education","higher_education","vocational_training","apprenticeships","professional_qualifications","licenses","certifications","skills_taxonomy","experience_levels","lifelong_learning"]},
"LABOUR_MARKET_INTELLIGENCE": {"name":"Labour Market Intelligence","topics":["vacancy_trends","occupation_demand","skills_gaps","wage_trends","aggregate_workforce_indicators","employment_indicators","regional_supply_demand"]}}

def list_domains():
    return [{"domain_id": k, **v} for k,v in DOMAINS.items()]

def list_topics():
    return [{"domain_id":k,"domain_name":v["name"],"topic":t} for k,v in DOMAINS.items() for t in v["topics"]]
