"""Purana literature index and responsible study metadata."""
from typing import Any

PURANA_CATEGORIES = {
 "maha_puranas": {
  "description":"The commonly enumerated eighteen Mahapuranas; lists and classifications may vary by tradition.",
  "works":[
   "Brahma Purana","Padma Purana","Vishnu Purana","Shiva Purana","Bhagavata Purana","Narada Purana",
   "Markandeya Purana","Agni Purana","Bhavishya Purana","Brahmavaivarta Purana","Linga Purana",
   "Varaha Purana","Skanda Purana","Vamana Purana","Kurma Purana","Matsya Purana",
   "Garuda Purana","Brahmanda Purana"
  ]
 },
 "study_dimensions":["cosmology","genealogies","manvantara and yuga frameworks","pilgrimage geography","vrata and ritual","dharma teaching","devotional theology","regional sacred geography","narrative and performance"],
 "textual_caution":"Puranic texts are layered and historically fluid. Recensions, interpolations, regional versions and sectarian traditions must be documented rather than flattened."
}

def list_purana_categories() -> dict[str, Any]:
    return PURANA_CATEGORIES.copy()
