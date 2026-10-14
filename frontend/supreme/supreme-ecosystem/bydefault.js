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

// Shared owner / brand identity class registry for SUPREME ECOSYSTEM pages.
const SUPREME_ECOSYSTEM_DEFAULT_IDENTITY_CLASSES = Object.freeze([
  "HOME-DR-RAJESH-KHANDELWAL-IBC",
  "HOME-DRRAJESHKHANDELWALIBC",
  "HOME-DR-RAJESH-KHANDELWAL-IBC-OFFICIAL",
  "HOME-DRRAJESHKHANDELWALIBCOFFICIAL",
  "HOME-RAJESH-KHANDELWAL",
  "HOME-RAJESHKHANDELWAL",
  "HOME-RAJESH-KHANDELWAL-OFFICIAL",
  "HOME-RAJESHKHANDELWALOFFICIAL",
  "HOME-KHANDELWAL-GROUP-AND-COMPANY",
  "HOME-KHANDELWALGROUPANDCOMPANY",
  "HOME-KHANDELWAL-GROUP-AND-COMPANIES",
  "HOME-KHANDELWALGROUPANDCOMPANIES"
]);

// Make the same default class registry available to other frontend modules.
window.SUPREME_ECOSYSTEM_DEFAULTS = Object.freeze({
  ...(window.SUPREME_ECOSYSTEM_DEFAULTS || {}),
  identityClasses: SUPREME_ECOSYSTEM_DEFAULT_IDENTITY_CLASSES
});

// Mark matching top-level identity sections without changing their content or layout.
document.addEventListener("DOMContentLoaded", () => {
  const selector = SUPREME_ECOSYSTEM_DEFAULT_IDENTITY_CLASSES
    .map(className => `section.${className}`)
    .join(",");
  document.querySelectorAll(selector).forEach(section => {
    section.dataset.supremeIdentitySection = "true";
  });
});
