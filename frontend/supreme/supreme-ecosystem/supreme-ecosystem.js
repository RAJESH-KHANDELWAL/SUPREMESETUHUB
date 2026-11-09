"use strict";

document.addEventListener("DOMContentLoaded", () => {
  const feedback = document.getElementById("copy-feedback");
  const copyButtons = document.querySelectorAll("[data-copy]");

  copyButtons.forEach((button) => {
    button.addEventListener("click", async () => {
      const value = button.getAttribute("data-copy") || "";
      try {
        if (!navigator.clipboard || !window.isSecureContext) {
          throw new Error("Clipboard API unavailable");
        }
        await navigator.clipboard.writeText(value);
        if (feedback) feedback.textContent = `Copied route: ${value}`;
      } catch (_error) {
        if (feedback) feedback.textContent = `Route: ${value} — select and copy it manually.`;
      }
    });
  });
});
