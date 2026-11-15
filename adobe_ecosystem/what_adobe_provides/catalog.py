"""Machine-readable Adobe product-family catalogue. Descriptive metadata only."""
ADOBE_PRODUCT_FAMILIES = {
 "creative_cloud": {"name":"Creative Cloud","products":["Photoshop","Illustrator","Premiere Pro","After Effects","InDesign","Lightroom","Audition","Substance 3D","Bridge"]},
 "document_cloud": {"name":"Document Cloud","products":["Acrobat","Acrobat Reader","Acrobat Sign","Adobe Scan","PDF Services"]},
 "experience_cloud": {"name":"Experience Cloud","products":["Experience Manager Sites","Experience Manager Assets","Experience Manager Forms","Experience Manager Guides","Analytics","Customer Journey Analytics","Real-Time CDP","Journey Optimizer","Campaign","Target","Marketo Engage","Audience Manager"]},
 "firefly_ai": {"name":"Firefly and AI","products":["Adobe Firefly","Firefly Services","Firefly Custom Models","Firefly Enterprise"]},
 "express_design": {"name":"Express and Design","products":["Adobe Express"]},
 "video_collaboration": {"name":"Video and Collaboration","products":["Frame.io","Camera to Cloud"]},
 "work_management": {"name":"Work Management","products":["Adobe Workfront","Adobe Learning Manager"]},
 "commerce": {"name":"Commerce","products":["Adobe Commerce","Commerce Optimizer"]},
 "publishing_community": {"name":"Publishing and Community","products":["Adobe Fonts","Adobe Stock","Behance","Adobe Portfolio","Captivate","FrameMaker","RoboHelp","ColdFusion","Adobe Connect"]},
}
def list_adobe_product_families():
    return {key: {"name": value["name"], "products": list(value["products"])} for key, value in ADOBE_PRODUCT_FAMILIES.items()}
__all__ = ["ADOBE_PRODUCT_FAMILIES", "list_adobe_product_families"]
