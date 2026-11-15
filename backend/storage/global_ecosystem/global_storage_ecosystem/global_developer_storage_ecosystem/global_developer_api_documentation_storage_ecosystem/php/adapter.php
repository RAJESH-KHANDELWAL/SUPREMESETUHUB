<?php
/** Metadata-only adapter. External operations remain disabled. */
if (!defined('ABSPATH')) { exit; }
final class Global_Developer_Storage_Category {
    public const CONNECTION_STATE = 'NOT_CONFIGURED';
    public const STORAGE_OPERATIONS_ENABLED = false;
}
