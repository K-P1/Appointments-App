from pydantic import BaseModel
from typing import Optional

class WriteDoctor(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class ReadDoctor(BaseModel):
    id: str
    name: str
    specialization: str
    phone: str
    is_available: bool = True

    class ConfigDict:
        from_attributes = True

class UpdateDoctor(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None
    is_available: Optional[bool] = True