from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from services.patient_crud import *

patients_router = APIRouter()

# Dependency to validate the user making the request
def is_patient(user_id: str = Query(..., description="The ID of the user making the request")):
    role = str(user_id).split('_')[0]
    if role != 'pt':
        raise HTTPException(status_code=403, detail="Unauthorized")

@patients_router.get("/all")
async def read_patients_endpoint():
    patients = read_patients()
    if patients:
        return JSONResponse(status_code=200, content=patients)
    raise HTTPException(status_code=404, detail="Patients not found")

@patients_router.get("/{id}")
async def read_patient_endpoint(
    id: Annotated[str, Path(..., description="The ID of the patient to view")]
):
    patient = read_patient(id)
    if patient:
        return JSONResponse(status_code=200, content=patient)
    raise HTTPException(status_code=404, detail="Patient not found")

@patients_router.post("/create")
async def create_patient_endpoint(patient: WritePatient):
    p = create_patient(patient)
    if p:
        return JSONResponse(status_code=201, content=p)
    raise HTTPException(status_code=400, detail="Error creating patient")

@patients_router.patch("/update/{id}")
async def update_patient_endpoint(
    id: Annotated[str, Path(..., description="The ID of the patient to update")],
    patient: UpdatePatient,
    user_validation: Annotated[None, Depends(is_patient)]):
    p = update_patient(id, patient)
    if p:
        return JSONResponse(status_code=200, content=p)
    raise HTTPException(status_code=404, detail="Patient not found")

@patients_router.delete("/delete/{id}")
async def delete_patient_endpoint(
    id: Annotated[str, Path(..., description="The ID of the patient to delete")],
    user_validation: Annotated[None, Depends(is_patient)]):
    p = delete_patient(id)
    if p:
        return JSONResponse(status_code=200, content=p)
    raise HTTPException(status_code=404, detail="Patient not found")
