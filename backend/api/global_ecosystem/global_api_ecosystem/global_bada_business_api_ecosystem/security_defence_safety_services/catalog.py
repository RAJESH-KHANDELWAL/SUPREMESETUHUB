CATEGORIES=(
    {"id": "physical_security", "name": "Physical Security", "subcategories": ["guarding_services","access_control","security_patrols","event_security"]},
    {"id": "cybersecurity", "name": "Cybersecurity Services", "subcategories": ["security_assessments","incident_response","security_monitoring","security_training"]},
    {"id": "fire_safety", "name": "Fire & Life Safety", "subcategories": ["fire_detection","fire_suppression","fire_audits","fire_equipment"]},
    {"id": "occupational_safety", "name": "Occupational Health & Safety", "subcategories": ["workplace_safety","industrial_hygiene","safety_training","risk_assessments"]},
    {"id": "defence_manufacturing", "name": "Defence Manufacturing", "subcategories": ["defence_equipment","aerospace_components","protective_equipment","systems_integration"]},
    {"id": "defence_services", "name": "Defence Support Services", "subcategories": ["maintenance_support","logistics_support","technical_services","simulation_training"]},
    {"id": "surveillance_monitoring", "name": "Monitoring & Detection Systems", "subcategories": ["cctv_systems","alarm_systems","perimeter_detection","monitoring_centres"]},
    {"id": "investigation_risk", "name": "Investigation & Risk Advisory", "subcategories": ["corporate_investigations","fraud_risk","due_diligence","security_consulting"]},
    {"id": "emergency_preparedness", "name": "Emergency Preparedness", "subcategories": ["business_continuity","disaster_planning","crisis_management","resilience_services"]},
    {"id": "public_safety_equipment", "name": "Public Safety Equipment", "subcategories": ["protective_clothing","rescue_equipment","safety_signage","emergency_communications"]},
    {"id": "security_compliance", "name": "Security Compliance & Audits", "subcategories": ["security_audits","standards_assessment","compliance_advisory","vendor_risk"]},
    {"id": "training_certification", "name": "Safety & Security Training", "subcategories": ["first_aid_training","security_personnel_training","industrial_safety_courses","emergency_drills"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
