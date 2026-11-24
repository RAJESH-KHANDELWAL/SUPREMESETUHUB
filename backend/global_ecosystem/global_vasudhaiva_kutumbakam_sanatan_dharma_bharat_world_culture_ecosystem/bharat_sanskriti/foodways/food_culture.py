"""Foodways knowledge model: regional, historical, ecological and community context."""
FOOD_CULTURE_DIMENSIONS = {
 "grains_and_millets":["rice","wheat","sorghum","pearl millet","finger millet","barley","regional pulses"],
 "food_systems":["monsoon agriculture","irrigation","pastoralism","coastal fisheries","forest foods","market networks"],
 "culinary_methods":["fermentation","steaming","roasting","sun drying","pickling","slow cooking","stone grinding"],
 "documentation_fields":["dish name in local script","community and region","ingredients with local names","seasonality","ritual or everyday context","oral-history source","historical source","dietary restrictions","consent and attribution"],
 "caution":"Avoid presenting a dish as belonging exclusively to one modern state when its history crosses communities and borders."
}
def get_food_culture_framework():
    return {key:list(value) if isinstance(value,list) else value for key,value in FOOD_CULTURE_DIMENSIONS.items()}
