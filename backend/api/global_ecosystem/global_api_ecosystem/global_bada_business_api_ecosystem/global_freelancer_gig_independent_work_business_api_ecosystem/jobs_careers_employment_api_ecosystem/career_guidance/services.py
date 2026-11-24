"""Career Guidance taxonomy services."""
from .categories import CATEGORY_ID,CATEGORY_NAME,list_tracks,get_track,search_tracks,validate_tracks
def get_status(): return {"success":True,"category_id":CATEGORY_ID,"category_name":CATEGORY_NAME,"taxonomy_status":"taxonomy_only","live_vacancies_available":False,"is_vacancy_category":False,**validate_tracks()}
