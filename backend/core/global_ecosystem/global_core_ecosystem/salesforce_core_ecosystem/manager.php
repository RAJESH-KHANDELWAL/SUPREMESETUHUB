<?php
/** Thin metadata facade; OAuth and Salesforce API transport are excluded. */
require_once __DIR__ . '/salesforce_php_core_ecosystem/SalesforceCoreContract.php';
class SalesforceCoreManager {
    public static function identity(): array { return SalesforceCoreContract::identity(); }
    public static function boundaries(): array { return SalesforceCoreContract::boundaries(); }
}
