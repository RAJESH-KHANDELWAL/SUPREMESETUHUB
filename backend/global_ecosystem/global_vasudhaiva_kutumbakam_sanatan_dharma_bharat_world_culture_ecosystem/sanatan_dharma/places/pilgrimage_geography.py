"""Pilgrimage geography data model and selected canonical study clusters."""
PILGRIMAGE_CLUSTERS = {
 "char_dham_tradition":{"name":"Char Dham (Uttarakhand usage)","places":["Yamunotri","Gangotri","Kedarnath","Badrinath"],"region":"Uttarakhand, India","caution":"Distinguish this Himalayan Char Dham circuit from the pan-Indian Char Dham associated with Shankaracharya tradition."},
 "pan_indian_char_dham":{"name":"Four-dham tradition","places":["Badrinath","Dwarka","Puri","Rameswaram"],"region":"Multiple regions of India","caution":"Historical development, pilgrimage practice and lists should be cited to specific sources."},
 "jyotirlinga":{"name":"Dvadasha Jyotirlinga tradition","count_traditional":12,"research_fields":["site name and location","regional tradition","temple history","inscriptions","living worship","heritage status"],"caution":"Temple histories may combine inscriptional evidence, local memory, Puranic narrative and later reconstruction."},
 "shakti_pitha":{"name":"Shakti Pitha traditions","count_note":"Lists vary among textual and regional traditions.","research_fields":["source text","regional list","site identification","community tradition","current custodians"],"caution":"Do not state a single universally accepted count without naming the source tradition."}
}
def list_pilgrimage_clusters():
    return {key:dict(value) for key,value in PILGRIMAGE_CLUSTERS.items()}
