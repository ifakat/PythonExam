from datetime import datetime

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        # Patient attributes
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
        self.procedures = []  # List to store all procedures associated with the patient

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    def get_emergency_contact_info(self):
        return f"Emergency Contact: {self.emergency_contact_name}, {self.emergency_contact_phone}"

    def add_procedure(self, procedure):
        # Method to add a procedure to the patient's list
        self.procedures.append(procedure)

    def get_all_procedures(self):
        return self.procedures

    def calculate_total_charges(self):
        # Method to calculate the total charges for all procedures associated with the patient
        return sum(procedure.procedure_charges for procedure in self.procedures)

    def calculate_total_charges_by_type(self, procedure_types):
        # Method to calculate the total charges for specific types of procedures
        return sum(procedure.procedure_charges for procedure in self.procedures if procedure.procedure_name in procedure_types)

    def calculate_total_charges_by_date(self, target_date):
        # Method to calculate the total charges for procedures performed on a specific date
        return sum(procedure.procedure_charges for procedure in self.procedures if procedure.procedure_date == target_date)


class Procedure:
    def __init__(self, procedure_name, practitioner_name, procedure_charges):
        # Procedure attributes
        self.procedure_name = procedure_name
        self.procedure_date = datetime.today().strftime('%Y-%m-%d')  # Current date
        self.practitioner_name = practitioner_name
        self.procedure_charges = procedure_charges

    def get_patient_name(self, patient):
        # Method to get the patient's full name
        return patient.get_full_name()

    # Add accessor and mutator methods for each attribute as needed


def main():
    # Create an instance of the Patient class with sample data
    patient = Patient("John", "Doe", "", "123 Main St", "Cityville", "CA", "12345", "555-1234", "Jane Doe", "555-5678")

    # Create instances of the Procedure class with sample data
    procedure1 = Procedure("X-Ray", "Dr. Smith", 500)
    procedure2 = Procedure("Blood Test", "Dr. Johnson", 300)
    procedure3 = Procedure("MRI", "Dr. Williams", 800)
    #procedure4 = Procedure("Blood Test", "Dr. Anderson", 400)

    # Add procedures to the patient
    patient.add_procedure(procedure1)
    patient.add_procedure(procedure2)
    patient.add_procedure(procedure3)
    #patient.add_procedure(procedure4)

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

    # Calculate and display the total charges for specific types of procedures
    specific_procedure_types = ["Blood Test", "MRI"]
    specific_procedure_charges = patient.calculate_total_charges_by_type(specific_procedure_types)
    print(f"Total Charges for {', '.join(specific_procedure_types)}: {specific_procedure_charges}")

    # Calculate and display the total charges for procedures performed on a specific date (current date in this example)
    target_date = datetime.today().strftime('%Y-%m-%d')
    total_charges_by_date = patient.calculate_total_charges_by_date(target_date)
    print(f"Total Charges for Procedures on {target_date}: {total_charges_by_date}")


if __name__ == "__main__":
    main()
