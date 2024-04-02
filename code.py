import random
from enum import Enum
from collections import deque


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
        self.prescription_stack = deque()

    def pushPrescription(self, prescription):
        self.prescription_stack.append(prescription)

    def popPrescription(self):
        if self.prescription_stack:
            return self.prescription_stack.pop()
        else:
            return None


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
        self.consultation_queue = deque()
        self.appointments = []

    def add_new_patient(self, num_patients):
        new_patients = generate_patients(num_patients)
        print(f"{num_patients} New patients are added:")
        for patient in new_patients:
            self.patients[patient.patient_id] = patient
            print(f"Name: {patient.name}, ID: {patient.patient_id}, Condition: {patient.condition}, Age: {patient.age}")

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
        if patient_id in self.patients:
            del self.patients[patient_id]
            return "The patient has been removed"
        else:
            return "Patient not found!"

    def schedule_appointment(self, patient_id, doctor_id, appointment_details):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            for doctor in self.doctors:
                if doctor.doctor_id == doctor_id:
                    appointment = (patient, doctor, appointment_details)
                    self.appointments.append(appointment)
                    self.consultation_queue.append(patient)  # Add patient to consultation queue
                    return "The appointment is scheduled and patient is added to the consultation queue"
            return "Doctor not found"
        else:
            return "Patient not found"

    def process_consultation(self):
        if not self.consultation_queue:
            return "No patients in the consultation queue"

        processed_patients = []

        while self.consultation_queue:
            patient = self.consultation_queue.popleft()
            processed_patients.append(patient)

        self.processed_patients = processed_patients  # Store processed patients
        return "Consultations processed for: " + ", ".join([patient.name for patient in processed_patients])

    def print_consultation_queue(self):
        if self.consultation_queue:
            print("Order of patients in consultation queue:", ", ".join([patient.name for patient in self.consultation_queue]))
        else:
            print("Consultation queue is empty")

    def issue_prescription(self):
        if self.processed_patients:  # Check if there are processed patients
            prescriptions_issued = []

            for patient in self.processed_patients:
                prescription = generate_prescriptions(1)[0]
                patient.pushPrescription(prescription)
                prescriptions_issued.append(patient.name)

            self.processed_patients.clear()  # Clear the list after issuing prescriptions
            return "Prescriptions issued for: " + ", ".join(prescriptions_issued)
        else:
            return "No patients to issue prescriptions to"

    def search_patient(self):
        patient_id = input("Enter patient ID to search: ")
        if patient_id not in self.patients:
            print("Patient not found!")
            return

        # Assuming patient exists
        patient = self.patients[patient_id]
        print(f"\nSummary for {patient.name} (ID: {patient.patient_id}):")
        print(f"  Condition: {patient.condition}")
        print(f"  Age: {patient.age}")

        # Find the patient's appointment, if any
        appointment_found = False
        for appointment in self.appointments:
            if appointment[0].patient_id == patient_id:
                print(f"  Appointment with Dr. {appointment[1].doctor_name} on {appointment[2]}")
                appointment_found = True
                break
        if not appointment_found:
            print("  No appointment scheduled.")

        # Find the patient's prescription, if any
        prescription_found = False
        for prescription in patient.prescription_stack:
            print(f"  Prescription: {prescription.medication_type} ({prescription.dosage})")
            prescription_found = True
        if not prescription_found:
            print("  No prescription issued.")

    def exit_program(self):
        print("Exiting program...")
        exit()

    def test(self):
        num_patients = int(input("Enter the number of new patients to add: "))
        self.add_new_patient(num_patients)

        while True:
            print("\n--- Hospital Management System Menu ---")
            print("1. Update patient record")
            print("2. Remove patient record")
            print("3. Schedule an appointment")
            print("4. Process consultation")
            print("5. Search for a patient")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.update_patient_record()
            elif choice == "2":
                patient_id = input("Enter patient ID to remove: ")
                print(self.remove_patient_record(patient_id))
            elif choice == "3":
                patient_id = input("Enter patient ID: ")
                doctor_id = input("Enter doctor ID: ")
                appointment_details = input("Enter appointment details: ")
                print(self.schedule_appointment(patient_id, doctor_id, appointment_details))
            elif choice == "4":
                print(self.process_consultation())
                self.print_consultation_queue()
                issue_prescription = input("Issue prescription for all patients (y/n)? ")
                if issue_prescription.lower() == "y":
                    print(self.issue_prescription())
            elif choice == "5":
                self.search_patient()
            elif choice == "6":
                self.exit_program()
            else:
                print("Invalid choice. Please try again.")


system = HospitalManagementSystem()
system.test()
