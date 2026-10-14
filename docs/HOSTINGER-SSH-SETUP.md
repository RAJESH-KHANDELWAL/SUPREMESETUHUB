# Hostinger SSH setup — SUPREME MUKTI MAHAL ECOSYSTEM

The SSH setup workflow was removed because a key pair generated on a temporary GitHub Actions runner is discarded when the job ends. Printing only the public key does not leave the matching private key available for the deployment secret.

## 1. Generate a deployment key on your own computer

In PowerShell, run:

```powershell
ssh-keygen -t ed25519 -C "github-actions-hostinger" -f "$HOME\.ssh\supreme_hostinger_deploy"
```

Use a passphrase only if your deployment method supports it non-interactively; otherwise follow your organization's approved key-management procedure. Do not commit either key file to this repository.

## 2. Add the public key to Hostinger

Display the public key:

```powershell
Get-Content "$HOME\.ssh\supreme_hostinger_deploy.pub"
```

Add that public key to the correct Hostinger account/server SSH authorized keys.

## 3. Add GitHub Actions secrets

In the repository, open **Settings → Secrets and variables → Actions → New repository secret** and add:

- `SSH_PRIVATE_KEY`: complete contents of `supreme_hostinger_deploy` (the private key; never share it publicly)
- `SSH_HOST`: Hostinger SSH hostname or IP
- `SSH_USER`: deployment SSH username
- `SSH_PORT`: SSH port provided by Hostinger

Under **Settings → Secrets and variables → Actions → Variables**, add:

- `HOSTINGER_REMOTE_PATH`: the exact target directory for the frontend deployment

Use the minimum-privilege deployment account and confirm the remote path before running the workflow.

## 4. VPS workflow configuration

For `.github/workflows/hostinger-vps.yml`, configure:

- Secret `HOSTINGER_API_KEY`
- Variable `HOSTINGER_VM_ID`

Do not run a deployment until the Hostinger credentials and target paths have been verified. A successful workflow file parse does not prove that the external deployment provider or credentials work.
