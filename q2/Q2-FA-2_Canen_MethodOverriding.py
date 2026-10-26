class Patient: 
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name 

    def get_bill_amount(self):
        return self._bill_amount

    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self._bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self._bill_amount * 0.80

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self._bill_amount * 0.85


# testing mic test mic test

regular_patient = Patient("Ruggie Bucchi", 1800.0)
senior_patient = SeniorPatient("Lilia Vanrouge", 7000.0)
philhealth_patient = PhilHealthPatient("Riddle Rosehearts", 1700.0)

patients = [regular_patient, senior_patient, philhealth_patient]

print("Hospital Billing System")
for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount()}")
    print(f"Final Bill: ₱{patient.calculate_bill()}\n")