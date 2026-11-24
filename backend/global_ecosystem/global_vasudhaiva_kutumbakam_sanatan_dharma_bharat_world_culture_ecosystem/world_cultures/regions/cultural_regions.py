"""World cultural regions for comparative discovery, not fixed civilisational boxes."""
WORLD_CULTURAL_REGIONS = {
 "south_asia":{"label":"South Asia","coverage":["India","Pakistan","Bangladesh","Nepal","Bhutan","Sri Lanka","Maldives"],"comparative_axes":["language families","religious histories","trade and migration","foodways","performance","colonial and postcolonial history"]},
 "east_asia":{"label":"East Asia","coverage":["China","Japan","Korea","Taiwan and diasporic communities"],"comparative_axes":["writing systems","philosophical traditions","court and popular arts","religious exchange","modernisation"]},
 "southeast_asia":{"label":"Southeast Asia","coverage":["Mainland and maritime Southeast Asian societies"],"comparative_axes":["Austronesian and Austroasiatic languages","Indic and Sinic exchange","Islamic histories","maritime networks","indigenous knowledge"]},
 "west_asia_north_africa":{"label":"West Asia and North Africa","coverage":["Arab societies","Iran","Anatolia","Levant","North Africa"],"comparative_axes":["Semitic and Iranian languages","religious pluralities","trade routes","urban histories","oral and written literatures"]},
 "africa":{"label":"Africa","coverage":["North, West, Central, East and Southern Africa"],"comparative_axes":["language diversity","kingdoms and states","oral literature","material culture","ecological knowledge","diaspora"]},
 "europe":{"label":"Europe","coverage":["Northern, Southern, Western, Central and Eastern Europe"],"comparative_axes":["language families","classical and medieval texts","religious change","folk traditions","migration"]},
 "americas":{"label":"The Americas","coverage":["North America","Central America","Caribbean","South America"],"comparative_axes":["Indigenous nations","colonial encounters","African diasporas","language revitalisation","land-based knowledge"]},
 "oceania":{"label":"Oceania","coverage":["Australia","Melanesia","Micronesia","Polynesia"],"comparative_axes":["First Nations and Indigenous sovereignty","navigation","oral genealogies","language revitalisation","oceanic knowledge"]}
}
def list_world_regions():
    return [{"id":key, **value} for key,value in WORLD_CULTURAL_REGIONS.items()]
