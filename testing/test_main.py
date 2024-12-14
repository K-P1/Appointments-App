from fastapi.testclient import TestClient
from main import app
from services.fake_data import patients, doctors

client = TestClient(app)
dr_id = [d["id"] for d in doctors if d["name"] == "Devon Taylor"][0]
pt_id = [p["id"] for p in patients if p["name"] == "Hector Harmon"][0]


#=======================================================
def test_get_patients():
    response = client.get("/patient/all")
    assert response.status_code == 200
    assert response.json() == patients

def test_get_patient():
    id = pt_id
    response = client.get(f"/patient/{id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Hector Harmon"

def test_create_patient():
    patient = {"name": "John Doe", "age": 30, "sex": "Male", "weight": 75, "height": 175, "phone": "123-456-7890"}
    response = client.post("/patient/create", json=patient)
    assert response.status_code == 201
    new_patient = response.json()
    print(new_patient)
    assert any(p["id"] == new_patient["id"] for p in patients)

def test_update_patient():
    patient = {"name": "Jane Doe", "age": 26, "sex": "female", "weight": 65, "height": 145}
    id = pt_id
    response = client.patch(f"/patient/update/{id}?user_id={id}", json=patient)
    assert response.status_code == 200
    updated_patient = response.json()
    assert updated_patient["name"] == "Jane Doe"

def test_delete_patient():
    id = pt_id
    response = client.delete(f"/patient/delete/{id}?user_id={id}")
    assert response.status_code == 200
#=======================================================


#=======================================================
def test_get_doctors():
    response = client.get("/doctor/all")
    assert response.status_code == 200
    assert response.json() == doctors

def test_get_doctor():
    id = dr_id
    response = client.get(f"/doctor/{id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Devon Taylor"

def test_create_doctor():
    doctor = {"name": "John Doe", "specialization": "Cardiology", "phone": "123-456-7890", "is_available": True}
    response = client.post("/doctor/create", json=doctor)
    assert response.status_code == 201
    new_doctor = response.json()
    print(new_doctor)
    assert any(p["id"] == new_doctor["id"] for p in doctors)

def test_update_doctor():
    doctor = {"name": "Jane Doe", "specialization": "Physician"}
    id = dr_id
    response = client.patch(f"/doctor/update/{id}?user_id={id}", json=doctor)
    assert response.status_code == 200
    updated_doctor = response.json()
    assert updated_doctor["name"] == "Jane Doe"

def test_delete_doctor():
    id = dr_id
    response = client.delete(f"/doctor/delete/{id}?user_id={id}")
    assert response.status_code == 200
#=======================================================


#=======================================================
def test_new_appointment():
    appointment= {"patient_id": pt_id, "doctor_id": dr_id}
    response = client.post("/appointment/new", json=appointment)
    assert response.status_code == 201
    new_appointment = response.json()
    print(new_appointment)
    assert new_appointment["status"] == "ongoing"
    assert new_appointment["patient_id"] == pt_id
    assert new_appointment["doctor_id"] == dr_id
    assert new_appointment["date"] != None
    
def test_cancel_appointment():
    id = "1"
    response = client.delete(f"/appointment/cancel/{id}")
    assert response.status_code == 200

def test_complete_appointment():
    id = "1"
    response = client.patch(f"/appointment/complete/{id}")
    assert response.status_code == 200
    updated_appointment = response.json()
    assert updated_appointment["status"] == "completed"

def test_check_appointment():
    id = "1"
    response = client.get(f"/appointment/check/{id}")
    assert response.status_code == 200
    appointment = response.json()
    assert appointment["status"] == "completed" or appointment["status"] == "ongoing"
    assert appointment["patient_id"] == pt_id
    assert appointment["doctor_id"] == dr_id
    assert appointment["date"] != None

def test_get_appointments():
    response = client.get("/appointment/all")
    assert response.status_code == 200
#=======================================================