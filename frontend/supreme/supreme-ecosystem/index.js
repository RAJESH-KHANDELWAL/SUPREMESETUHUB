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
document.getElementById("checkWordPress").addEventListener("click",checkWordPress);
document.getElementById("signOut").addEventListener("click",()=>{localStorage.removeItem("supreme_ecosystem_token");window.location.replace("signin.html");});

if(!token){window.location.replace("signin.html");}
else{
  loadPrivate("/api/v1/supreme-ecosystem/status","status");
  loadPrivate("/api/v1/supreme-ecosystem/account","account");
  loadPrivate("/api/v1/supreme-ecosystem/integrations","integrations");
}
document.getElementById("hostingerBadge").textContent="NEEDS API";
refreshAll();
