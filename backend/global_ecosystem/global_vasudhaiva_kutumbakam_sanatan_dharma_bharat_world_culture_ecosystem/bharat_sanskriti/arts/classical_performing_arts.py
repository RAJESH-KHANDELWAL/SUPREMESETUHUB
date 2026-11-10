"""Classical performing arts reference map with source and lineage fields."""
CLASSICAL_PERFORMING_ARTS = {
 "bharatanatyam":{"form":"Bharatanatyam","primary_region":"Tamil Nadu","medium":"Dance","study":["nritta","nritya","natya","abhinaya","repertoire","modern revival history"],"caution":"Modern stage practice has a documented history of change; do not claim an unchanged form across all centuries."},
 "kathak":{"form":"Kathak","primary_region":"North India","medium":"Dance","study":["gharana histories","storytelling","rhythm","court and devotional contexts","modern institutions"]},
 "kathakali":{"form":"Kathakali","primary_region":"Kerala","medium":"Dance-drama","study":["make-up and costume","mudra","music","performance texts","temple and court histories"]},
 "kuchipudi":{"form":"Kuchipudi","primary_region":"Andhra Pradesh","medium":"Dance-drama and dance","study":["village performance history","Yakshagana connections","repertoire","modern solo format"]},
 "odissi":{"form":"Odissi","primary_region":"Odisha","medium":"Dance","study":["temple sculpture and performance debates","Mahari and Gotipua histories","reconstruction and modern pedagogy"]},
 "manipuri":{"form":"Manipuri","primary_region":"Manipur","medium":"Dance","study":["Ras Lila","Vaishnava influences","Lai Haraoba","community performance"]},
 "mohiniyattam":{"form":"Mohiniyattam","primary_region":"Kerala","medium":"Dance","study":["lasya","music","costume","modern institutional history"]},
 "sattriya":{"form":"Sattriya","primary_region":"Assam","medium":"Dance","study":["Sattras","Ankiya Naat","Sankardev tradition","community and stage forms"]},
 "hindustani_music":{"form":"Hindustani classical music","primary_region":"North and Central India","medium":"Music","study":["raga","tala","gharana","dhrupad","khayal","instrumental traditions"]},
 "carnatic_music":{"form":"Carnatic classical music","primary_region":"South India","medium":"Music","study":["raga","tala","kriti","compositional traditions","concert history"]}
}
def list_performing_arts():
    return [{"id":key, **value} for key,value in CLASSICAL_PERFORMING_ARTS.items()]
