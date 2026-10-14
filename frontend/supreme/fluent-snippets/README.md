# SUPREME HOME — GitHub snippet system

**WordPress is not modified by this repository setup.** This directory stores the separated GitHub-side implementation for the SUPREME homepage, so the system can be maintained from GitHub.

## The three snippet files

1. `home-html.html` — HTML/PHP Content container used by the Fluent Snippets shortcode.
2. `home-css.css` — CSS entry point importing the canonical SUPREME stylesheet.
3. `home-js.js` — JavaScript loader that fetches the canonical SUPREME homepage HTML and inserts it into `#GITHUB-HOME-CONTENT`.

These files are intentionally separated so the HTML, CSS, and JavaScript can be maintained independently in GitHub.

## Canonical SUPREME source

- Homepage content: `frontend/supreme/index.html`
- Homepage CSS: `frontend/supreme/style.css`
- Loader reference: `frontend/supreme/index.js`

## Relationship to the current WordPress snippets

The WordPress export currently identifies these snippets:

- `4-f09f8fa1-home-f09f8fa1.php` — `🏡 HOME 🏡 HTML`, configured for shortcode output. Its current code includes a Render fetch and uses `SUPREMESETUHUB-HOME`.
- `5-f09f8fa1-home-f09f8fa1.php` — `🏡 HOME 🏡 CSS`, configured to run everywhere.
- `3-f09f9191-drrajeshkhandelwalibc-f09f9191-js.php` — the global brand-identity JavaScript snippet, configured for `admin_head`; it is **not** a dedicated homepage loader.

The GitHub files above represent the separated GitHub-maintained homepage implementation; they are not a claim that the older WordPress snippets have already been replaced. The live WordPress snippets remain unchanged unless you separately choose to edit them in WordPress.

## Keep the projects separate

- `frontend/supreme/` is the SUPREME website homepage.
- `frontend/index.html` is the LINKSETU social hub (Facebook, Instagram, WhatsApp, LinkedIn, and X).
- Do not merge LINKSETU's page with the SUPREME homepage.
