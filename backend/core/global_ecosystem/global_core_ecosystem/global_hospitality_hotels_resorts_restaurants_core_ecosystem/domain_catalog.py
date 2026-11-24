"""Canonical hospitality industry taxonomy; no live listings."""
from copy import deepcopy

DOMAINS = {
"accommodation": ["Hotels","Resorts","Motels","Hostels","Boutique hotels","Serviced apartments","Homestays","Guest houses","Vacation rentals","Eco lodges","Heritage stays","Extended-stay properties"],
"food_beverage": ["Fine dining","Casual dining","Quick-service restaurants","Cafes","Bakeries","Cloud kitchens","Catering","Food trucks","Bars and beverage service","Central kitchens","Menu engineering","Food sourcing","Allergen management"],
"guest_experience": ["Discovery","Enquiries","Reservations","Pre-arrival","Check-in","Guest services","Housekeeping","Concierge","Check-out","Feedback","Complaint handling","Loyalty"],
"distribution": ["Direct bookings","Group bookings","Corporate bookings","Online travel agencies","Global distribution systems","Channel management","Rate plans","Availability metadata","Cancellation policies"],
"property_operations": ["Front office","Rooms division","Housekeeping","Laundry","Engineering","Maintenance","Security","Parking","Recreation","Spa","Pool operations","Facilities management","Asset lifecycle"],
"events": ["Banquets","Weddings","Meetings","Conferences","Exhibitions","Celebrations","Event catering","Venue operations","Audio visual coordination"],
"workforce": ["Front office roles","Housekeeping roles","Kitchen roles","Food service roles","Management roles","Maintenance roles","Security roles","Recruitment","Scheduling","Training","Workplace safety"],
"revenue": ["Room revenue","Food and beverage revenue","Revenue management","Rate strategy","Occupancy","Average daily rate","Revenue per available room","Demand forecasting","Cost controls"],
"safety_compliance": ["Food safety","Fire and life safety","Guest privacy","Workplace safety","Emergency readiness","Incident reporting","Accessibility","Licensing checkpoints","Consumer protection"],
"sustainability": ["Energy efficiency","Water stewardship","Waste reduction","Food waste","Responsible sourcing","Community engagement","Biodiversity","Sustainable tourism"],
"technology_data": ["Property management systems","Point of sale","Customer relationship management","Booking engines","Channel managers","Revenue systems","Guest messaging","Analytics","Cybersecurity","Data governance"],
"supply_chain": ["Food suppliers","Linen and amenities","Furniture and fixtures","Kitchen equipment","Cleaning supplies","Maintenance materials","Vendor onboarding","Inventory controls","Procurement"],
"accessibility": ["Accessible rooms","Accessible dining","Mobility access","Assistive communication","Inclusive service design","Accessible events"],
"geography": ["Country","State or province","District or county","City","Town","Locality","Tourism region","Destination"],
}

def list_domains():
    return [{"id": key, "capabilities": list(values)} for key, values in DOMAINS.items()]

def get_domain(domain_id):
    key = str(domain_id or "").strip().lower()
    values = DOMAINS.get(key)
    return {"id": key, "capabilities": list(values)} if values is not None else None

def search_domains(query=""):
    term = str(query or "").strip().casefold()
    return [item for item in list_domains() if not term or term in item["id"].casefold() or any(term in value.casefold() for value in item["capabilities"])]

def catalog_snapshot():
    return {"domains": deepcopy(DOMAINS), "domain_count": len(DOMAINS), "capability_count": sum(len(v) for v in DOMAINS.values())}
