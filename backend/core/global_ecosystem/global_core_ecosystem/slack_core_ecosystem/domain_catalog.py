"""Slack product grouping and domain inventory."""
from collections import defaultdict
from .product_catalog import PRODUCTS
DOMAIN_DEFINITIONS={"ADMINISTRATION":{"name":"Workspace Administration"},"CONTENT":{"name":"Files, Bookmarks and Canvases"},"COLLABORATION":{"name":"Conversations and Lists"},"EVENTS":{"name":"Events and Webhooks"},"MESSAGING":{"name":"Messages and Reactions"},"IDENTITY":{"name":"OAuth and User Identity"},"DISCOVERY":{"name":"Search and Discovery"},"AUTOMATION":{"name":"Workflow Automation"}}
def list_domain_inventory():
 grouped=defaultdict(list)
 for p in PRODUCTS:grouped[p["domain_id"]].append(p["product_id"])
 return [{"domain_id":k,**DOMAIN_DEFINITIONS[k],"product_ids":sorted(v),"product_count":len(v)} for k,v in sorted(grouped.items())]
def domain_summary():
 items=list_domain_inventory()
 return {"success":True,"domain_count":len(items),"product_count":sum(x["product_count"] for x in items),"domains":items}
