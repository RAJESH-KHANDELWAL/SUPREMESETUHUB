"""Abstract storage operations contract; no Adobe HTTP client or OAuth code here."""
from abc import ABC,abstractmethod
from typing import Any
class AdobeStorageAdapterContract(ABC):
    @abstractmethod
    def health_check(self)->dict[str,Any]: raise NotImplementedError
    @abstractmethod
    def list_objects(self,*,parent_id:str|None=None,cursor:str|None=None)->dict[str,Any]: raise NotImplementedError
    @abstractmethod
    def get_object_metadata(self,object_id:str)->dict[str,Any]: raise NotImplementedError
    @abstractmethod
    def upload(self,*,source:Any,parent_id:str|None=None,metadata:dict|None=None)->dict[str,Any]: raise NotImplementedError
    @abstractmethod
    def download(self,object_id:str,*,destination:Any)->dict[str,Any]: raise NotImplementedError
    @abstractmethod
    def delete(self,object_id:str)->dict[str,Any]: raise NotImplementedError
