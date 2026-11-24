"""Regional security governance scope."""
REGIONS={"India":("central","state","union_territory","sectoral"),"Global":("country","cross_border","multiregional","international")}
def get_security_regions():
    return dict(REGIONS)
