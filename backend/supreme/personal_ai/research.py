"""Private SUPREME PERSONAL AI public-business/opportunity research."""
from __future__ import annotations
import os, sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import httpx

DB_PATH=Path(os.getenv("SUPREME_PERSONAL_AI_DB","supreme_personal_ai.db"))
SEARCH_URL="https://www.googleapis.com/customsearch/v1"
TRACKS: dict[str,dict[str,Any]]={
 "wordpress_website":{"label":"WordPress websites and maintenance","horizon":"SHORT_AND_LONG_TERM","queries":['"WordPress developer needed" freelance business website','"website maintenance" small business freelancer','"WordPress website redesign" business']},
 "seo_content":{"label":"SEO and content writing","horizon":"SHORT_AND_LONG_TERM","queries":['"SEO content writer" freelance project','"website content writing" small business','"local SEO" small business website service']},
 "copywriting":{"label":"Copywriting and marketing content","horizon":"SHORT_TERM","queries":['"copywriter needed" freelance project','"landing page copywriter" project agency','"email copywriting" small business freelance']},
 "recurring_maintenance":{"label":"Recurring website care plans","horizon":"LONG_TERM","queries":['"WordPress care plan" small business partnership','"website support retainer" freelance WordPress','"monthly SEO content" small business agency']}
}
def _db():
 DB_PATH.parent.mkdir(parents=True,exist_ok=True)
 c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row
 c.execute("""CREATE TABLE IF NOT EXISTS research_results(id INTEGER PRIMARY KEY,track TEXT,horizon TEXT,title TEXT,url TEXT UNIQUE,snippet TEXT,source TEXT,researched_at TEXT)"""); c.commit(); return c
def status():
 configured=bool(os.getenv("GOOGLE_CSE_API_KEY","").strip() and os.getenv("GOOGLE_CSE_ID","").strip())
 with _db() as c: count=c.execute("SELECT COUNT(*) FROM research_results").fetchone()[0]
 return {"success":True,"system":"SUPREME PERSONAL AI","privacy":"PRIVATE_BY_DEFAULT","research_provider":"GOOGLE_PROGRAMMABLE_SEARCH","research_configured":configured,"tracks":list(TRACKS),"saved_research_items":count,"message_sending":"DRAFT_ONLY"}
async def research(track="all",limit_per_query=5):
 key=os.getenv("GOOGLE_CSE_API_KEY","").strip(); cx=os.getenv("GOOGLE_CSE_ID","").strip()
 if not key or not cx: return {"success":False,"error":"GOOGLE_SEARCH_NOT_CONFIGURED","setup_required":["GOOGLE_CSE_API_KEY","GOOGLE_CSE_ID"]}
 if track!="all" and track not in TRACKS: return {"success":False,"error":"UNKNOWN_RESEARCH_TRACK","available_tracks":list(TRACKS)}
 chosen=TRACKS if track=="all" else {track:TRACKS[track]}; n=max(1,min(int(limit_per_query),10)); now=datetime.now(timezone.utc).isoformat(); found=[]; errors=[]
 async with httpx.AsyncClient(timeout=15) as client:
  for tid,info in chosen.items():
   for q in info["queries"]:
    try:
     r=await client.get(SEARCH_URL,params={"key":key,"cx":cx,"q":q,"num":n}); r.raise_for_status()
     for item in r.json().get("items",[]):
      url=str(item.get("link","")).strip(); title=str(item.get("title","")).strip()
      if not title or not url.startswith(("https://","http://")): continue
      found.append({"track":tid,"track_label":info["label"],"horizon":info["horizon"],"title":title[:500],"url":url[:2000],"snippet":str(item.get("snippet",""))[:2000],"source":"Google Programmable Search","researched_at":now})
    except (httpx.HTTPError,ValueError) as e: errors.append({"query":q,"error":type(e).__name__})
 with _db() as c:
  for x in found:
   c.execute("""INSERT INTO research_results(track,horizon,title,url,snippet,source,researched_at) VALUES(?,?,?,?,?,?,?) ON CONFLICT(url) DO UPDATE SET track=excluded.track,horizon=excluded.horizon,title=excluded.title,snippet=excluded.snippet,source=excluded.source,researched_at=excluded.researched_at""",(x["track"],x["horizon"],x["title"],x["url"],x["snippet"],x["source"],x["researched_at"]))
  c.commit()
 unique={x["url"]:x for x in found}
 return {"success":bool(unique) or not errors,"track":track,"searched_tracks":list(chosen),"count":len(unique),"results":list(unique.values()),"errors":errors,"note":"Verify opportunity, business legitimacy, public contact details and project budget before outreach."}
def list_results(track=None,limit=50):
 n=max(1,min(int(limit),200))
 if track and track not in TRACKS: return {"success":False,"error":"UNKNOWN_RESEARCH_TRACK","available_tracks":list(TRACKS)}
 with _db() as c:
  rows=c.execute("SELECT * FROM research_results"+(" WHERE track=?" if track else "")+" ORDER BY researched_at DESC LIMIT ?",((track,n) if track else (n,))).fetchall()
 return {"success":True,"count":len(rows),"results":[dict(x) for x in rows]}
def draft_outreach(business_name,service,public_context,contact_name="",channel="email"):
 name=business_name.strip(); service=service.strip(); context=public_context.strip()
 if not name or not service or not context: raise ValueError("BUSINESS_NAME_SERVICE_AND_PUBLIC_CONTEXT_REQUIRED")
 greeting=f"Hello {contact_name.strip()}," if contact_name.strip() else "Hello,"
 if channel.lower()=="whatsapp":
  body=f"{greeting}\nI came across {name} and noticed {context}. I help businesses with {service}. If relevant, may I share a short suggestion? If not, no worries."
 else:
  body=f"{greeting}\n\nI came across {name} and noticed {context}. I provide {service} for businesses improving their online presence. If this is relevant, I can share a brief tailored suggestion and clear scope/pricing.\n\nIf this isn't relevant, let me know and I won't follow up.\n\nRegards,\nDR RAJESH KHANDELWAL IBC\nINDEPENDENT BUSINESS CONSULTANT"
 return {"channel":channel.lower(),"business_name":name,"subject":f"Idea for {name}: {service}" if channel.lower()=="email" else "","message":body,"status":"DRAFT_ONLY","next_step":"Review before sending"}
