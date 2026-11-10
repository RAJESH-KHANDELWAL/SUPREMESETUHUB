"""Yajna and ritual study taxonomy; descriptive rather than prescriptive."""
YAJNA_STUDY_AREAS = {
 "shrauta":{"description":"Large-scale Vedic śrauta ritual systems based on Vedic textual traditions.","research_fields":["Veda and recension","ritual manuals","officiant roles","altar geometry","mantra corpus","historical performance"]},
 "grihya":{"description":"Domestic rites described in Grihya Sutras and later ritual manuals.","research_fields":["life-cycle rite","household context","regional custom","textual source","contemporary practice"]},
 "agnihotra":{"description":"A daily fire offering practice with variations in textual prescription and living observance.","research_fields":["source tradition","timing","materials","mantra","lineage","modern observance"]},
 "temple_ritual":{"description":"Temple worship systems with Agamic, Puranic and regional forms.","research_fields":["Agama or ritual manual","temple lineage","daily schedule","festival cycle","custodian authority"]}
}
def list_yajna_areas():
    return {key:dict(value) for key,value in YAJNA_STUDY_AREAS.items()}
