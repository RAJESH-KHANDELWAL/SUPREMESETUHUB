"use strict";
const API="https://supremesetuhub-3v4e.onrender.com";
const REPOSITORY="https://api.github.com/repos/RAJESH-KHANDELWAL/SUPREMESETUHUB";
const token=localStorage.getItem("supreme_ecosystem_token");

function setBadge(id,state,label){
  const el=document.getElementById(id); if(!el)return;
  el.className="badge "+state; el.textContent=label;
}
function safeUrl(value){
  try{const u=new URL(value);return u.protocol==="https:"||u.protocol==="http:"?u.href:"";}
  catch(_){return "";}
}
async function checkApi(){
  const detail=document.getElementById("apiDetail");
  setBadge("apiBadge","pending","CHECKING");
  try{
    const r=await fetch(API+"/health",{headers:{Accept:"application/json"},cache:"no-store"});
    const body=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error("HTTP "+r.status);
    setBadge("apiBadge","ok","RESPONDING");
    detail.textContent="Backend health endpoint responded successfully. "+(body.status||body.message||"Health response received.");
  }catch(e){setBadge("apiBadge","bad","UNREACHABLE");detail.textContent="Could not confirm backend health from this browser: "+e.message;}
}
async function checkGithub(){
  const detail=document.getElementById("githubDetail");
  setBadge("githubBadge","pending","CHECKING");
  try{
    const r=await fetch(REPOSITORY,{headers:{Accept:"application/vnd.github+json"},cache:"no-store"});
    const data=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(data.message||("HTTP "+r.status));
    setBadge("githubBadge","ok","REACHABLE");
    const date=data.pushed_at?new Date(data.pushed_at).toLocaleString():"unknown";
    detail.textContent="Repository API responded. Default branch: "+(data.default_branch||"unknown")+". Last push: "+date+". This checks repository metadata, not private workflows or deployment health.";
  }catch(e){setBadge("githubBadge","bad","CHECK FAILED");detail.textContent="GitHub metadata check failed: "+e.message;}
}
async function checkWordPress(){
  const input=document.getElementById("wordpressUrl");
  const detail=document.getElementById("wordpressDetail");
  const url=safeUrl(input.value.trim());
  if(!url){setBadge("wordpressBadge","pending","NEEDS URL");detail.textContent="Enter a valid http:// or https:// WordPress website URL. Browser cross-origin restrictions may prevent a direct response check.";return;}
  setBadge("wordpressBadge","pending","CHECKING");
  detail.textContent="Checking website reachability…";
  try{
    // no-cors can only establish that the browser request did not throw; it cannot read the site's HTTP status.
    await fetch(url,{mode:"no-cors",cache:"no-store"});
    setBadge("wordpressBadge","pending","REQUEST SENT");
    detail.textContent="The browser sent a reachability request, but WordPress HTTP status cannot be verified cross-origin. Reliable monitoring requires a server-side URL check.";
  }catch(e){setBadge("wordpressBadge","bad","UNCONFIRMED");detail.textContent="The browser could not confirm a connection: "+e.message+". A server-side monitor is needed for reliable results.";}
}
async function loadPrivate(path,target){
  const el=document.getElementById(target);
  try{
    const r=await fetch(API+path,{headers:{Authorization:"Bearer "+token,Accept:"application/json"},cache:"no-store"});
    const data=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(data.detail||"REQUEST FAILED: "+r.status);
    el.textContent=JSON.stringify(data,null,2);
  }catch(e){
    el.textContent=e.message;
    if(/AUTHENTICATION_REQUIRED|INVALID_OR_EXPIRED_TOKEN|SUPREME_ECOSYSTEM_PRIVATE/.test(e.message)){
      localStorage.removeItem("supreme_ecosystem_token");
    }
  }
}

function escapeHtml(value){
  return String(value ?? "").replace(/[&<>"']/g, ch => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
}
function initials(name){
  const clean=String(name||"SUPREME").replace(/[👑🌍🧠💼🏢🏡❤️]/gu,"").trim();
  return clean.split(/\s+/).filter(Boolean).slice(0,2).map(part=>part[0]).join("").toUpperCase()||"SK";
}
function profileField(label,value){
  return '<div class="profile-field"><span>'+escapeHtml(label)+'</span><strong>'+escapeHtml(value||"NOT REGISTERED")+'</strong></div>';
}
function renderOwnerProfiles(data){
  const grid=document.getElementById("ownerProfilesGrid");
  const status=document.getElementById("profilesStatus");
  const profiles=Array.isArray(data.profiles)?data.profiles:[];
  status.textContent=profiles.length ? profiles.length+" profiles loaded from the private SUPREME registry." : "No profiles were returned.";
  grid.innerHTML=profiles.map((p,index)=>{
    const name=p.display_name||p.brand||"OWNER PROFILE";
    const monogram=initials(name);
    const cover=p.cover_url ? '<img class="profile-cover-image" src="'+escapeHtml(p.cover_url)+'" alt="'+escapeHtml(name)+' cover photo" loading="lazy" referrerpolicy="no-referrer">' : '<div class="profile-cover-placeholder cover-'+(index+1)+'"><span>COVER PHOTO NOT SET</span></div>';
    const avatar=p.avatar_url ? '<img class="profile-avatar-image" src="'+escapeHtml(p.avatar_url)+'" alt="'+escapeHtml(name)+' profile photo" loading="lazy" referrerpolicy="no-referrer">' : '<div class="profile-avatar-placeholder">'+escapeHtml(monogram)+'</div>';
    const domain=String(p.domain_name||"").toLowerCase();
    const domainLink=/^[a-z0-9.-]+\.[a-z]{2,}$/i.test(domain) ? '<a href="https://'+escapeHtml(domain)+'" target="_blank" rel="noopener noreferrer">OPEN WEBSITE ↗</a>' : "";
    return '<article class="owner-profile-card"><div class="profile-cover">'+cover+'</div><div class="profile-identity">'+avatar+'<span class="profile-state '+(p.avatar_url&&p.cover_url?'configured':'missing')+'">'+(p.avatar_url&&p.cover_url?'IMAGES CONFIGURED':'IMAGES NOT SET')+'</span></div><div class="profile-card-body"><h3>'+escapeHtml(name)+'</h3><p class="profile-tagline">'+escapeHtml(p.tagline||"SUPREME OWNER PROFILE")+'</p>'+profileField("USERNAME",p.username)+profileField("DOMAIN",p.domain_name)+profileField("PROFILE ID",p.profile_id)+profileField("USER ID",p.user_id)+profileField("BUSINESS ID",p.business_id)+profileField("COMPANY ID",p.company_id)+profileField("PAGE ID",p.page_id)+profileField("CHANNEL ID",p.channel_id)+profileField("COMMUNITY ID",p.community_id)+profileField("GROUP ID",p.group_id)+'<div class="profile-card-footer">'+domainLink+'<span>SUPREME INTERNAL REGISTRY</span></div></div></article>';
  }).join("");
}
async function loadOwnerProfiles(){
  const status=document.getElementById("profilesStatus");
  status.textContent="Loading profiles securely…";
  try{
    const r=await fetch(API+"/api/v1/supreme-ecosystem/owner-admin/profiles",{headers:{Authorization:"Bearer "+token,Accept:"application/json"},cache:"no-store"});
    const data=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(data.detail||"PROFILE REQUEST FAILED: "+r.status);
    renderOwnerProfiles(data);
  }catch(e){
    status.textContent="Could not load profiles: "+e.message+". Sign in with the SUPREME owner account and confirm the backend deployment includes the profiles endpoint.";
    document.getElementById("ownerProfilesGrid").innerHTML="";
    if(/AUTHENTICATION_REQUIRED|INVALID_OR_EXPIRED_TOKEN|SUPREME_ECOSYSTEM_PRIVATE/.test(e.message))localStorage.removeItem("supreme_ecosystem_token");
  }
}

const BACKEND_ROUTE_PANELS=[
  {title:"OWNER ADMIN STATUS",path:"/api/v1/supreme-ecosystem/owner-admin/status"},
  {title:"OWNED PLATFORMS",path:"/api/v1/supreme-ecosystem/owner-admin/owned-platforms"},
  {title:"GOOGLE OWNER ACCOUNTS",path:"/api/v1/supreme-ecosystem/owner-admin/google-accounts"},
  {title:"SOCIAL PLATFORMS",path:"/api/v1/supreme-ecosystem/owner-admin/social-platforms"},
  {title:"BUSINESS COACH PROFILE",path:"/api/v1/supreme-ecosystem/owner-admin/business-coach-profile"},
  {title:"OWNER GOVERNANCE",path:"/api/v1/supreme-ecosystem/owner-admin/governance"},
  {title:"CAPABILITY CATALOG",path:"/api/v1/supreme-ecosystem/capabilities"},
  {title:"CONTROL PLANE STATUS",path:"/api/v1/supreme-ecosystem/control/status"},
  {title:"BUSINESS ECOSYSTEM",path:"/api/v1/supreme-ecosystem/business/status"},
  {title:"AI ECOSYSTEM",path:"/api/v1/supreme-ecosystem/ai/status"},
  {title:"ACCOUNT DASHBOARD",path:"/api/v1/supreme-ecosystem/dashboard"}
];
function moduleLabel(name){
  return String(name||"MODULE").replace(/_/g," ");
}
async function loadBackendModuleMap(){
  const status=document.getElementById("backendModulesStatus");
  const grid=document.getElementById("backendModulesGrid");
  const panelGrid=document.getElementById("backendRoutePanels");
  status.textContent="Fetching module registry from the backend…";
  try{
    const response=await fetch(API+"/api/v1/supreme-ecosystem/status",{headers:{Authorization:"Bearer "+token,Accept:"application/json"},cache:"no-store"});
    const data=await response.json().catch(()=>({}));
    if(!response.ok)throw new Error(data.detail||"BACKEND MODULE REQUEST FAILED: "+response.status);
    const modules=Array.isArray(data.modules)?data.modules:[];
    grid.innerHTML=modules.map((name,index)=>{
      const label=moduleLabel(name);
      return '<article class="card module-link"><span class="service-icon">'+String(index+1).padStart(2,"0")+'</span><h3>'+escapeHtml(label)+'</h3><p>Registered by the live SUPREME ECOSYSTEM backend status endpoint.</p><span>BACKEND REGISTERED MODULE</span></article>';
    }).join("");
    status.textContent=modules.length+" module entries loaded from "+API+"/api/v1/supreme-ecosystem/status · Parent: "+escapeHtml(data.parent||"NOT RETURNED")+" · Privacy: "+escapeHtml(data.privacy||"NOT RETURNED");
  }catch(e){
    status.textContent="Backend module list could not load: "+e.message;
    grid.innerHTML="";
    if(/AUTHENTICATION_REQUIRED|INVALID_OR_EXPIRED_TOKEN|SUPREME_ECOSYSTEM_PRIVATE/.test(e.message))localStorage.removeItem("supreme_ecosystem_token");
  }
  panelGrid.innerHTML=BACKEND_ROUTE_PANELS.map((item,index)=>'<section class="card"><div class="card-top"><h3>'+escapeHtml(item.title)+'</h3><span id="routeBadge'+index+'" class="badge pending">LOADING</span></div><p class="subtle">'+escapeHtml(item.path)+'</p><pre id="routeData'+index+'">Loading backend response…</pre></section>').join("");
  await Promise.all(BACKEND_ROUTE_PANELS.map(async(item,index)=>{
    const target=document.getElementById("routeData"+index);
    const badge=document.getElementById("routeBadge"+index);
    try{
      const response=await fetch(API+item.path,{headers:{Authorization:"Bearer "+token,Accept:"application/json"},cache:"no-store"});
      const data=await response.json().catch(()=>({}));
      if(!response.ok)throw new Error(data.detail||"HTTP "+response.status);
      target.textContent=JSON.stringify(data,null,2);
      badge.className="badge ok";badge.textContent="RESPONDED";
    }catch(e){
      target.textContent=e.message;
      badge.className="badge bad";badge.textContent="FAILED";
      if(/AUTHENTICATION_REQUIRED|INVALID_OR_EXPIRED_TOKEN|SUPREME_ECOSYSTEM_PRIVATE/.test(e.message))localStorage.removeItem("supreme_ecosystem_token");
    }
  }));
}
document.getElementById("refreshBackendModules").addEventListener("click",loadBackendModuleMap);

async function refreshAll(){
  const button=document.getElementById("refreshAll");
  button.disabled=true;
  document.getElementById("lastUpdated").textContent="CHECKING…";
  await Promise.all([checkApi(),checkGithub()]);
  if(document.getElementById("wordpressUrl").value.trim())await checkWordPress();
  document.getElementById("lastUpdated").textContent="LAST CHECK: "+new Date().toLocaleString();
  button.disabled=false;
}
document.getElementById("refreshAll").addEventListener("click",refreshAll);
document.getElementById("refreshProfiles").addEventListener("click",loadOwnerProfiles);
document.getElementById("checkWordPress").addEventListener("click",checkWordPress);
document.getElementById("signOut").addEventListener("click",()=>{localStorage.removeItem("supreme_ecosystem_token");window.location.replace("signin.html");});

if(!token){window.location.replace("signin.html");}
else{
  loadPrivate("/api/v1/supreme-ecosystem/status","status");
  loadPrivate("/api/v1/supreme-ecosystem/account","account");
  loadPrivate("/api/v1/supreme-ecosystem/integrations","integrations");
  loadOwnerProfiles();
  loadBackendModuleMap();
}
document.getElementById("hostingerBadge").textContent="NEEDS API";
refreshAll();
