document.addEventListener("DOMContentLoaded", () => {
  const feedback = document.getElementById("copy-feedback");
  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const value = button.getAttribute("data-copy") || "";
      try {
        await navigator.clipboard.writeText(value);
        if (feedback) feedback.textContent = "Copied: " + value;
      } catch (error) {
        if (feedback) feedback.textContent = "Copy unavailable. Select and copy: " + value;
      }
    });
  });
});
