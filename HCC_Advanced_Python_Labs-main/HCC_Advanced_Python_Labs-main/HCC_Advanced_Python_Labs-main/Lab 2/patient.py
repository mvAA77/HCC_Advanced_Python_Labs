### Tanya Kadiyala
### CMSY-257-300
### Lab 2
### Problem 3: Patient and Procedure

class Patient:
    def __init__(self, first_name, last_name, address, phone, emergency_contact):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.emergency_contact = emergency_contact
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return (f"Patient: {self.full_name}\n"
                f"Address: {self.address}\n"
                f"Phone: {self.phone}\n"
                f"Emergency Contact: {self.emergency_contact}")


class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge
    
    def __str__(self):
        return f"{self.date} — {self.name} by {self.practitioner} — ${self.charge:.2f}"


def print_invoice(patient, procedures):
    # Sort procedures by date
    sorted_procedures = sorted(procedures, key=lambda x: x.date)
    
    # Calculate total charge
    total_charge = sum(proc.charge for proc in procedures)
    
    # Print invoice
    print("=" * 50)
    print("MEDICAL INVOICE")
    print("=" * 50)
    print(patient)
    print("-" * 50)
    print("PROCEDURES:")
    for procedure in sorted_procedures:
        print(f"  • {procedure}")
    print("-" * 50)
    print(f"TOTAL CHARGE: ${total_charge:.2f}")
    print("=" * 50)


# Driver code
if __name__ == "__main__":
    # Create one Patient
    p = Patient("John", "Doc", "123 Main St", "555-1234", "Jane Doc")
    
    # Create at least 3 Procedure objects with different dates and charges
    proc1 = Procedure("X-Ray", "2025-01-10", "Dr. Smith", 200)
    proc2 = Procedure("MRI", "2025-02-01", "Dr. Lee", 1200)
    proc3 = Procedure("Blood Test", "2025-01-05", "Dr. White", 100)
    
    procedures = [proc1, proc2, proc3]
    
    # Call print_invoice
    print_invoice(p, procedures)