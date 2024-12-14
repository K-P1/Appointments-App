from fastapi import APIRouter, HTTPException
from services.appointment_crud import *
from fastapi.responses import JSONResponse

appointments_router = APIRouter()

@appointments_router.post("/new")
async def create_appointment_endpoint(appointment : WriteAppointment):
    a = create_appointment(appointment)
    if a:
        return JSONResponse(status_code=201, content=a)
    raise HTTPException(status_code=400, detail="Error creating appointment")

@appointments_router.delete("/cancel/{id}")
async def cancel_appointment_endpoint(id : str):
    a = cancel_appointment(id)
    if a:
        return JSONResponse(status_code=200, content=a)
    raise HTTPException(status_code=404, detail="Appointment not found")

@appointments_router.patch("/complete/{id}")
async def complete_appointment_endpoint(id : str):
    a = update_appointment_status(id, "completed")
    if a:
        return JSONResponse(status_code=200, content=a)
    raise HTTPException(status_code=404, detail="Appointment not found")

@appointments_router.get("/all")
async def read_all_appointments_endpoint():
    a = get_all_appointments()
    if a:
        return JSONResponse(status_code=200, content=a)
    raise HTTPException(status_code=404, detail="No appointments found")

@appointments_router.get("/check/{id}")
async def check_appointment_endpoint():
    a = check_appointment(id)
    if a:
        return JSONResponse(status_code=200, content=a)
    raise HTTPException(status_code=404, detail="Appointment not found")