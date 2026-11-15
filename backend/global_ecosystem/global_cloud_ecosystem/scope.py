"""Cloud scope from local deployments to global infrastructure."""
CLOUD_SCOPES={
"bharat_india_cloud":("india_regions","indian_cloud_providers","data_residency","local_compliance"),
"asia_pacific_cloud":("south_asia","east_asia","southeast_asia","oceania"),
"europe_cloud":("eu_regions","uk_regions","sovereign_cloud","regional_storage"),
"americas_cloud":("north_america","south_america","regional_infrastructure"),
"middle_east_africa_cloud":("middle_east_regions","africa_regions","regional_data_centres"),
"global_world_cloud":("multi_region","multi_cloud","hybrid_cloud","edge_networks"),
"personal_cloud":("consumer_storage","device_backup","file_sync"),
"business_cloud":("enterprise_storage","business_continuity","managed_services"),
"advanced_cloud":("gpu_fabric","confidential_computing","distributed_storage","zero_trust"),
"supreme_cloud":("multi_cloud_control_plane","policy_orchestration","cross_cloud_observability","sovereign_workload_placement"),
}
__all__=["CLOUD_SCOPES"]
