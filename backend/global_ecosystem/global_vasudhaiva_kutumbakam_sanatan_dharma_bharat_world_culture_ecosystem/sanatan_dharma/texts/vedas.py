"""Structured guide to the four Vedas and their internal textual layers.

This is a curated orientation catalogue, not a critical edition or a claim that
all recensions, shakhas and manuscript variants are represented.
"""
from typing import Any

VEDAS: dict[str, dict[str, Any]] = {
 "rigveda": {
  "name":"Rigveda", "sanskrit":"ऋग्वेद", "veda_order":"one of the four Vedas",
  "primary_character":"Hymns (sukta) addressed to deities and powers of the Vedic world",
  "traditional_structure":["Samhita","Brahmana","Aranyaka","Upanishad (where associated)"],
  "notable_topics":["cosmology","ritual praise","nature imagery","speech","order (ṛta)","poetic composition"],
  "transmission":"Oral recitation through specialised Vedic recitation traditions; recension-specific transmission matters",
  "caution":"Do not treat one modern translation as a substitute for the Sanskrit text, padapatha, accent and recension."
 },
 "samaveda": {
  "name":"Samaveda", "sanskrit":"सामवेद",
  "primary_character":"Liturgical chants and melodies, with many verses adapted from Rigvedic material",
  "notable_topics":["saman chanting","ritual music","melodic arrangement","recitation"],
  "caution":"Its importance is not measured by counting unique verses alone; musical and ritual arrangement is central."
 },
 "yajurveda": {
  "name":"Yajurveda", "sanskrit":"यजुर्वेद",
  "major_streams":["Shukla (White) Yajurveda","Krishna (Black) Yajurveda"],
  "primary_character":"Ritual formulae and prose/mantra material associated with sacrificial procedures",
  "notable_topics":["yajna","ritual sequence","mantra","Brahmana interpretation"],
  "caution":"Keep the distinct recensions and their textual arrangements separate."
 },
 "atharvaveda": {
  "name":"Atharvaveda", "sanskrit":"अथर्ववेद",
  "primary_character":"Hymns, prayers, domestic and royal concerns, healing-related and protective formulae, and philosophical material",
  "notable_topics":["household life","healing traditions","royal rites","social life","cosmology"],
  "caution":"Avoid reducing the text to magic or medicine; interpret individual hymns in their historical and ritual setting."
 }
}

VEDIC_TEXT_LAYERS = {
 "samhita":{"function":"Mantra and hymn collections; the precise contents vary by Veda and recension."},
 "brahmana":{"function":"Prose expositions of ritual, sacrificial symbolism and related interpretation."},
 "aranyaka":{"function":"Texts associated with forest settings, contemplation and transitions between ritual and speculative inquiry."},
 "upanishad":{"function":"Philosophical and contemplative teachings; individual Upanishads have distinct dates, settings and textual histories."}
}

def get_veda(veda_id: str) -> dict[str, Any]:
    key=veda_id.strip().lower()
    if key not in VEDAS:
        raise KeyError(f"VEDA_NOT_FOUND:{key}")
    return dict(VEDAS[key])

def list_vedas() -> tuple[dict[str, Any], ...]:
    return tuple({"id":key, **value} for key,value in VEDAS.items())
