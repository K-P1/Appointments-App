from fastapi import FastAPI
from routers import patient_routes, doctor_routes, appointment_routes

app = FastAPI()

app.include_router(patient_routes.patients_router, prefix="/patient", tags=["Patients"])
app.include_router(doctor_routes.doctors_router, prefix="/doctor", tags=["Doctors"])
app.include_router(appointment_routes.appointments_router, prefix="/appointment", tags=["Appointments"])