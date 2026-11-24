<?php
/** Frontend/backend infrastructure contract checker; no frontend domain files or folders. */
final class FrontendGlobalInfrastructureEcosystemConnector {
    private const DOMAINS = ['backup','billing','cdn','containers','database','dns','domains','email','firewall','ftp','hosting','ipam','load_balancer','model','monitoring','network','object_storage','security','server','ssl','storage'];

    public function connect(): array {
        $frontend = __DIR__;
        $repository = dirname(dirname(dirname(dirname($frontend))));
        $backend = $repository . '/backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem';
        $backendEntry = $repository . '/backend/infrastructure/global_ecosystem';

        $backendDomains = [];
        foreach (self::DOMAINS as $domain) {
            $backendDomains[$domain] = is_dir($backend . '/' . $domain);
        }
        $frontendFiles = [];
        foreach (['__init__.py','manager.py','manager.php',
            'frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.py',
            'frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.php'] as $file) {
            $frontendFiles[$file] = is_file($frontend . '/' . $file);
        }
        $backendFiles = [];
        foreach (['__init__.py','manager.py','manager.php'] as $file) {
            $backendFiles[$file] = is_file($backend . '/' . $file);
        }
        $backendEntryFiles = [
            'global_ecosystem_manager.py' => is_file($backendEntry . '/manager.py'),
            'global_ecosystem_manager.php' => is_file($backendEntry . '/manager.php')
        ];
        $domainFiles = array_filter(self::DOMAINS, static fn($name) => is_file($frontend . '/' . $name . '.py'));
        $domainFolders = array_filter(self::DOMAINS, static fn($name) => is_dir($frontend . '/' . $name));

        $frontendHealthy = !in_array(false, $frontendFiles, true)
            && count($domainFiles) === 0 && count($domainFolders) === 0;
        $backendHealthy = !in_array(false, $backendDomains, true)
            && !in_array(false, $backendFiles, true)
            && !in_array(false, $backendEntryFiles, true);

        return [
            'name' => 'FRONTEND-BACKEND GLOBAL INFRASTRUCTURE CONNECTOR',
            'frontend' => ['healthy' => $frontendHealthy, 'file_checks' => $frontendFiles,
                'domain_file_count' => count($domainFiles), 'domain_folder_count' => count($domainFolders)],
            'backend' => ['healthy' => $backendHealthy, 'domain_checks' => $backendDomains,
                'file_checks' => $backendFiles, 'entry_checks' => $backendEntryFiles,
                'expected_domain_count' => count(self::DOMAINS),
                'present_domain_count' => count(array_filter($backendDomains))],
            'connected' => $frontendHealthy && $backendHealthy,
            'connection_type' => 'repository structure and contract validation; no external provider operations'
        ];
    }
}
