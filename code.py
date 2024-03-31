

class Patient:
    def __init__(self, name, patient_id, medical_condition, age, id_num):
        self.name = name
        self.patient_id = patient_id
        self.condition = medical_condition
        self.age = age
        self.id = id_num

class Doctor:
    def __init__(self, doctor_name, doctor_id, specialty, id_num):
        self.doctor_name = doctor_name
        self.doctor_id = doctor_id
        self.specialty = specialty
        self.id = id_num

class Prescription:
    def __init__(self, prescription_id, medication_type, dosage, id_num):
        self.prescription_id = prescription_id
        self.medication_type = medication_type
        self.dosage = dosage
        self.id = id_num

