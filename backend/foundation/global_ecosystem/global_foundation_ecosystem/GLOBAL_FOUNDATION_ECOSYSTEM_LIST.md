# Global Foundation Ecosystem List

This is the canonical planned sub-ecosystem list for `backend/foundation/global_ecosystem/global_foundation_ecosystem/`.

Every item uses the exact naming pattern `global_<name>_ecosystem`. The same 14 ecosystem names and order are maintained in both Global Foundation and Global Infrastructure.

| # | Folder name | Responsibility |
|---:|---|---|
| 1 | `global_backup_ecosystem/` | Backup ecosystem |
| 2 | `global_rebackup_ecosystem/` | Re-backup / secondary backup ecosystem |
| 3 | `global_recovery_ecosystem/` | Recovery ecosystem |
| 4 | `global_rerecovery_ecosystem/` | Re-recovery / recovery validation ecosystem |
| 5 | `global_store_ecosystem/` | Store / repository ecosystem |
| 6 | `global_restore_ecosystem/` | Restore ecosystem |
| 7 | `global_database_ecosystem/` | Database ecosystem |
| 8 | `global_redatabase_ecosystem/` | Database re-initialization / reconfiguration ecosystem |
| 9 | `global_storage_ecosystem/` | Storage ecosystem |
| 10 | `global_restorage_ecosystem/` | Secondary / replicated storage ecosystem |
| 11 | `global_sync_ecosystem/` | Synchronization ecosystem |
| 12 | `global_resync_ecosystem/` | Re-synchronization / reconciliation ecosystem |
| 13 | `global_history_ecosystem/` | History / audit trail ecosystem |
| 14 | `global_rehistory_ecosystem/` | History replay / re-audit ecosystem |

## Structural rules

1. Create each folder only when its implementation is ready to be added; do not create empty folders just to make the list appear complete.
2. Each folder should use the existing project convention: `__init__.py` where it is a Python package, and `manager.py` as the primary manager entry point when applicable.
3. Keep the same folder names in both Global Foundation and Global Infrastructure; implementation details may differ according to each layer's responsibility.
4. Backup, recovery, restore, database, storage, synchronization, and history are separate responsibilities. Do not treat them as interchangeable modules.
5. Update this list whenever an ecosystem is added, renamed, moved, or retired. Update both lists in the same change.
6. Do not delete or rename existing modules automatically. First map existing code, imports, tests, and workflow references, then migrate with compatibility and tests.

## Existing repository note

The inspected Foundation ecosystem currently contains the `android/` directory and manager/connect files. The 14 entries above are the planned standard sub-ecosystems; they have not all been created.

This file is an inventory and naming contract; it does not claim that every listed folder has already been implemented.
