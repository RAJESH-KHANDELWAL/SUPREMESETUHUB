"""Evidence-aware broad chronology of South Asian history."""
SOUTH_ASIAN_PERIODS = [
 {"id":"palaeolithic","label":"Palaeolithic","period":"Deep prehistory; dates vary by region and archaeological sequence","evidence":["stone tools","faunal remains","sediments","dating methods"]},
 {"id":"mesolithic","label":"Mesolithic","period":"Post-Pleistocene regional sequences; not a single uniform start date","evidence":["microliths","settlement traces","rock art","burials"]},
 {"id":"neolithic_chalcolithic","label":"Neolithic and Chalcolithic","period":"Regionally varied farming, herding and copper-use horizons","evidence":["domesticated remains","ceramics","settlements","metallurgy"]},
 {"id":"harappan","label":"Harappan / Indus Civilization","period":"Broadly c. 2600–1900 BCE for the Mature Harappan phase; earlier and later phases extend beyond this","evidence":["urban settlements","seals","weights","crafts","burials","script corpus"]},
 {"id":"early_historic","label":"Early Historic South Asia","period":"First millennium BCE onward, with regional variation","evidence":["inscriptions","coins","texts","urban archaeology","trade routes"]},
 {"id":"early_medieval","label":"Early Medieval","period":"Approximate and debated regional periodisation, often c. 600–1200 CE in some historiographies","evidence":["temple inscriptions","land grants","regional polities","literature","architecture"]},
 {"id":"late_medieval_early_modern","label":"Late Medieval and Early Modern","period":"Regionally distinct transitions across c. 1200–1800 CE","evidence":["court chronicles","administrative records","architecture","trade archives","vernacular literature"]},
 {"id":"colonial_modern","label":"Colonial and Modern","period":"Eighteenth century onward; region-specific political and social transitions","evidence":["company and state archives","newspapers","census records","oral histories","constitutional documents"]}
]
def list_periods():
    return [dict(item) for item in SOUTH_ASIAN_PERIODS]
