"use strict";


/* =========================================================
   THEME HUB CONFIGURATION
   ========================================================= */

const THEME_HUB_API =
    "/api/v1/theme-hub/themes";


/* =========================================================
   DOM ELEMENTS
   ========================================================= */

const searchInput =
    document.getElementById(
        "HOME-THEME-HUB-SEARCH-INPUT"
    );

const searchButton =
    document.getElementById(
        "HOME-THEME-HUB-SEARCH-BUTTON"
    );

const statusElement =
    document.getElementById(
        "HOME-THEME-HUB-STATUS"
    );

const themesContainer =
    document.getElementById(
        "HOME-THEME-HUB-THEMES"
    );


/* =========================================================
   LOAD THEMES
   ========================================================= */

async function loadThemes(search = "") {

    try {

        showLoading();

        let apiUrl = THEME_HUB_API;

        if (search.trim() !== "") {

            apiUrl +=
                "?search=" +
                encodeURIComponent(
                    search.trim()
                );
        }


        const response =
            await fetch(apiUrl, {
                method: "GET",
                headers: {
                    "Accept": "application/json"
                }
            });


        if (!response.ok) {

            throw new Error(
                "THEME_API_HTTP_" +
                response.status
            );
        }


        const data =
            await response.json();


        if (
            !data ||
            data.success !== true
        ) {

            throw new Error(
                "THEME_API_RESPONSE_INVALID"
            );
        }


        const themes =
            Array.isArray(data.themes)
                ? data.themes
                : [];


        renderThemes(themes);


        statusElement.textContent =
            `${themes.length} THEME${themes.length === 1 ? "" : "S"} FOUND`;


    } catch (error) {

        console.error(
            "THEME HUB ERROR:",
            error
        );

        showError();

    }

}


/* =========================================================
   LOADING STATE
   ========================================================= */

function showLoading() {

    statusElement.textContent =
        "⏳ LOADING THEMES...";

    themesContainer.innerHTML = "";

}


/* =========================================================
   ERROR STATE
   ========================================================= */

function showError() {

    statusElement.textContent =
        "❌ UNABLE TO LOAD THEMES";

    themesContainer.innerHTML = `

        <div class="HOME-THEME-HUB-EMPTY">

            <div class="HOME-THEME-HUB-EMPTY-TITLE">
                ❌ THEME DATA NOT AVAILABLE
            </div>

            <div class="HOME-THEME-HUB-EMPTY-TEXT">
                PLEASE TRY AGAIN OR SEARCH ANOTHER THEME
            </div>

        </div>

    `;

}


/* =========================================================
   EMPTY STATE
   ========================================================= */

function showEmpty() {

    themesContainer.innerHTML = `

        <div class="HOME-THEME-HUB-EMPTY">

            <div class="HOME-THEME-HUB-EMPTY-TITLE">
                🔍 NO THEMES FOUND
            </div>

            <div class="HOME-THEME-HUB-EMPTY-TEXT">
                TRY SEARCHING FOR ANOTHER WORDPRESS THEME
            </div>

        </div>

    `;

}


/* =========================================================
   RENDER THEMES
   ========================================================= */

function renderThemes(themes) {

    themesContainer.innerHTML = "";


    if (!themes.length) {

        showEmpty();

        return;
    }


    themes.forEach(
        (theme) => {

            const card =
                createThemeCard(theme);

            themesContainer.appendChild(
                card
            );

        }
    );

}


/* =========================================================
   CREATE THEME CARD
   ========================================================= */

function createThemeCard(theme) {

    const card =
        document.createElement("article");


    card.className =
        "HOME-THEME-HUB-THEME-CARD";


    const screenshot =
        theme.screenshot ||
        theme.screenshot_url ||
        "";


    const name =
        theme.name ||
        theme.title ||
        "WORDPRESS THEME";


    const version =
        theme.version ||
        "N/A";


    const author =
        theme.author ||
        "WORDPRESS.ORG";


    const description =
        cleanText(
            theme.description ||
            theme.short_description ||
            "NO DESCRIPTION AVAILABLE."
        );


    const previewUrl =
        theme.preview_url ||
        theme.preview ||
        theme.homepage ||
        "#";


    const downloadUrl =
        theme.download_url ||
        theme.download ||
        "#";


    card.innerHTML = `

        <div class="HOME-THEME-HUB-THEME-SCREENSHOT-WRAPPER">

            ${
                screenshot
                ?
                `
                <img
                    class="HOME-THEME-HUB-THEME-SCREENSHOT"
                    src="${escapeAttribute(screenshot)}"
                    alt="${escapeAttribute(name)}"
                    loading="lazy"
                    onerror="this.style.display='none';"
                >
                `
                :
                `
                <div
                    class="HOME-THEME-HUB-EMPTY"
                    style="height:100%; border:0; border-radius:0;"
                >
                    🖼️
                </div>
                `
            }

        </div>


        <div class="HOME-THEME-HUB-THEME-CONTENT">

            <h2 class="HOME-THEME-HUB-THEME-NAME">
                ${escapeHtml(name)}
            </h2>


            <div class="HOME-THEME-HUB-THEME-VERSION">
                VERSION ${escapeHtml(version)}
            </div>


            <div class="HOME-THEME-HUB-THEME-AUTHOR">
                👤 ${escapeHtml(author)}
            </div>


            <div class="HOME-THEME-HUB-THEME-DESCRIPTION">
                ${escapeHtml(
                    truncateText(
                        description,
                        240
                    )
                )}
            </div>


            <div class="HOME-THEME-HUB-THEME-ACTIONS">

                <a
                    class="HOME-THEME-HUB-PREVIEW-BUTTON"
                    href="${escapeAttribute(previewUrl)}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    👁️ PREVIEW
                </a>


                <a
                    class="HOME-THEME-HUB-DOWNLOAD-BUTTON"
                    href="${escapeAttribute(downloadUrl)}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    ⬇️ DOWNLOAD
                </a>

            </div>

        </div>

    `;


    return card;

}


/* =========================================================
   SEARCH
   ========================================================= */

function performSearch() {

    const search =
        searchInput
            ? searchInput.value.trim()
            : "";


    loadThemes(search);

}


/* =========================================================
   SEARCH BUTTON
   ========================================================= */

if (searchButton) {

    searchButton.addEventListener(
        "click",
        performSearch
    );

}


/* =========================================================
   ENTER KEY SEARCH
   ========================================================= */

if (searchInput) {

    searchInput.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Enter"
            ) {

                event.preventDefault();

                performSearch();

            }

        }
    );

}


/* =========================================================
   HTML ESCAPE
   ========================================================= */

function escapeHtml(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

}


/* =========================================================
   ATTRIBUTE ESCAPE
   ========================================================= */

function escapeAttribute(value) {

    return escapeHtml(
        value
    );

}


/* =========================================================
   CLEAN TEXT
   ========================================================= */

function cleanText(value) {

    const temporary =
        document.createElement("div");

    temporary.innerHTML =
        String(value);

    return temporary.textContent ||
        temporary.innerText ||
        "";

}


/* =========================================================
   TRUNCATE DESCRIPTION
   ========================================================= */

function truncateText(
    text,
    maxLength
) {

    const value =
        String(text).trim();


    if (
        value.length <= maxLength
    ) {

        return value;

    }


    return (
        value.substring(
            0,
            maxLength
        ).trim() +
        "..."
    );

}


/* =========================================================
   INITIAL LOAD
   ========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        loadThemes();

    }
);
