# GLOBAL BUSINESS COACH CONTACT SETUP

## Public business identity

- Brand: DR RAJESH KHANDELWAL IBC
- Role: GLOBAL BUSINESS COACH AND INDEPENDENT BUSINESS CONSULTANT
- Audience: BHARAT + GLOBAL WORLD
- Contact email: DRRAJESHKHANDELWALIBC@GMAIL.COM
- Website: https://drrajeshkhandelwalibc.com
- Requested consistent social handle: @DRRAJESHKHANDELWALIBC
- WhatsApp contact: https://wa.me/917611967229

## Services

- Global business coaching
- Independent business consulting
- Freelancing and work opportunities
- Business networking and collaboration
- WordPress and website development
- Affiliate marketing
- Startup and entrepreneurship guidance
- Digital marketing and SEO

## Public API

`GET /api/v1/global-business-coach/profile`

This endpoint is intentionally public and returns only business profile, intended contact channels, service scope, and social handle metadata. It must not return owner credentials, tokens, private account registries, or internal governance data.

The SUPREME OWNER ADMIN route remains owner-only:
`GET /api/v1/supreme-ecosystem/owner-admin/business-coach-profile`

## Free lead-intake workflow

1. Publish the public business profile on the website and social profiles.
2. Use a Google Form for inquiry intake. Suggested fields: name, email, country/time zone, service of interest, short project brief, budget range (optional), and permission to contact.
3. Link the form to a Google Sheet for a basic lead register. Restrict Sheet access to the owner; do not collect passwords, OTPs, bank details, or sensitive identity documents.
4. Put the verified form URL on the website and social bios. Configure the form confirmation message to say how soon a reply is normally expected.
5. Test one submission end-to-end: form submit, row appears in Sheet, email notification arrives, and owner can reply.
6. Keep email, WhatsApp, and website form delivery marked unverified until each is tested.

## Social handle limitation

The code registers `DRRAJESHKHANDELWALIBC` as the intended consistent username for Facebook, Instagram, LinkedIn, YouTube, X, Threads, and Telegram. It does not create, rename, claim, or edit third-party accounts. Check username availability and confirm the profile URL separately on each platform before publishing links.

## Deployment configuration

Set these in private deployment environment variables if overriding defaults:

- `GLOBAL_BUSINESS_COACH_EMAIL`
- `GLOBAL_BUSINESS_COACH_WEBSITE`
- `GLOBAL_BUSINESS_COACH_SOCIAL_USERNAME`
- `GLOBAL_BUSINESS_COACH_WHATSAPP_NUMBER`
- `GLOBAL_BUSINESS_COACH_WEBSITE_FORM_URL`

Do not commit secrets or paste credentials into chat. `GLOBAL_BUSINESS_COACH_WEBSITE_FORM_URL` should be set only after the actual Google Form or website contact form URL is known and tested.
