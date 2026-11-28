"""Comparative civilization research framework; avoids ranking or single-origin narratives."""
CIVILIZATION_STUDY_DIMENSIONS = [
 "settlement and urbanisation","agriculture and food systems","water and landscape management",
 "technology and craft production","trade and exchange networks","writing and record keeping",
 "political institutions and law","religious and philosophical systems","art and architecture",
 "language and literature","migration and demographic change","environmental transformation",
 "warfare and diplomacy","social hierarchy and everyday life"
]
COMPARATIVE_METHOD = {
 "unit_of_analysis":"A defined society, region, network or historical period; never assume a civilization is culturally uniform.",
 "evidence":["archaeology","inscriptions","manuscripts","coins","environmental data","oral histories","comparative linguistics"],
 "rules":["State chronological range and geography.","Separate archaeological evidence from later literary memory.","Avoid equating ancient populations with modern ethnic or national identities.","Record scholarly disagreement and limits of inference."]
}
def get_civilization_framework():
    return {"dimensions":list(CIVILIZATION_STUDY_DIMENSIONS),"method":dict(COMPARATIVE_METHOD)}
