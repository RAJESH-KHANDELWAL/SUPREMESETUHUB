"""Upanishad catalogue with careful separation of text, tradition and dating."""
from typing import Any

UPANISHADS: dict[str, dict[str, Any]] = {
 "isha":{"name":"Isha (Īśā) Upanishad","sanskrit":"ईशावास्योपनिषद्","associated_veda":"Shukla Yajurveda","themes":["renunciation and responsible action","seeing the world through the divine","knowledge and action"],"textual_status":"A principal/major Upanishad in common scholarly classifications","dating_note":"Relative chronology is debated; avoid assigning a precise year."},
 "kena":{"name":"Kena Upanishad","sanskrit":"केनोपनिषद्","associated_veda":"Samaveda","themes":["source of cognition","limits of speech and mind","Brahman and the gods"],"textual_status":"Principal Upanishad"},
 "katha":{"name":"Katha Upanishad","sanskrit":"कठोपनिषद्","associated_veda":"Krishna Yajurveda","themes":["Nachiketa and Yama","death and immortality","self and discipline","chariot analogy"],"textual_status":"Principal Upanishad"},
 "prashna":{"name":"Prashna Upanishad","sanskrit":"प्रश्नोपनिषद्","associated_veda":"Atharvaveda","themes":["six questions","prana","creation","Om meditation"],"textual_status":"Principal Upanishad"},
 "mundaka":{"name":"Mundaka Upanishad","sanskrit":"मुण्डकोपनिषद्","associated_veda":"Atharvaveda","themes":["higher and lower knowledge","two birds image","Brahman","the bow metaphor"],"textual_status":"Principal Upanishad"},
 "mandukya":{"name":"Mandukya Upanishad","sanskrit":"माण्डूक्योपनिषद्","associated_veda":"Atharvaveda","themes":["Om","four states of consciousness","turīya"],"textual_status":"Principal Upanishad; very concise"},
 "aitareya":{"name":"Aitareya Upanishad","sanskrit":"ऐतरेयोपनिषद्","associated_veda":"Rigveda","themes":["cosmogony","self","consciousness"],"textual_status":"Principal Upanishad"},
 "taittiriya":{"name":"Taittiriya Upanishad","sanskrit":"तैत्तिरीयोपनिषद्","associated_veda":"Krishna Yajurveda","themes":["five sheaths teaching","Brahman inquiry","student-teacher instruction"],"textual_status":"Principal Upanishad"},
 "chandogya":{"name":"Chandogya Upanishad","sanskrit":"छान्दोग्योपनिषद्","associated_veda":"Samaveda","themes":["Om and chant","Uddalaka and Shvetaketu","tat tvam asi","meditation"],"textual_status":"Principal Upanishad"},
 "brihadaranyaka":{"name":"Brihadaranyaka Upanishad","sanskrit":"बृहदारण्यकोपनिषद्","associated_veda":"Shukla Yajurveda","themes":["Yajnavalkya dialogues","neti neti","self and reality","Maitreyi dialogue"],"textual_status":"Principal Upanishad"},
 "maha":{"name":"Maha Upanishad","sanskrit":"महोपनिषद्","associated_veda":"Samaveda in commonly cited classifications","themes":["renunciation","knowledge","Vasudhaiva Kutumbakam passage"],"textual_status":"Later Upanishad in many scholarly classifications","dating_note":"Do not assign a precise composition date or author without specialist evidence."}
}

def get_upanishad(upanishad_id: str) -> dict[str, Any]:
    key=upanishad_id.strip().lower()
    if key not in UPANISHADS:
        raise KeyError(f"UPANISHAD_NOT_FOUND:{key}")
    return {"id":key, **UPANISHADS[key]}

def search_upanishads(term: str) -> list[dict[str, Any]]:
    q=term.strip().casefold()
    if not q: return []
    return [{"id":key, **item} for key,item in UPANISHADS.items()
            if q in " ".join([item["name"],item["sanskrit"],item["associated_veda"],*item["themes"]]).casefold()]
