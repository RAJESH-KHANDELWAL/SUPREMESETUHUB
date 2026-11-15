"""Catalog of Adobe storage-oriented product packages."""
ADOBE_STORAGE_PRODUCTS = [
 {"id":"cloud_storage_and_collaboration","folder":"adobe_cloud_storage_and_collaboration_storage_ecosystem","product":"Creative Cloud collaboration and cloud assets","api_verification":"REQUIRED"},
 {"id":"creative_cloud_assets","folder":"adobe_creative_cloud_assets_storage_ecosystem","product":"Creative Cloud Assets","api_verification":"REQUIRED"},
 {"id":"creative_cloud","folder":"adobe_creative_cloud_storage_ecosystem","product":"Creative Cloud","api_verification":"REQUIRED"},
 {"id":"document_cloud","folder":"adobe_document_cloud_storage_ecosystem","product":"Document Cloud / Acrobat","api_verification":"REQUIRED"},
 {"id":"experience_manager_assets","folder":"adobe_experience_manager_assets_storage_ecosystem","product":"Experience Manager Assets","api_verification":"REQUIRED"},
 {"id":"express","folder":"adobe_express_storage_ecosystem","product":"Adobe Express","api_verification":"REQUIRED"},
 {"id":"frameio","folder":"adobe_frameio_storage_ecosystem","product":"Frame.io","api_verification":"REQUIRED"},
 {"id":"lightroom","folder":"adobe_lightroom_storage_ecosystem","product":"Lightroom","api_verification":"REQUIRED"},
 {"id":"workfront","folder":"adobe_workfront_storage_ecosystem","product":"Workfront","api_verification":"REQUIRED"},
]
def list_storage_products(): return [dict(item) for item in ADOBE_STORAGE_PRODUCTS]
