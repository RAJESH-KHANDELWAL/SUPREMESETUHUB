# SUPREME WordPress Snippets Setup

This setup keeps the two frontends separate and does not touch `frontend/index.html` (LINKSETU).

## Source files and purpose

- Public SUPREME homepage: `frontend/supreme/index.html`, served by `/api/v1/frontend/supreme`.
- SUPREME ECOSYSTEM private owner dashboard: `frontend/supreme-ecosystem/index.html`, with `signin.html` and `signin.js` served through the owner-dashboard routes.
- LINKSETU homepage: `frontend/index.html` — leave unchanged.

## WordPress setup

The existing **SUPREMESETUHUB Connector** plugin now registers these shortcodes:

- `[supreme_main_home]` — embeds the public SUPREME homepage.
- `[supreme_owner_dashboard]` — embeds the private dashboard only for signed-in WordPress administrators. The dashboard also retains its own SUPREME ECOSYSTEM owner-token sign-in; WordPress administrator access alone does not authenticate the backend.

### Create the pages

1. In WordPress Admin, open **Pages → Add New**.
2. Create a page titled **SUPREME** and place only `[supreme_main_home]` in the content.
3. Create a separate page titled **SUPREME ECOSYSTEM** and place only `[supreme_owner_dashboard]` in the content. Keep this page private/restricted; do not add the shortcode to a public menu.
4. In **Settings → SUPREMESETUHUB**, confirm the backend URL is the working HTTPS API base and run **Test Backend Connection**.
5. Preview both pages on desktop and mobile before setting the SUPREME page as the WordPress homepage under **Settings → Reading**.

## Security and verification notes

- The owner dashboard shortcode denies visitors who are not WordPress administrators; its API calls still require the separate owner token.
- No public signup is added.
- GitHub changes do not automatically deploy the backend or install/update the WordPress plugin. Deploy the repository changes first, then update the plugin on WordPress.
- Test these endpoints after backend deployment:
  - `GET /api/v1/frontend/supreme`
  - `GET /api/v1/frontend/supreme-owner-dashboard/`
  - `GET /api/v1/frontend/supreme-owner-dashboard/signin.html`
  - `GET /api/v1/frontend/supreme-owner-dashboard/signin.js`
- Keep `frontend/index.html` untouched; it belongs to LINKSETU.
