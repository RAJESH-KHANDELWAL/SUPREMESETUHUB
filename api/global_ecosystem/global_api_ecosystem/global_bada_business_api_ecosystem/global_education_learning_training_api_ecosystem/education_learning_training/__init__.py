"""Education, Learning & Training industry API domain package."""

INDUSTRY_ID = "education_learning_training"
INDUSTRY_NAME = "Education, Learning & Training"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import EducationLearningService

__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "EducationLearningService"]
