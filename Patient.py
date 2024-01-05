from datetime import datetime

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.procedures = []  # Liste, hastanın sahip olduğu tüm işlemleri depolamak için

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    def get_emergency_contact_info(self):
        return f"Emergency Contact: {self.emergency_contact_name}, {self.emergency_contact_phone}"

    def add_procedure(self, procedure):
        self.procedures.append(procedure)

    def get_all_procedures(self):
        return self.procedures

    def calculate_total_charges(self):
        return sum(procedure.procedure_charges for procedure in self.procedures)


class Procedure:
    def __init__(self, procedure_name, practitioner_name, procedure_charges):
        self.procedure_name = procedure_name
        self.procedure_date = datetime.today().strftime('%Y-%m-%d')  # Mevcut tarih
        self.practitioner_name = practitioner_name
        self.procedure_charges = procedure_charges

    def get_patient_name(self, patient):
        return patient.get_full_name()


def main():
    # Create an instance of the Patient class with sample data
    patient = Patient("John", "Doe", "", "123 Main St", "Cityville", "CA", "12345", "555-1234", "Jane Doe", "555-5678")

    # Create three instances of the Procedure class with sample data
    procedure1 = Procedure("X-Ray", "Dr. Smith", 500)
    procedure2 = Procedure("Blood Test", "Dr. Johnson", 300)
    procedure3 = Procedure("MRI", "Dr. Williams", 800)

    # Add procedures to the patient
    patient.add_procedure(procedure1)
    patient.add_procedure(procedure2)
    patient.add_procedure(procedure3)

    # Display patient information
    print("Patient Information:")
    print("Name:", patient.get_full_name())
    print("Address:", patient.get_address())
    print(patient.get_emergency_contact_info())
    print()

    # Display information about all procedures for the patient
    print("Procedures for the Patient:")
    for idx, procedure in enumerate(patient.get_all_procedures(), 1):
        print(f"{idx}. Name: {procedure.procedure_name}")
        print(f"   Date: {procedure.procedure_date}")
        print(f"   Practitioner: {procedure.practitioner_name}")
        print(f"   Charges: {procedure.procedure_charges}")
        print()

    # Calculate and display the total charges for the patient
    total_charges = patient.calculate_total_charges()
    print("Total Charges for All Procedures:", total_charges)


if __name__ == "__main__":
    main()