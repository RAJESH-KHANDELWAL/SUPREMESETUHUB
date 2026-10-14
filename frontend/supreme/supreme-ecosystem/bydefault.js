"use strict";
document.addEventListener("DOMContentLoaded",()=>{
 document.querySelectorAll("[data-current-year]").forEach(el=>{el.textContent=String(new Date().getFullYear());});
 document.querySelectorAll("[data-copy]").forEach(button=>{
  button.addEventListener("click",async()=>{
   const value=button.getAttribute("data-copy")||"";
   const feedback=document.getElementById("copy-feedback");
   try{await navigator.clipboard.writeText(value);if(feedback)feedback.textContent="Copied: "+value;}
   catch(_error){if(feedback)feedback.textContent="Select and copy: "+value;}
  });
 });
});
