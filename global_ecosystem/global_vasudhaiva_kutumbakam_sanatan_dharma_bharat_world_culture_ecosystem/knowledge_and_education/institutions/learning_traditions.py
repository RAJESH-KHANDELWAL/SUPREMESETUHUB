"""Knowledge transmission institutions across historical and living traditions."""
LEARNING_TRADITIONS = {
 "gurukula":{"description":"Teacher-centred learning arrangements documented in multiple historical and contemporary forms.","research":["textual ideals","actual institutional records","student access","curriculum","patronage","regional variation"],"caution":"Do not romanticise one model as universal or unchanged."},
 "pathashala_tola":{"description":"Sanskrit and other traditional schools with regionally distinct curricula and histories.","research":["institutional archives","subjects taught","teacher lineages","language of instruction","colonial-era records"]},
 "monastic_learning":{"description":"Buddhist, Jain, Hindu and other monastic learning institutions.","research":["monastery records","curriculum","manuscript collections","debate traditions","patronage and networks"]},
 "madrasa_maktab":{"description":"Islamic educational institutions with diverse historical curricula and regional forms.","research":["foundational texts","language instruction","law and theology","community institutions","modern reforms"]},
 "modern_university":{"description":"Modern universities, colleges, research institutes and professional education systems.","research":["founding documents","curriculum","access and equity","research output","language policy"]}
}
def list_learning_traditions():
    return [{"id":key, **value} for key,value in LEARNING_TRADITIONS.items()]
