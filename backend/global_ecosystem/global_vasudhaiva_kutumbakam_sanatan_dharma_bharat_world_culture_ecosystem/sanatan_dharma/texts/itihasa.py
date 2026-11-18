"""Itihasa epic knowledge records: narrative, textual layers and interpretation."""
from typing import Any

ITIHASA_WORKS: dict[str, dict[str, Any]] = {
 "ramayana":{"name":"Ramayana","sanskrit":"रामायण","traditional_attribution":"Valmiki","genre":"Itihasa / epic","major_figures":["Rama","Sita","Lakshmana","Bharata","Hanuman","Ravana"],"major_themes":["dharma and difficult duty","kingship and responsibility","family and loyalty","exile","devotion","justice and ethical conflict"],"textual_history":"The Sanskrit Valmiki Ramayana has a layered textual history; regional Ramayana traditions in many languages developed with distinct emphases.","study_tracks":["Sanskrit text and recensions","critical edition and textual history","regional retellings","performance traditions","ethical and philosophical interpretation"],"caution":"Distinguish the Sanskrit text, later regional retellings, devotional traditions and modern adaptations."},
 "mahabharata":{"name":"Mahabharata","sanskrit":"महाभारत","traditional_attribution":"Vyasa","genre":"Itihasa / epic","major_figures":["Krishna","Arjuna","Yudhishthira","Draupadi","Bhishma","Karna","Duryodhana"],"major_themes":["dharma under conflict","kinship and power","war and consequences","statecraft","ethics","liberation","narrative of the Bhagavad Gita"],"textual_history":"A vast layered epic with a long period of composition and transmission; its text contains multiple books and embedded teachings.","study_tracks":["parvan-by-parvan reading","Bhagavad Gita within Bhishma Parva","Shanti and Anushasana Parvas","critical edition","regional and performance traditions"],"caution":"Do not present a single simplified moral as the only interpretation of complex episodes."}
}

def get_itihasa(work_id: str) -> dict[str, Any]:
    key=work_id.strip().lower()
    if key not in ITIHASA_WORKS: raise KeyError(f"ITIHASA_NOT_FOUND:{key}")
    return {"id":key, **ITIHASA_WORKS[key]}

def list_itihasa() -> tuple[dict[str, Any], ...]:
    return tuple({"id":key, **item} for key,item in ITIHASA_WORKS.items())
