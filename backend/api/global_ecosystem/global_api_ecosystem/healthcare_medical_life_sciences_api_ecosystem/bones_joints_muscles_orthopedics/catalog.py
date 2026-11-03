"""Catalog metadata for Bones, Joints, Muscles & Orthopedics."""
CATEGORY_ID = "bones_joints_muscles_orthopedics"
CATEGORY_NAME = "Bones, Joints, Muscles & Orthopedics"
DESCRIPTION = "Skeletal, muscular, connective-tissue, joint, spine, trauma and orthopaedic health."
STATUS = "taxonomy_scaffold"

def get_metadata():
    return {"id": CATEGORY_ID, "name": CATEGORY_NAME, "description": DESCRIPTION, "status": STATUS}
