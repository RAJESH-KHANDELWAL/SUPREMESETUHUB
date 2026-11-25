"""Jurisdiction overlays; these classify systems without duplicating core domains."""
REGIONAL_FRAMEWORKS = {
    "bharat": {
        "region_id": "BHARAT",
        "country_code": "IN",
        "scope": "India national, state, union-territory and local education systems",
        "frameworks": [
            "National Education Policy (NEP)",
            "NCF and NCERT curriculum frameworks",
            "CBSE, CISCE and State/UT school boards",
            "NIOS and open-schooling pathways",
            "UGC and university higher-education framework",
            "AICTE and technical education framework",
            "NCTE and teacher education framework",
            "NMC, DCI, INC, PCI and allied health regulators",
            "NTA examinations and national entrance pathways",
            "NCVET, NSDC, Skill India, ITI and apprenticeship systems",
            "National/State qualification and credit frameworks",
            "Central, State, private, deemed and autonomous institutions",
        ],
        "coverage": ["central", "state", "union_territory", "district", "rural", "urban", "tribal", "community"],
    },
    "global": {
        "region_id": "GLOBAL",
        "scope": "Cross-border and country-specific education systems worldwide",
        "frameworks": [
            "National and subnational education ministries",
            "International qualification and credit frameworks",
            "Country-specific school boards and examination authorities",
            "University and research governance systems",
            "Technical and vocational qualification frameworks",
            "International quality assurance and accreditation bodies",
            "Cross-border recognition and student mobility frameworks",
            "Open, distance and lifelong learning systems",
        ],
        "coverage": ["country", "state_or_province", "territory", "regional_union", "cross_border", "international"],
    },
}

def list_regional_frameworks():
    return {key: {"region_id": value["region_id"], "scope": value["scope"], "frameworks": list(value["frameworks"]), "coverage": list(value["coverage"])} for key, value in REGIONAL_FRAMEWORKS.items()}

def get_regional_framework(region_id):
    key = region_id.strip().casefold()
    value = REGIONAL_FRAMEWORKS.get(key)
    return None if value is None else list_regional_frameworks()[key]
