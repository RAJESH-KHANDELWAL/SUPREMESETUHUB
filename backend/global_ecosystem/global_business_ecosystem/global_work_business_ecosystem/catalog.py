"""Canonical work and workforce categories; labels are searchable aliases."""
from __future__ import annotations
CATEGORIES = {
"employees":{"name":"Employees","role_names":["Employee","Salaried Worker","Staff Member","Wage Employee","Private-sector Employee","Public-sector Employee"],"responsibilities":["Perform work under an employment relationship","Deliver assigned duties under agreed terms"]},
"employers":{"name":"Employers","role_names":["Employer","Hiring Organization","Business Employer","Household Employer"],"responsibilities":["Engage and organize workers","Set work terms and meet applicable employer duties"]},
"government_public_workers":{"name":"Government and Public Workers","role_names":["Government Employee","Public Servant","Civil Servant","Public-sector Worker","Municipal Worker"],"responsibilities":["Deliver public administration or public services","Work within applicable public-service rules"]},
"managers_and_supervisors":{"name":"Managers and Supervisors","role_names":["Manager","General Manager","Operations Manager","Department Head","Supervisor","Team Lead"],"responsibilities":["Plan work and allocate resources","Coordinate teams and monitor delivery"]},
"professionals":{"name":"Professionals","role_names":["Professional","Licensed Professional","Knowledge Worker","Specialist","Practitioner"],"responsibilities":["Apply advanced domain knowledge","Deliver professional services within competence and licensing limits"]},
"technicians_and_associate_professionals":{"name":"Technicians and Associate Professionals","role_names":["Technician","Technical Associate","Engineering Technician","IT Technician","Associate Professional"],"responsibilities":["Perform technical and applied tasks","Support professional and operational teams"]},
"clerical_and_administrative_workers":{"name":"Clerical and Administrative Workers","role_names":["Clerk","Administrative Assistant","Office Assistant","Secretary","Records Clerk","Data-entry Clerk"],"responsibilities":["Maintain records and office processes","Coordinate documentation and administration"]},
"service_and_sales_workers":{"name":"Service and Sales Workers","role_names":["Service Worker","Salesperson","Retail Sales Worker","Customer Service Representative","Hospitality Worker"],"responsibilities":["Serve customers and clients","Support sales, retail and hospitality operations"]},
"agriculture_forestry_and_fishery_workers":{"name":"Agriculture, Forestry and Fishery Workers","role_names":["Farmer","Agricultural Worker","Forestry Worker","Fisher","Aquaculture Worker","Farm Labourer"],"responsibilities":["Produce agricultural, forestry or fishery goods","Maintain farm and natural-resource operations"]},
"craft_and_trade_workers":{"name":"Craft and Trade Workers","role_names":["Craft Worker","Artisan","Electrician","Plumber","Carpenter","Mason","Mechanic"],"responsibilities":["Perform skilled manual and trade work","Build, repair, install or maintain products and infrastructure"]}
}
def get_category(category_id):
    return CATEGORIES.get(category_id.strip().lower())
def search_roles(query):
    q=query.strip().casefold()
    if not q: return []
    return [{"id":k,**v} for k,v in CATEGORIES.items() if q in (k+" "+v["name"]+" "+" ".join(v["role_names"])+" "+" ".join(v["responsibilities"])).casefold()]
