from pydantic import BaseModel
from typing import Optional

class WritePatient(BaseModel):
    name: str
    age: int
    sex: str
    weight: int
    height: int
    phone: str

class UpdatePatient(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    weight: Optional[int] = None
    height: Optional[int] = None
    phone: Optional[str] = None
    
class ReadPatient(BaseModel):
    id: str 
    name: str
    age: int
    sex: str
    weight: int
    height: int
    phone: str

    class ConfigDict:
        from_attributes = True
