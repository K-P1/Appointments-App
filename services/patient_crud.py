from schemas.patient_schemas import ReadPatient, WritePatient, UpdatePatient
from services.fake_data import generate_id, patients

def create_patient(patient: WritePatient):
    try:
        patient_dict = dict(patient)
        patient_dict["id"] = generate_id(False)
        patients.append(patient_dict)
        return patient_dict
    except Exception as e:
        #print(f"Error creating patient: {e}")
        return None

def read_patients():
    return patients

def read_patient(id: str):
    for patient in patients:
        if patient["id"] == id:
            return patient
    return None

def update_patient(id: str, patient_in: UpdatePatient):
    patient = read_patient(id)
    if patient:
        patient= dict(patient)
        patient_dict = dict(patient_in)
        try:
            for key, value in patient_dict.items():
                if value:
                    patient[key] = value
            return patient
        except Exception as e:
            #print(f"Error updating patient: {e}")
            return None
    #print("Patient not found")
    return None

def delete_patient(id: str):
    for i, patient in enumerate(patients):
        if patient["id"] == id:
            return patients.pop(i)
    return None