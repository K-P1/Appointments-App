from faker import Faker
import random
import uuid

fake= Faker()

patients = [
    {'id': 'pt_9767', 'name': 'Brent Bauer', 'age': 39, 'sex': 'Female', 'weight': 136, 'height': 198, 'phone': '785-906-8967x7186'}, 
    {'id': 'pt_e127', 'name': 'Martin Morris', 'age': 80, 'sex': 'Male', 'weight': 80, 'height': 181, 'phone': '669.351.0259'}, 
    {'id': 'pt_3475', 'name': 'Kenneth Santiago', 'age': 45, 'sex': 'Female', 'weight': 175, 'height': 163, 'phone': '813-962-2215x090'}, 
    {'id': 'pt_8f90', 'name': 'Hector Harmon', 'age': 63, 'sex': 'Female', 'weight': 55, 'height': 161, 'phone': '523.825.6764'}, 
    {'id': 'pt_936d', 'name': 'Brianna Mccormick', 'age': 51, 'sex': 'Male', 'weight': 139, 'height': 178, 'phone': '447-247-4717'}]

doctors = [
    {'id': 'dr_396f', 'name': 'Judy Jones', 'specialization': 'Pediatrics', 'phone': '001-463-653-1625x98117', 'is_available': True}, 
    {'id': 'dr_8bf8', 'name': 'Devon Taylor', 'specialization': 'Cardiology', 'phone': '881.456.0971x94441', 'is_available': True}, 
    {'id': 'dr_fcf9', 'name': 'Katie Carpenter', 'specialization': 'Cardiology', 'phone': '950-272-9165x187', 'is_available': True}]

specializations = ["Cardiology", "Neurology", "Pediatrics", "Orthopedics", "Dermatology"]
sexes = ["Male", "Female"]
    
def generate_id(is_dr):
    if is_dr:
        return 'dr_' + str(uuid.uuid4())[:4]
    return 'pt_' + str(uuid.uuid4())[:4]

def generate_patients(number):
    patients = []
    for _ in range(number):
        patient = {
            "id": generate_id(4),
            "name": fake.name(),
            "age": random.randint(10, 90),
            "sex": random.choice(sexes),
            "weight": random.randint(50, 200),
            "height": random.randint(120, 200),
            "phone": fake.phone_number()
        }
        patients.append(patient)
    return patients

def generate_doctors(number):
    doctors = []
    for _ in range(number):
        doctor = {
            "id": generate_id(4),
            "name": fake.name(),
            "specialization": random.choice(specializations),
            "phone": fake.phone_number(),
            "is_available": True
        }
        doctors.append(doctor)
    return doctors

# patients.extend(generate_patients(5))
# doctors.extend(generate_doctors(3))
# print(patients)
# print(doctors)