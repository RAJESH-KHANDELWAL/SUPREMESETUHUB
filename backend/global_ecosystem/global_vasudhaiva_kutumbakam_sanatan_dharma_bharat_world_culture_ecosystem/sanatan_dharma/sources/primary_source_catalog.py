"""Primary-source discovery catalogue for Sanatan Dharma research.

Entries identify source families and research directions; they are not a claim
that a particular edition or translation is licensed for redistribution.
"""
PRIMARY_SOURCE_FAMILIES = {
 "vedic":{"name":"Vedic Samhitas and associated literature","materials":["Rigveda Samhita","Samaveda Samhita","Yajurveda Samhita recensions","Atharvaveda Samhita","Brahmanas","Aranyakas"],"research_checks":["shakha/recension","samhita or pada text","accent notation","edition","translator","copyright status"]},
 "upanishadic":{"name":"Upanishadic literature","materials":["Principal Upanishads","Maha Upanishad","other later Upanishads"],"research_checks":["associated Veda","recension","chapter and verse numbering","Sanskrit edition","translation provenance","dating scholarship"]},
 "epic":{"name":"Itihasa","materials":["Valmiki Ramayana","Mahabharata","Bhagavad Gita within Mahabharata"],"research_checks":["critical edition or regional recension","parvan/kanda","manuscript evidence","translation edition","commentary lineage"]},
 "puranic":{"name":"Purana literature","materials":["Mahapuranas","Upapuranas","Sthala Puranas"],"research_checks":["recension","regional text","sectarian context","interpolation history","edition and translation"]},
 "sutra_shastra":{"name":"Sutra and Shastra literature","materials":["Dharmasutras","Grihyasutras","Shrautasutras","Darshana sutras","Dharma and philosophical commentaries"],"research_checks":["school","commentator","text layer","historical context","edition"]}
}

def source_family(family_id: str):
    key=family_id.strip().lower()
    if key not in PRIMARY_SOURCE_FAMILIES: raise KeyError(f"SOURCE_FAMILY_NOT_FOUND:{key}")
    return {"id":key, **PRIMARY_SOURCE_FAMILIES[key]}
