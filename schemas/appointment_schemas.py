from pydantic import BaseModel
from datetime import date as dt_date, time as dt_time, datetime
from typing import Optional

class WriteAppointment(BaseModel):
    patient_id: str
    doctor_id: str
    time: Optional[dt_time] = datetime.now().time()
    date: Optional[dt_date] = datetime.now().date()
    status: Optional[str] = "ongoing"

class UpdateAppointment(BaseModel):
    patient_id: Optional[str] = None
    doctor_id: Optional[str] = None
    time: Optional[dt_time] = datetime.now().time()
    date: Optional[dt_date] = datetime.now().date()
    status: Optional[str] = None

class ReadAppointment(BaseModel):
    id: str
    patient_id: str
    doctor_id: str
    time: Optional[dt_time] = datetime.now().time()
    date: Optional[dt_date] = datetime.now().date()
    status: str

    class ConfigDict:
        from_attributes = True