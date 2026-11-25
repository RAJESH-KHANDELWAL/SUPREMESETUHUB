# Folder and File Mirror Policy

This policy applies to every new folder and file created in the backend ecosystem.

## 1. Required mirror locations

For every source folder or file created under the backend project, maintain two corresponding mirrors:

- Workflow mirror root: `backend/workflow/`
- Test mirror root: `backend/test/`

Keep the same relative directory structure beneath the appropriate mirror root.

## 2. Naming rule

Use the original folder or file name unchanged, with exactly one prefix added at the beginning:

- Workflow mirror: `workflow_<original-name>`
- Test mirror: `test_<original-name>`

Examples:

| Original | Workflow mirror | Test mirror |
|---|---|---|
| `global_ecosystem/` | `workflow_global_ecosystem/` | `test_global_ecosystem/` |
| `manager.py` | `workflow_manager.py` | `test_manager.py` |
| `global_ai_core/` | `workflow_global_ai_core/` | `test_global_ai_core/` |
| `engine.py` | `workflow_engine.py` | `test_engine.py` |

Do not change, abbreviate, translate, or otherwise alter the original name. Preserve file extensions.

## 3. Create, rename, and delete synchronization

- When a source folder or file is added, create its matching workflow and test mirrors using the naming rule above.
- When a source folder or file is renamed or moved, rename or move both corresponding mirrors to match.
- When a source folder or file is deleted, delete both corresponding mirrors as well.
- Apply these operations to the complete affected folder tree, not just its top-level entry.
- Never delete unrelated workflow or test content. Confirm the source-to-mirror mapping before deletion.

## 4. Scope and exclusions

- Do not create mirrors recursively for content already inside `backend/workflow/` or `backend/test/`.
- Keep GitHub Actions workflow definition YAML files in the repository-root `.github/workflows/` directory so GitHub can discover and run them. Backend workflow implementation files belong under `backend/workflow/`.
- A mirror must contain the appropriate workflow implementation or test content; do not create empty placeholder copies merely to satisfy naming.

## 5. Enforcement

This document defines the required convention. It does not itself perform file operations. A sync/check automation must enforce the create, rename/move, and delete rules, and must be tested before the repository treats synchronization as automatic.

The same policy must be kept in both the workflow and test mirror roots. Update both copies together whenever this policy changes.
