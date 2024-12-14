from schemas.doctor_schemas import ReadDoctor, WriteDoctor, UpdateDoctor
from services.fake_data import generate_id, doctors

def create_doctor(doctor: WriteDoctor):
    try:
        doctor_dict = dict(doctor)
        doctor_dict["id"] = generate_id(True)
        doctors.append(doctor_dict)
        print(doctor_dict)
        return doctor_dict
    except Exception as e:
        print(f"Error creating doctor: {e}")
        return None

def read_doctors():
    return doctors

def read_doctor(id: str):
    for doctor in doctors:
        if doctor["id"] == id:
            return doctor
    return None

def update_doctor(id: str, doctor_in: UpdateDoctor):
    doctor = read_doctor(id)
    if doctor:
        doctor= dict(doctor)
        doctor_dict = dict(doctor_in)
        try:
            for key, value in doctor_dict.items():
                if value:
                    doctor[key] = value
            return doctor
        except Exception as e:
            print(f"Error updating doctor: {e}")
            return None
    print("Doctor not found")
    return None

def delete_doctor(id: str):
    for i, doctor in enumerate(doctors):
        if doctor["id"] == id:
            return doctors.pop(i)
    return None