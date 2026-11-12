# GITHUB-SUPREME deployment notes

This directory is designed to be deployed unchanged to both domains:

- `rajeshkhandelwalofficial.com/public_html/GITHUB-SUPREME/`
- `drrajeshkhandelwalibc.com/public_html/GITHUB-SUPREME/`

## Current setup

- `index.php`: JSON status endpoint; reports counts and domain metadata only.
- `core/Registry.php`: reads and validates the JSON registry.
- `config/hosts.json`: five placeholder host records. Add confirmed hostnames and usernames later.
- `config/domains.json`: the two deployment destinations.
- `.htaccess`: disables directory listing and blocks direct access to registry JSON files.

## Security rules

- Do not commit database passwords, Hostinger API tokens, SSH/SFTP passwords, private keys, or other secrets.
- Keep deployment credentials in GitHub Actions Secrets or the hosting environment.
- Confirm each Hostinger hostname and username in hPanel before populating the five records.
- Do not enable live database connections until the actual host records and required permissions are verified.

This is an initial registry foundation, not a completed Hostinger deployment. No files have been uploaded to either hosting account by this GitHub change.
