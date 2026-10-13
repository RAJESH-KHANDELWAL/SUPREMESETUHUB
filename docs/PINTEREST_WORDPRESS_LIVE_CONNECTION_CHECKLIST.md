# Pinterest ↔ WordPress ↔ SUPREMESETUHUB Live Connection Checklist

**Owner:** DR RAJESH KHANDELWAL IBC  
**WordPress site:** https://rajeshkhandelwalofficial.com/  
**Repository:** RAJESH-KHANDELWAL/SUPREMESETUHUB

## Verified from repository/account screenshots shared by the owner
- `frontend/supreme/index.html` references the brand image:
  `https://rajeshkhandelwalofficial.com/wp-content/uploads/2026/03/DR-RAJESH-KHANDELWAL-IBC-K1-3.jpg`
- Pinterest settings show `rajeshkhandelwalofficial.com` with an **Unclaim** control, which indicates an existing claim; do not unclaim it as part of troubleshooting.
- Pinterest bulk-create page shows the RSS feed URL entered as `https://rajeshkhandelwalofficial.com/feed/`.
- A prior CSV upload failed. The initial generated CSV had empty media URL values; do not reuse that file.

## Current verification status
The GitHub HTML source proves that the image URL is referenced in the page source, but does not prove the image URL responds publicly with a valid image. The repository source also does not prove that Pinterest has accepted the RSS feed or published Pins. Verify both live endpoints and the Pinterest UI before marking these tasks complete.

## Manual live connection sequence
1. In a browser, open the RSS URL and confirm it returns a valid RSS 2.0 or RSS 1.0 XML feed, not an error page or unsupported feed format.
2. Open the image URL in a private/incognito browser window. Confirm it displays the image without login, cookies, or a redirect to an HTML page.
3. In Pinterest Business settings → Import content → Create Pins in bulk, keep the existing claimed domain intact. Use the RSS feed connection UI and select the intended board. Save, then check the displayed connection status and allow Pinterest's stated processing window.
4. Check Pinterest after processing for a created Pin, its image, title, source URL, and destination URL. If no Pin is created, use the Pinterest-provided error/report before changing URLs or adding code.
5. Do not upload a CSV until it matches Pinterest's current official sample/template exactly. Required media URL fields must be filled with public direct image/video URLs; never use blank placeholders or guessed asset paths.
6. If verification is genuinely needed, add the exact meta tag supplied by Pinterest to the WordPress site's `<head>` through a maintained site-level integration, or use the offered DNS/file method. Do not remove an existing claim or overwrite unrelated verification tags.
7. After RSS works, configure WooCommerce catalog only if Pinterest shows eligibility and the correct catalog onboarding path. Validate product image, product ID/SKU, price, currency, availability and landing URL before promotion.
8. Treat GitHub automation as a separate later phase. The repo can hold integration code/configuration and documentation, but GitHub alone does not grant access to Pinterest or Hostinger accounts. Any API automation needs authorized Pinterest API access, OAuth, server-side secrets, idempotency, retries, logs and owner approval.

## Acceptance checklist
- [ ] RSS endpoint returns valid supported XML publicly.
- [ ] Image URL returns the intended public image.
- [ ] Pinterest confirms the RSS connection.
- [ ] At least one RSS Pin is published and its destination works.
- [ ] CSV upload is tested only with Pinterest's current official schema and valid media URLs.
- [ ] Existing website claim remains intact.
- [ ] WordPress/WooCommerce catalog connection is approved and validated, if available.
- [ ] No API tokens, passwords or verification secrets are committed to GitHub.
- [ ] No live connection, publication, catalog approval or analytics result is marked complete without evidence.
