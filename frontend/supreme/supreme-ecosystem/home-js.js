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

/*
 * The SUPREME HOME can be embedded in WordPress on a different origin.
 * The parent cannot read this document's height directly, so report the
 * measured document height with postMessage. The message contains only a
 * numeric height; the WordPress parent validates the sender and origin.
 */
(() => {
  if (window.parent === window) return;

  let lastHeight = 0;
  let scheduled = false;

  const measureAndReport = () => {
    scheduled = false;
    const body = document.body;
    const html = document.documentElement;
    if (!body || !html) return;

    const height = Math.ceil(Math.max(
      body.scrollHeight,
      body.offsetHeight,
      html.clientHeight,
      html.scrollHeight,
      html.offsetHeight
    ));

    if (!Number.isFinite(height) || height < 1 || height === lastHeight) return;
    lastHeight = height;

    window.parent.postMessage({
      type: "SUPREME_HOME_HEIGHT",
      height
    }, "*");
  };

  const scheduleReport = () => {
    if (scheduled) return;
    scheduled = true;
    window.requestAnimationFrame(measureAndReport);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", scheduleReport, { once: true });
  } else {
    scheduleReport();
  }

  window.addEventListener("load", scheduleReport);
  window.addEventListener("resize", scheduleReport);

  if ("ResizeObserver" in window) {
    const observer = new ResizeObserver(scheduleReport);
    const observeContent = () => {
      if (document.documentElement) observer.observe(document.documentElement);
      if (document.body) observer.observe(document.body);
    };
    observeContent();
    document.addEventListener("DOMContentLoaded", observeContent, { once: true });
  }

  document.querySelectorAll("img").forEach((img) => {
    if (!img.complete) img.addEventListener("load", scheduleReport, { once: true });
    img.addEventListener("error", scheduleReport, { once: true });
  });

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(scheduleReport).catch(() => {});
  }
})();
