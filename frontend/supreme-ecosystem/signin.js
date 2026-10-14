"use strict";
document.addEventListener("DOMContentLoaded",()=>{
  const feedback=document.getElementById("copy-feedback");
  document.querySelectorAll("[data-copy]").forEach(button=>{
    button.addEventListener("click",async()=>{
      const value=button.getAttribute("data-copy")||"";
      try{
        if(!navigator.clipboard||!window.isSecureContext)throw new Error("Clipboard unavailable");
        await navigator.clipboard.writeText(value);
        if(feedback)feedback.textContent="Copied: "+value;
      }catch(_error){
        if(feedback)feedback.textContent="Select and copy: "+value;
      }
    });
  });
});
