import random
from enum import Enum

class MedicalCondition(Enum):
    DIABETES = "Diabetes"
    HYPERTENSION = "Hypertension"
    ASTHMA = "Asthma"
    COVID19 = "COVID-19"
    FLU = "Flu"

class Specialty(Enum):
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    GENERAL_PRACTICE = "General Practice"
    PEDIATRICS = "Pediatrics"

class MedicationType(Enum):
    ANTIBIOTIC = "Antibiotic"
    ANTIVIRAL = "Antiviral"
    ANALGESIC = "Analgesic"
    ANTI_INFLAMMATORY = "Anti-inflammatory"
    VACCINE = "Vaccine"


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

def generate_patients(num_patients):
    patients = []
    for i in range(1, num_patients + 1):
        name = f"Patient {i}"  
        medical_condition = random.choice(list(MedicalCondition)).value
        age = random.randint(1, 100)  
        patients.append(Patient(name, f"PAT{i}", medical_condition, age, i))
    return patients

def generate_doctors(num_doctors):
    doctors = []
    for i in range(1, num_doctors + 1):
        doctor_name = f"Doctor {i}" 
        specialty = random.choice(list(Specialty)).value
        doctors.append(Doctor(doctor_name, f"DOC{i}", specialty, i))
    return doctors


def generate_prescriptions(num_prescriptions):
    prescriptions = []
    for i in range(1, num_prescriptions + 1):
        medication_type = random.choice(list(MedicationType)).value
        dosage = f"{random.randint(50, 500)}mg"  
        prescriptions.append(Prescription(f"PRES{i}", medication_type, dosage, i))
    return prescriptions



class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = generate_doctors(5)
        self.prescriptions = []
        self.consultation_queue = []
        self.appointments = []
        
    def add_new_patient(self):
        num_patients = int(input("Enter the number of new patients to add: "))
        new_patients = generate_patients(num_patients)  # Use the existing function for generation
        print(num_patients, "New patients are added:")
        for patient in new_patients:
            self.patients[patient.patient_id] = patient
            print(
                f"Name: {patient.name}, ID: {patient.patient_id}, Condition: {patient.condition}, Age: {patient.age}")
            
    def update_patient_record(self):
        patient_id = input("Enter patient ID to update: ")
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            choice = int(input("Press 1 to update age, and 2 to update medical condition: "))
            if choice == 1:
                new_age = int(input("Enter new age: "))
                patient.age = new_age
                print(f"Patient {patient_id}'s age updated to {new_age}.")
            elif choice == 2:
                new_condition = input("Enter the new medical condition: ")
                patient.condition = new_condition
                print(f"Patient {patient_id}'s medical condition updated to {new_condition}.")
            else:
                print("Invalid choice.")
        else:
            print("Patient ID not found.")
    
    def remove_patient_record(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                return "The patient has been removed"
        return "Patient not found!"

    def schedule_appointment(self, patient_id, doctor_id, appointment_details):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                for doctor in self.doctors:
                    if doctor.doctor_id == doctor_id:
                        appointment = Appointment(patient, doctor, appointment_details)
                        self.appointments.append(appointment_details)
                        return "The appointment is scheduled"
                    else:
                        return "ERROR. Information missing"
                
    def add_to_consultation_queue(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.consultation_queue.append(patient)
                return "The patient is added to the consultation queue"
            else:
                return "ERROR. Patient not found"
    
    def process_consultation(self):
        if self.consultation_queue:
            patient = self.consultation_queue.pop(0)
            return f"Consultation processed for patient {patient.name}"
        else:
            return "No patients in the consultation queue"

    def issue_prescription(self):
        if self.consultation_queue:
            patient = self.consultation_queue[0]
            prescription = generate_prescriptions(1)[0]
            self.prescriptions.append(prescription)
            return f"Prescription issued for patient {patient.name}"
        else:
            return "No patients in the consultation queue"

    def exit_program(self):
        print("Exiting program...")
        exit()


# Example usage:
hospital = HospitalManagementSystem()
hospital.add_new_patient()
hospital.add_to_consultation_queue("PAT1")
print(hospital.process_consultation())
print(hospital.issue_prescription())
hospital.exit_program()
