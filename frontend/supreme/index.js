(function () {
  "use strict";

  const HTML_URL = "https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/index.html";
  const TARGET_ID = "GITHUB-HOME-CONTENT";

  function executeInsertedScripts(target) {
    target.querySelectorAll("script").forEach(function (oldScript) {
      const script = document.createElement("script");
      Array.from(oldScript.attributes).forEach(function (attribute) {
        script.setAttribute(attribute.name, attribute.value);
      });
      script.textContent = oldScript.textContent;
      oldScript.replaceWith(script);
    });
  }

  function loadSupremeHome() {
    const target = document.getElementById(TARGET_ID);
    if (!target || target.dataset.supremeLoaded === "true") return;
    target.dataset.supremeLoaded = "loading";

    fetch(HTML_URL, { method: "GET", cache: "no-cache" })
      .then(function (response) {
        if (!response.ok) throw new Error("SUPREME homepage load failed: HTTP " + response.status);
        return response.text();
      })
      .then(function (html) {
        const doc = new DOMParser().parseFromString(html, "text/html");
        target.innerHTML = doc.body ? doc.body.innerHTML : html;
        executeInsertedScripts(target);
        target.dataset.supremeLoaded = "true";
      })
      .catch(function (error) {
        target.dataset.supremeLoaded = "error";
        console.error("SUPREME homepage loader:", error);
        target.innerHTML = '<p role="alert">SUPREME homepage could not load. Please refresh or try again later.</p>';
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadSupremeHome, { once: true });
  } else {
    loadSupremeHome();
  }
})();
