"""Database migration planning metadata; no live schema changes are executed."""
def build_migration_plan(source_model: str, target_model: str):
    if not source_model.strip() or not target_model.strip():
        raise ValueError("source_model and target_model are required")
    return {"source_model":source_model,"target_model":target_model,"stages":["inventory","schema_mapping","data_profiling","compatibility_review","dry_run","validation","cutover_plan","rollback_plan"],"execution_status":"not_executed","requires_backup":True,"requires_owner_approval":True}
