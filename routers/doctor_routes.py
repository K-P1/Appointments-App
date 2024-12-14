from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from services.doctor_crud import *
from fastapi.responses import JSONResponse

doctors_router = APIRouter()

def is_doctor(user_id: str = Query(..., description="The ID of the user making the request")):
    role = str(user_id).split('_')[0]
    if role != 'dr':
        raise HTTPException(status_code=403, detail="Unauthorized")

@doctors_router.get("/all")
async def read_doctors_endpoint():
    doctors= read_doctors()
    if doctors:
        return JSONResponse(status_code=200, content= doctors)
    raise HTTPException(status_code=404, detail="Doctors not found")

@doctors_router.get("/{id}")
async def read_doctor_endpoint(id: str):
    doctor= read_doctor(id)
    if doctor:
        return JSONResponse(status_code=200, content= doctor)
    raise HTTPException(status_code=404, detail="Doctor not found")

@doctors_router.post("/create")
async def create_doctor_endpoint(doctor: WriteDoctor):
    d = create_doctor(doctor)
    if d:
        return JSONResponse(status_code=201, content= d)
    raise HTTPException(status_code=400, detail="Error creating doctor")

@doctors_router.patch('/update/{id}')
async def update_doctor_endpoint(
    id: Annotated[str, Path(..., description="The ID of the doctor to update")],
    doctor: UpdateDoctor, 
    user_validation: Annotated[None, Depends(is_doctor)]):
    d = update_doctor(id, doctor)
    if d:
        return JSONResponse(status_code=200, content= d)
    raise HTTPException(status_code=404, detail="Doctor not found")

@doctors_router.delete('/delete/{id}')
async def delete_doctor_endpoint(
    id: Annotated[str, Path(..., description="The ID of the doctor to update")],
    user_validation: Annotated[None, Depends(is_doctor)]):
    d = delete_doctor(id)
    if d:
        return JSONResponse(status_code=200, content= d)
    raise HTTPException(status_code=404, detail="Doctor not found")