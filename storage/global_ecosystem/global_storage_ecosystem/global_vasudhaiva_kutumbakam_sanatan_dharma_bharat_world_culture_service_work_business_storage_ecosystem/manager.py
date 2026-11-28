"""File/object storage adapter boundary for culture-service-work-business assets."""
from __future__ import annotations
from typing import BinaryIO,Any
from backend.storage.filesystem import LocalFileStorage
class GlobalCultureServiceWorkBusinessStorage:
    AREA="culture-service-work-business"
    def __init__(self,storage:LocalFileStorage|None=None)->None:self.storage=storage or LocalFileStorage()
    def status(self)->dict[str,Any]:return {"area":self.AREA,**self.storage.health()}
    def store_asset(self,stream:BinaryIO,filename:str,max_bytes:int=25*1024*1024)->dict[str,Any]:
        if max_bytes<1:raise ValueError("MAX_BYTES_MUST_BE_POSITIVE")
        safe_name=str(filename or "asset.bin").replace("\\","/").split("/")[-1]
        content=stream.read(max_bytes+1)
        if not content:raise ValueError("EMPTY_ASSET")
        if len(content)>max_bytes:raise ValueError("ASSET_MAX_SIZE_EXCEEDED")
        key=self.storage.save_bytes(content,safe_name)
        return {"storage_key":key,"filename":safe_name,"area":self.AREA,"size_bytes":len(content),"backend":"LOCAL_FILESYSTEM"}
    def open_asset(self,storage_key:str):return self.storage.open_key(storage_key)
    def delete_asset(self,storage_key:str)->bool:return self.storage.delete_key(storage_key)
