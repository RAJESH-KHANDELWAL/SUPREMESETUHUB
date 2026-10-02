/* =========================================================
   GITHUB HOME LOADER
   SUPREMESETUHUB
   ========================================================= */

(function () {

    "use strict";

    /* =========================================================
       GITHUB SOURCE
       ========================================================= */

    const GITHUB_HTML =
        "https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/index.html";

    const GITHUB_CSS =
        "https://raw.githubusercontent.com/RAJESH-KHANDELWAL/SUPREMESETUHUB/main/frontend/supreme/style.css";


    /* =========================================================
       LOAD GITHUB CSS
       ========================================================= */

    const styleId = "SUPREME-GITHUB-HOME-CSS";

    if (!document.getElementById(styleId)) {

        const link = document.createElement("link");

        link.id = styleId;
        link.rel = "stylesheet";
        link.type = "text/css";
        link.href = GITHUB_CSS;

        document.head.appendChild(link);
    }


    /* =========================================================
       LOAD GITHUB HTML
       ========================================================= */

    fetch(GITHUB_HTML, {
        method: "GET",
        cache: "no-cache"
    })

    .then(function (response) {

        if (!response.ok) {
            throw new Error(
                "GitHub Home Page Load Failed: " +
                response.status
            );
        }

        return response.text();
    })

    .then(function (html) {

        /*
         * Existing Hostinger Home page ke andar
         * GitHub ka HTML load hoga.
         */

        const target =
            document.getElementById("GITHUB-HOME-CONTENT");

        if (!target) {

            console.error(
                "GITHUB-HOME-CONTENT target nahi mila."
            );

            return;
        }

        target.innerHTML = html;

    })

    .catch(function (error) {

        console.error(
            "GitHub Home Loader Error:",
            error
        );

    });

})();
