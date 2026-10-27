# People Password Manager — Backend API

This is a user-facing API for signed-in SUPREMESETUHUB users. It is separate from the private SUPREME OWNER ADMIN and SUPREME OWNER ADMIN ECOSYSTEM password managers; it does not seed, import, or reference the owner's personal credentials.

## Security boundary

- Every vault endpoint requires the existing SUPREMESETUHUB Bearer sign-in session.
- Each vault is keyed by the authenticated user's internal user ID; callers cannot submit another user's ID.
- The server accepts only a structured `SUPREME-ENCRYPTED-VAULT` envelope using `PBKDF2-SHA256-600000` and `AES-256-GCM`.
- Server storage contains only the encrypted envelope. Encryption/decryption and vault passphrase handling belong in the client. Never send plaintext password entries to this API.
- There is no password discovery, password reset, OTP/CVV storage, or third-party automatic login.

## Endpoints

- `GET /api/v1/people-password-manager/status`
- `GET /api/v1/people-password-manager/platforms`
- `GET /api/v1/people-password-manager/vault`
- `PUT /api/v1/people-password-manager/vault` — save encrypted envelope
- `DELETE /api/v1/people-password-manager/vault` — delete the signed-in user's envelope

## Product catalog

The API lists these requested product categories: LinkSetu, WebSetu, CodeSetu, LinkHub, WebHub, CodeHub, WebPress, CodePress, and LinkPress. This catalog enables account categorization and future platform integration; listing a brand does not claim that its independent frontend, authentication, or automatic third-party integration is already deployed.

## Deployment note

The backend must be deployed with persistent database storage configured. The endpoints are committed to the repository; a successful live deployment and client integration must be verified separately.
