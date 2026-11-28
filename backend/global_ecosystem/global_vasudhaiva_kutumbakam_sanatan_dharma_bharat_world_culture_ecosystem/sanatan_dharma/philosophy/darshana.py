"""Six classical astika darshana traditions: orientation and comparison."""
from typing import Any

DARSHANAS: dict[str, dict[str, Any]] = {
 "nyaya":{"name":"Nyaya","sanskrit":"न्याय","central_concern":"Logic, epistemology and valid means of knowledge","key_terms":["pramana","anumana","tarka","hetvabhasa"],"traditional_association":"Akshapada Gautama and the Nyaya Sutra","caution":"The tradition develops across many commentators and historical periods."},
 "vaisheshika":{"name":"Vaisheshika","sanskrit":"वैशेषिक","central_concern":"Categories of reality, substances, qualities, motion and atomism","key_terms":["padartha","dravya","guna","karma","samanya","vishesha","samavaya"],"traditional_association":"Kanada and the Vaisheshika Sutra"},
 "samkhya":{"name":"Samkhya","sanskrit":"सांख्य","central_concern":"Analysis of consciousness and material nature","key_terms":["purusha","prakriti","gunas","tattvas","kaivalya"],"traditional_association":"Kapila in traditional attribution; textual history is complex"},
 "yoga":{"name":"Yoga","sanskrit":"योग","central_concern":"Discipline of mind and liberation; classical system associated with Patanjali's Yoga Sutra","key_terms":["chitta-vritti-nirodha","ashtanga","samadhi","klesha","kaivalya"],"caution":"Classical Yoga, broader Indian yoga traditions and modern postural yoga are related but not interchangeable."},
 "mimamsa":{"name":"Purva Mimamsa","sanskrit":"पूर्वमीमांसा","central_concern":"Vedic injunction, ritual interpretation, dharma and language","key_terms":["dharma","vidhi","apurva","shabda","hermeneutics"],"traditional_association":"Jaimini and the Mimamsa Sutra"},
 "vedanta":{"name":"Vedanta / Uttara Mimamsa","sanskrit":"वेदान्त","central_concern":"Brahman, self, world, knowledge and liberation","major_streams":["Advaita","Vishishtadvaita","Dvaita","Bhedabheda","Achintya Bhedabheda and other traditions"],"key_terms":["Brahman","Atman","moksha","maya","bhakti","jnana"],"caution":"Do not collapse distinct Vedanta schools into a single doctrine."}
}

def get_darshana(name: str) -> dict[str, Any]:
    key=name.strip().lower().replace(" ","_")
    if key not in DARSHANAS: raise KeyError(f"DARSHANA_NOT_FOUND:{key}")
    return {"id":key, **DARSHANAS[key]}

def compare_darshanas() -> list[dict[str, Any]]:
    return [{"id":key, **value} for key,value in DARSHANAS.items()]
