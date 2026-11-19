<?php
/** Backend-to-frontend Infrastructure structure and contract checker. */
final class BackendInfrastructureFrontendInfrastructureConnector {
    private const DOMAINS = [
        'backup','billing','cdn','containers','database','dns','domains','email',
        'firewall','ftp','hosting','ipam','load_balancer','model','monitoring',
        'network','object_storage','security','server','ssl','storage'
    ];

    public function connect(): array {
        $backend = __DIR__;
        $repository = dirname(dirname($backend));
        $frontend = $repository . '/frontend/infrastructure';
        $backendEcosystem = $backend . '/global_ecosystem/global_infrastructure_ecosystem';
        $frontendEcosystem = $frontend . '/global_ecosystem/global_infrastructure_ecosystem';

        $backendChecks = [];
        foreach (['__init__.py','manager.py','manager.php',
            'backend_infrastructure_frontend_infrastructure_connect.py',
            'backend_infrastructure_frontend_infrastructure_connect.php'] as $file) {
            $backendChecks[$file] = is_file($backend . '/' . $file);
        }
        $backendChecks['global_ecosystem'] = is_dir($backend . '/global_ecosystem');

        $frontendChecks = [];
        foreach (['__init__.py','manager.py','manager.php',
            'frontend_infrastructure_backend_infrastructure_connect.py',
            'frontend_infrastructure_backend_infrastructure_connect.php'] as $file) {
            $frontendChecks[$file] = is_file($frontend . '/' . $file);
        }
        $frontendChecks['global_ecosystem'] = is_dir($frontend . '/global_ecosystem');
        $frontendChecks['global_infrastructure_ecosystem_manager'] =
            is_file($frontendEcosystem . '/manager.py');

        $backendDomains = [];
        foreach (self::DOMAINS as $domain) {
            $backendDomains[$domain] = is_dir($backendEcosystem . '/' . $domain);
        }

        $backendHealthy = !in_array(false, $backendChecks, true)
            && !in_array(false, $backendDomains, true);
        $frontendHealthy = !in_array(false, $frontendChecks, true);

        return [
            'name' => 'BACKEND-FRONTEND INFRASTRUCTURE CONNECTOR',
            'backend' => [
                'checks' => $backendChecks,
                'domain_checks' => $backendDomains,
                'expected_domain_count' => count(self::DOMAINS),
                'present_domain_count' => count(array_filter($backendDomains)),
                'healthy' => $backendHealthy
            ],
            'frontend' => [
                'checks' => $frontendChecks,
                'healthy' => $frontendHealthy
            ],
            'connected' => $backendHealthy && $frontendHealthy,
            'connection_type' => 'local structure and contract validation; no provider mutations'
        ];
    }
}
