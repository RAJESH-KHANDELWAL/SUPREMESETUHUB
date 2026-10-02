(function () {
    "use strict";

    const HTML_URL =
        "https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/index.html";

    const CSS_URL =
        "https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/style.css";

    const TARGET_ID = "GITHUB-HOME-CONTENT";


    /* =====================================================
       FIND WORDPRESS HOME CONTAINER
       ===================================================== */

    const target = document.getElementById(TARGET_ID);

    if (!target) {
        console.error(
            "GitHub Home Loader: #" + TARGET_ID + " nahi mila."
        );
        return;
    }


    /* =====================================================
       LOAD GITHUB CSS
       ===================================================== */

    if (!document.getElementById("SUPREME-GITHUB-CSS")) {

        const css = document.createElement("link");

        css.id = "SUPREME-GITHUB-CSS";
        css.rel = "stylesheet";
        css.type = "text/css";
        css.href = CSS_URL;

        document.head.appendChild(css);
    }


    /* =====================================================
       LOAD GITHUB HTML
       ===================================================== */

    fetch(HTML_URL, {
        method: "GET",
        cache: "no-cache"
    })

    .then(function (response) {

        if (!response.ok) {
            throw new Error(
                "GitHub HTML load failed: " + response.status
            );
        }

        return response.text();
    })

    .then(function (html) {

        /*
         * GitHub index.html me agar complete document
         * structure hai, to sirf BODY ka content nikalo.
         */

        const parser = new DOMParser();

        const doc = parser.parseFromString(
            html,
            "text/html"
        );

        target.innerHTML = doc.body
            ? doc.body.innerHTML
            : html;

    })

    .catch(function (error) {

        console.error(
            "GitHub Home Loader Error:",
            error
        );

    });

})();
