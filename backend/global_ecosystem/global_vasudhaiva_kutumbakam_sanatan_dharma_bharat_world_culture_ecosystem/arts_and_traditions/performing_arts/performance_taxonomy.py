"""Performing arts taxonomy for cross-cultural knowledge records."""
PERFORMANCE_FIELDS = (
 "form_id","local_form_name","community","region","language","genre",
 "performance_context","repertoire","music_and_instruments","movement_or_gesture",
 "costume_and_material_culture","transmission_lineage","performer_consent",
 "recording_rights","source_references"
)
PERFORMANCE_CONTEXTS = ["ritual","devotional","courtly","community_festival","seasonal","theatre_stage","street_performance","contemporary_fusion"]
DOCUMENTATION_RULES = [
 "Ask performers how they name and contextualise the form.",
 "Do not record restricted ritual performance without permission.",
 "Credit performers, teachers, composers, instrument makers and community custodians.",
 "Record the date and context of the performance; do not treat one performance as the definitive form."
]
def get_performance_taxonomy():
    return {"fields":list(PERFORMANCE_FIELDS),"contexts":list(PERFORMANCE_CONTEXTS),"rules":list(DOCUMENTATION_RULES)}
