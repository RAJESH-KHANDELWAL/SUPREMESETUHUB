"""Regional culture map for Bharat; a discovery taxonomy, not a claim of uniformity."""
REGIONAL_CULTURE_ZONES = {
 "north":{"label":"Northern India","study_states":["Punjab","Haryana","Himachal Pradesh","Uttarakhand","Uttar Pradesh","Rajasthan","Delhi","Jammu and Kashmir","Ladakh"],"dimensions":["languages and dialects","foodways","dress and textiles","folk music","architecture","pilgrimage","seasonal festivals"]},
 "west":{"label":"Western India","study_states":["Gujarat","Maharashtra","Goa"],"dimensions":["Gujarati and Marathi literary traditions","coastal and inland foodways","Bhakti movements","crafts and textiles","maritime history"]},
 "south":{"label":"Southern India","study_states":["Andhra Pradesh","Telangana","Karnataka","Kerala","Tamil Nadu"],"dimensions":["Dravidian languages","temple architecture","classical and folk performance","Sangam and medieval literature","coastal trade","regional ritual traditions"]},
 "east":{"label":"Eastern India","study_states":["Bihar","Jharkhand","Odisha","West Bengal"],"dimensions":["Indo-Aryan and Austroasiatic languages","tribal and regional traditions","Buddhist and Jain heritage","Jagannath traditions","literature","crafts"]},
 "north_east":{"label":"Northeastern India","study_states":["Assam","Arunachal Pradesh","Manipur","Meghalaya","Mizoram","Nagaland","Tripura","Sikkim"],"dimensions":["Tibeto-Burman and other language families","community governance","weaving","oral epics","music and dance","ecological knowledge"]},
 "central":{"label":"Central India","study_states":["Madhya Pradesh","Chhattisgarh"],"dimensions":["Adivasi communities","forest-linked knowledge","rock art","folk performance","crafts","regional languages"]}
}
def list_regions():
    return [{"id":key, **value} for key,value in REGIONAL_CULTURE_ZONES.items()]
