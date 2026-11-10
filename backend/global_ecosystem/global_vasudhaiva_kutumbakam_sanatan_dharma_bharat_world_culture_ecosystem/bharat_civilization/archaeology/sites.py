"""Archaeological site research records with evidence-class separation."""
ARCHAEOLOGICAL_SITE_RECORDS = {
 "dholavira":{"name":"Dholavira","location":"Khadir Bet, Kutch, Gujarat, India","civilization_context":"Harappan / Indus Civilization","evidence_topics":["planned urban settlement","water management","fortifications","craft and trade evidence","inscriptions/signboard"],"heritage_note":"UNESCO World Heritage property (inscribed 2021).","caution":"Interpretations of the signboard and social organisation remain subject to specialist debate."},
 "lothal":{"name":"Lothal","location":"Gujarat, India","civilization_context":"Harappan / Indus Civilization","evidence_topics":["settlement layout","craft production","bead making","trade interpretations","waterfront structure debate"],"caution":"The function of the basin commonly called a dockyard has been debated; describe the evidence and competing interpretations."},
 "kalibangan":{"name":"Kalibangan","location":"Hanumangarh district, Rajasthan, India","civilization_context":"Harappan / Indus Civilization","evidence_topics":["early and mature Harappan phases","fire installations","ploughed field evidence","settlement planning"],"caution":"Avoid treating one excavation feature as proof of a uniform religious system."},
 "rakhigarhi":{"name":"Rakhigarhi","location":"Hisar district, Haryana, India","civilization_context":"Harappan / Indus Civilization","evidence_topics":["settlement extent","burials","craft production","bioarchaeology","urban phases"],"caution":"Ancient DNA findings require careful reading of the actual study and cannot support simplistic modern identity claims."},
 "sanchi":{"name":"Sanchi","location":"Madhya Pradesh, India","civilization_context":"Buddhist monastic and monumental complex","evidence_topics":["stupas","inscriptions","patronage","sculptural narratives","monastic history"],"heritage_note":"UNESCO World Heritage property (inscribed 1989)."}
}
def get_site(site_id: str):
    key=site_id.strip().lower()
    if key not in ARCHAEOLOGICAL_SITE_RECORDS: raise KeyError(f"ARCHAEOLOGICAL_SITE_NOT_FOUND:{key}")
    return {"id":key, **ARCHAEOLOGICAL_SITE_RECORDS[key]}
def list_sites():
    return [{"id":key, **value} for key,value in ARCHAEOLOGICAL_SITE_RECORDS.items()]
