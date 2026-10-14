"use strict";
const SUPREME_ECOSYSTEM_API = "https://supremesetuhub-3v4e.onrender.com";
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-current-year]").forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });
  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const value = button.getAttribute("data-copy") || "";
      const feedback = document.getElementById("copy-feedback");
      try {
        if (!navigator.clipboard || !window.isSecureContext) throw new Error("Clipboard unavailable");
        await navigator.clipboard.writeText(value);
        if (feedback) feedback.textContent = "Copied: " + value;
      } catch (_error) {
        if (feedback) feedback.textContent = "Select and copy: " + value;
      }
    });
  });
});
