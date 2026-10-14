const API="https://supremesetuhub-3v4e.onrender.com";
const token=localStorage.getItem("supreme_ecosystem_token");
if(!token){window.location.replace("signin.html");}
async function loadPrivate(path,target){
  const el=document.getElementById(target);
  try{
    const r=await fetch(API+path,{headers:{Authorization:"Bearer "+token,Accept:"application/json"}});
    const data=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(data.detail||"REQUEST FAILED: "+r.status);
    el.textContent=JSON.stringify(data,null,2);
  }catch(e){el.textContent=e.message; if(/AUTHENTICATION_REQUIRED|INVALID_OR_EXPIRED_TOKEN|SUPREME_ECOSYSTEM_PRIVATE/.test(e.message)){localStorage.removeItem("supreme_ecosystem_token");}}
}
if(token){
  loadPrivate("/api/v1/supreme-ecosystem/status","status");
  loadPrivate("/api/v1/supreme-ecosystem/account","account");
  loadPrivate("/api/v1/supreme-ecosystem/integrations","integrations");
}
document.getElementById("signOut").addEventListener("click",()=>{localStorage.removeItem("supreme_ecosystem_token");window.location.replace("signin.html");});