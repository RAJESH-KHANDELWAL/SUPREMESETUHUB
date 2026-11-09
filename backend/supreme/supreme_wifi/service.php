<?php
/**
 * SUPREME Wi-Fi status contract.
 * Actual radio scanning is performed by the trusted local Python adapter.
 * This PHP layer intentionally does not inspect device secrets or Wi-Fi passwords.
 */
declare(strict_types=1);

function supreme_wifi_scan_contract(): array {
    return [
        'service' => 'SUPREME_WIFI',
        'status' => 'LOCAL_ADAPTER_REQUIRED',
        'fields' => ['ssid', 'authentication', 'encryption', 'signal_percent', 'free_open_network', 'internet_status'],
        'passwords_collected' => false,
        'auto_connect' => false,
        'note' => 'Open authentication may indicate no Wi-Fi password is required; internet access and safety are not guaranteed.',
    ];
}
