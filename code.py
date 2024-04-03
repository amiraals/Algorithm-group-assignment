import random
from enum import Enum
from collections import deque
import datetime


# Defining Enums for various medical conditions that patients may have.
class MedicalCondition(Enum):
    DIABETES = "Diabetes"
    HYPERTENSION = "Hypertension"
    ASTHMA = "Asthma"
    COVID19 = "COVID-19"
    FLU = "Flu"

# Defining Enums for doctor specialties to categorize doctors based on their field of expertise.
class Specialty(Enum):
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    GENERAL_PRACTICE = "General Practice"
    PEDIATRICS = "Pediatrics"

# Defining Enums for types of medications that might be prescribed to patients.
class MedicationType(Enum):
    ANTIBIOTIC = "Antibiotic"
    ANTIVIRAL = "Antiviral"
    ANALGESIC = "Analgesic"
    ANTI_INFLAMMATORY = "Anti-inflammatory"
    VACCINE = "Vaccine"


class Patient:
    """
    Class to represent a Patient
    """
    def __init__(self, name, patient_id, medical_condition, age, id_num): # Initiating a constructor for the Patient class
        # Constructor for Patient class
        self.name = name
        self.patient_id = patient_id
        self.condition = medical_condition
        self.age = age
        self.id = id_num
        self.prescription_stack = deque()  # Initialize prescription stack for the patient

    def pushPrescription(self, prescription):
        # Method to push a prescription onto the patient's prescription stack
        self.prescription_stack.append(prescription)

    def popPrescription(self):
        # Method to pop a prescription from the patient's prescription stack
        if self.prescription_stack:
            return self.prescription_stack.pop()
        else:
            return None


class Doctor:
    """
    Class to represent a Doctor
    """
    def __init__(self, doctor_name, doctor_id, specialty, id_num):
        # Constructor for Doctor class
        self.doctor_name = doctor_name
        self.doctor_id = doctor_id
        self.specialty = specialty
        self.id = id_num


class Prescription:
    """
    Class to represent a Prescription
    """
    def __init__(self, prescription_id, medication_type, dosage, id_num):
        # Constructor for Prescription class
        self.prescription_id = prescription_id
        self.medication_type = medication_type
        self.dosage = dosage
        self.id = id_num


def generate_patients(num_patients):
    # Generating a list of random patients
    patients = []  # Initializing an empty list to hold the patient objects
    for i in range(1, num_patients + 1):
        # Looping through the specified number of times to create patient objects
        name = f"Patient {i}"
        medical_condition = random.choice(list(MedicalCondition)).value
        age = random.randint(1, 100)
        patients.append(Patient(name, f"P{i}", medical_condition, age, i))
    return patients


def generate_doctors(num_doctors):
    # Generating a list of random doctors on a specified number
    doctors = []
    for i in range(1, num_doctors + 1):
        # Looping through the specified number of times to create doctor objects
        doctor_name = f"Doctor {i}"
        specialty = random.choice(list(Specialty)).value
        doctors.append(Doctor(doctor_name, f"DOC{i}", specialty, i))
    return doctors


def generate_prescriptions(num_prescriptions):
    # Generating a list of random prescriptions
    prescriptions = []
    for i in range(1, num_prescriptions + 1):
        # Looping through the specified number of times to create prescription objects
        medication_type = random.choice(list(MedicationType)).value
        dosage = f"{random.randint(50, 500)}mg"
        prescriptions.append(Prescription(f"PRES{i}", medication_type, dosage, i))
    return prescriptions


class HospitalManagementSystem:
    def __init__(self):
        # Constructor for HospitalManagementSystem class
        self.patients = {}  # Dictionary to store patients
        self.doctors = generate_doctors(5)  # Generating a list of 5 doctors
        self.prescriptions = []  # List to store prescriptions
        self.consultation_queue = deque()  # Queue to manage consultation order
        self.appointments = []  # List to store appointments

    def add_new_patient(self, num_patients):
        # Function to add new patients to the system
        new_patients = generate_patients(num_patients)  # Generating a list of new patient objects
        for patient in new_patients:
            self.patients[patient.patient_id] = patient  # Adding each new patient to the dictionary

    def update_patient_record(self):
        # Function to update patient's record
        patient_id = input("Enter patient ID to update: ")
        if patient_id in self.patients:
            # If the patient exists, proceed with the update
            patient = self.patients[patient_id]  # Accessing the patient object
            choice = int(input("Press 1 to update age, and 2 to update medical condition: "))
            if choice == 1:
                # If choice is 1, update the patient's age
                new_age = int(input("Enter new age: "))
                patient.age = new_age
                print(f"Patient {patient_id}'s age updated to {new_age}.")
            elif choice == 2:
                # If choice is 2, update the patient's medical condition
                new_condition = input("Enter the new medical condition: ")
                patient.condition = new_condition
                print(f"Patient {patient_id}'s medical condition updated to {new_condition}.")
            else:
                print("Invalid choice.")

            # Printing the updated patient details
            print(f"\nUpdated Patient Details:")
            print(f"Name: {patient.name}")
            print(f"ID: {patient.patient_id}")
            print(f"Condition: {patient.condition}")
            print(f"Age: {patient.age}")
        else:
            print("Patient ID not found.")

    def remove_patient_record(self, patient_id):
        # Function to remove a patient's record
        if patient_id in self.patients:
            del self.patients[patient_id] # This removes the patients record from the dictionary
            return "The patient has been removed"
        else:
            return "Patient not found!"

    def list_doctors(self):
        # Function to display all available doctors in the system
        print("Available doctors:")
        for doctor in self.doctors:
            print(f"Doctor Name: {doctor.doctor_name}, ID: {doctor.doctor_id}, Specialty: {doctor.specialty}")

    def schedule_appointment(self):
        choice = input(
            "Enter 1 to schedule an appointment for a patient manually, or 2 to randomly schedule appointments: ")

        if choice == "1":
            # Manual appointment scheduling
            patient_id = input("Enter patient ID to schedule an appointment: ")
            success_message, success = self.schedule_for_patient(patient_id, choose_doctor_manually=True)   # Call the method to schedule an appointment for a specific patient by manually choosing a doctor.
            if success:
                print(success_message)  # Print only the message without the True flag
            else:
                print(success_message)

        elif choice == "2":
            # Random appointment scheduling
            while True:
                    num_appointments = int(input("How many appointments do you want to schedule randomly? "))
                    patient_ids = list(self.patients.keys())  # Getting a list of patient IDs
                    if num_appointments > len(patient_ids):
                        # if requested number of appointments exceeds available patients
                        print(
                            f"The number of appointments exceeds the total number of patients ({len(patient_ids)}). Please try a smaller number or type 'exit' to go back.")
                        continue_or_exit = input("Enter 'r' to try again or 'e' to go back): ")
                        if continue_or_exit.lower() == 'e':
                            break  # Exit the scheduling process

                    else:
                        for _ in range(num_appointments):
                            # Scheduling each appointment randomly
                            patient_id = random.choice(patient_ids)
                            success_message, _ = self.schedule_for_patient(patient_id, choose_doctor_manually=False)
                            print(success_message)
                            patient_ids.remove( patient_id)  # Avoiding scheduling multiple appointments for the same patient
                        break
        else:
            print("Invalid choice.")

    def schedule_for_patient(self, patient_id, choose_doctor_manually=True):
        # Function to schedule an appointment for a given patient, either choosing a doctor manually or randomly

        if patient_id not in self.patients:
            return "Patient not found"

        patient = self.patients[patient_id]  # Getting the patient object

        if choose_doctor_manually:
            # If choosing a doctor manually, list available doctors and ask for a doctor ID
            self.list_doctors()
            doctor_id = input("Enter doctor ID for the appointment: ")
            doctor_found = None
            for doctor in self.doctors:
                if doctor.doctor_id == doctor_id:
                    doctor_found = doctor
                    break
        else:
            # If choosing a doctor randomly, select a random doctor from the list
            doctor_found = random.choice(self.doctors)

        if doctor_found:
            # If a doctor was found, schedule the appointment

            today = datetime.date.today()
            future = today + datetime.timedelta(days=random.randint(1, 365))
            appointment_date = future.strftime("%Y-%m-%d")

            appointment_details = "General Checkup"  # Assuming general checkup, modify as needed.
            appointment = (patient, doctor_found, appointment_date, appointment_details)
            self.appointments.append(appointment)  # Adding the appointment to the list
            self.consultation_queue.append(patient)  # Adding the patient to the consultation queue
            return f"{patient.name}, has successfully entered the consultation queue. The appointment is scheduled for {patient.name} with {doctor_found.doctor_name} for {appointment_date}", True

        return "Doctor not found", False


    def process_consultation(self):
        # Process consultations in the consultation queue
        if not self.consultation_queue:   # Checking if the consultation queue is empty
            return "No patients in the consultation queue"
        processed_patients = []  # Initializing a list to keep track of processed patients

        while self.consultation_queue:
            # Pop the first patient from the queue (the one who has been waiting the longest)
            patient = self.consultation_queue.popleft()
            # Add the popped patient to the list of processed patients
            processed_patients.append(patient)

        self.processed_patients = processed_patients  # Store processed patients
        return "Consultations processed for: " + ", ".join([patient.name for patient in processed_patients])

    def print_consultation_queue(self):
        # Print the order of patients in the consultation queue
        if self.consultation_queue:
            print("Order of patients in consultation queue:",
                  ", ".join([patient.name for patient in self.consultation_queue]))
        else:
            print("Consultation queue is empty")

    def issue_prescription(self):
        # Issue prescriptions for patients in the consultation queue
        if self.processed_patients:  # Check if there are processed patients
            prescription_details_list = []  # List to hold details of issued prescriptions

            for patient in self.processed_patients:
                # Loop through each patient in the list of processed patients
                prescription = generate_prescriptions(1)[0]  # This generates a random prescription
                patient.pushPrescription(prescription)  # Push the prescription onto the patient's stack
                # Format and append prescription details to the list
                prescription_details = f"Prescription for {patient.name}: {prescription.medication_type} ({prescription.dosage})"
                prescription_details_list.append(prescription_details)

            self.processed_patients.clear()  # Clear the list after issuing prescriptions
            # Join and return the formatted prescription details
            return "\n".join(prescription_details_list)
        else:
            return "No patients to issue prescriptions to"


    def search_patient(self, patient_id):
        # Sorting patient IDs to enable binary search
        patient_ids_sorted = sorted(self.patients.keys())
        patient = None  # Initializing patient to None

        # Setting initial low and high indices for binary search
        low, high = 0, len(patient_ids_sorted) - 1

        # Binary search algorithm
        while low <= high:
            mid = (low + high) // 2  # Calculating mid index
            mid_patient_id = patient_ids_sorted[mid]  # Getting patient ID at mid index

            # Compare mid_patient_id with the search target (patient_id)
            if mid_patient_id < patient_id:
                low = mid + 1  # Searching in the right half
            elif mid_patient_id > patient_id:
                high = mid - 1  # Searching in the left half
            else:
                patient = self.patients[mid_patient_id]  # Patient found
                break  # Exit loop

        # If a patient is found
        if patient is not None:
            # Printing summary of patient information
            print(f"\nSummary for {patient.name} (ID: {patient.patient_id}):")
            print(f"  Condition: {patient.condition}")
            print(f"  Age: {patient.age}")

            # Checking for an appointment
            appointment_found = False
            for appointment in self.appointments:
                # Checking if the current appointment matches the patient ID
                if appointment[0].patient_id == patient_id:
                    # Print appointment details
                    print(f"  Appointment with Dr. {appointment[1].doctor_name} on {appointment[2]}")
                    appointment_found = True  # Marking appointment as found
                    break  # Exit loop
            if not appointment_found:
                print("  No appointment scheduled.")

            # Checking for prescriptions
            if patient.prescription_stack:
                # Print details of each prescription
                print("  Prescriptions:")
                for prescription in list(patient.prescription_stack):
                    print(f"    - {prescription.medication_type} ({prescription.dosage})")
            else:
                # No prescriptions issued for the patient
                print("  No prescriptions issued.")
        else:
            # Patient ID not found in the system
            print("Patient not found!")


    def exit_program(self):
        print("Thank you for using the Hospital's system. Exiting ..")
        exit()

    def test(self):
        print("\n--- Welcome to the hospital system ---")
        num_patients = int(input("Please enter the number of patients to add: "))
        self.add_new_patient(num_patients)
        print(f"{num_patients} New patients are added")

        # Main loop to display the menu and handle user choices
        while True:
            print("\n--- Hospital Management System Menu ---")
            print("1. List patients records")
            print("2. Update patient record")
            print("3. Remove patient record")
            print("4. Schedule an appointment")
            print("5. Process consultation")
            print("6. Search for a patient")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                for patient_id, patient in self.patients.items():
                    print(
                        f"Name: {patient.name}, ID: {patient.patient_id}, Condition: {patient.condition}, Age: {patient.age}")
            elif choice == "2":
                self.update_patient_record()
            elif choice == "3":
                patient_id = input("Enter patient ID to remove: ")
                print(self.remove_patient_record(patient_id))
            elif choice == "4":
                print(self.schedule_appointment())
                queue_display = input("Do you want to display the consultation queue (y/n)? ")
                if queue_display.lower() == "y":
                    print(self.print_consultation_queue())
            elif choice == "5":
                consultation_response = self.process_consultation()
                print(consultation_response)
                if "No patients in the consultation queue" not in consultation_response:
                    self.print_consultation_queue()
                    issue_prescription = input("Issue prescription for all patients (y/n)? ")
                    if issue_prescription.lower() == "y":
                        print(self.issue_prescription())
                else:
                    continue 
            elif choice == "6":
                patient_id = input("Enter patient ID:")
                print(self.search_patient(patient_id))
            elif choice == "7":
                self.exit_program()
            else:
                print("Invalid choice. Please try again.")


system = HospitalManagementSystem()
system.test()
