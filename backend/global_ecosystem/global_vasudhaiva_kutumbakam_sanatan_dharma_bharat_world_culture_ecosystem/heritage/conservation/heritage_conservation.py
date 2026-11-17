"""Heritage conservation workflow and risk assessment vocabulary."""
CONSERVATION_WORKFLOW = [
 "Identify the heritage object, place, practice or cultural landscape.",
 "Document legal status, custodianship, ownership and community authority.",
 "Record physical condition, intangible continuity and environmental threats.",
 "Collect provenance, archival history, oral testimony and prior interventions.",
 "Assess risks: climate, urban development, conflict, tourism pressure, theft and neglect.",
 "Consult local communities and relevant conservation specialists.",
 "Select the least harmful intervention and document all materials and methods.",
 "Monitor condition and community access after intervention."
]
HERITAGE_TYPES = {
 "tangible_immovable":["monuments","archaeological sites","historic buildings","cultural landscapes"],
 "tangible_movable":["manuscripts","sculptures","paintings","textiles","archaeological objects"],
 "intangible":["oral traditions","performing arts","rituals","festive events","craft knowledge"],
 "natural_and_biocultural":["sacred groves","cultural landscapes","community ecological knowledge"]
}
def get_conservation_framework():
    return {"workflow":list(CONSERVATION_WORKFLOW),"types":{k:list(v) for k,v in HERITAGE_TYPES.items()}}
