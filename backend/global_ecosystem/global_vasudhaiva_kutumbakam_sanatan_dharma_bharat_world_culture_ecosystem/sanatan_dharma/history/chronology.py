"""Chronology framework for Sanatan Dharma textual and institutional history.

Periods are deliberately broad. A date must be attached to a particular
textual layer, manuscript, inscription, institution or scholarly argument.
"""
CHRONOLOGY = [
 {"id":"early_vedic","label":"Early Vedic textual horizons","period_note":"Second millennium BCE is often discussed for early Vedic composition; exact dates and layers remain scholarly questions.","evidence_types":["linguistic analysis","textual stratification","comparative Indo-Iranian studies"],"caution":"A broad horizon is not a date for every hymn or recension."},
 {"id":"later_vedic","label":"Later Vedic developments","period_note":"Late second to early first millennium BCE is a broad scholarly frame often used, with variation by text and layer.","evidence_types":["Brahmana and Aranyaka texts","ritual prose","linguistic evidence"]},
 {"id":"early_upanishadic","label":"Early Upanishadic compositions","period_note":"First millennium BCE; relative chronology and individual textual dates are debated.","evidence_types":["textual language","intertextual references","philosophical development"]},
 {"id":"epic_textual_growth","label":"Epic textual formation","period_note":"Long and layered processes across the later first millennium BCE and first millennium CE are discussed by scholarship; no single date captures the epics.","evidence_types":["recensions","manuscripts","critical editions","linguistic and narrative layers"]},
 {"id":"classical_sutra_sastra","label":"Sutra and Shastra traditions","period_note":"Multiple centuries BCE/CE depending on school and work.","evidence_types":["commentaries","citations","manuscript witnesses","inscriptions"]},
 {"id":"medieval_bhakti","label":"Medieval devotional movements","period_note":"Region- and lineage-specific; many movements span several centuries.","evidence_types":["vernacular compositions","temple records","hagiographies","performance traditions"]},
 {"id":"early_modern","label":"Early modern religious and intellectual developments","period_note":"Broadly second millennium CE; highly regionally differentiated.","evidence_types":["court records","manuscripts","pilgrimage records","institutional histories"]},
 {"id":"modern_global","label":"Modern reform, revival and global transmission","period_note":"Nineteenth century onward, with distinct movements and international networks.","evidence_types":["print publications","institutional archives","correspondence","colonial and postcolonial records"]}
]

def get_chronology():
    return [dict(item) for item in CHRONOLOGY]
