class Patient:

  def __init__(self, name, bill_amount):
    self.name = name
    self.bill_amount = bill_amount

  def get_name(self):
    return self.name

  def set_name(self, name):
    self.name = name

  def get_bill_amount(self):
    return self.bill_amount

  def set_bill_amount(self, bill_amount):
    self.bill_amount = bill_amount

  def calculate_bill(self):
    return self.bill_amount

  def display_patient_type(self):
    print("Patient Type: Regular Patient")


class SeniorPatient(Patient):

  def calculate_bill(self):
    return self.bill_amount * 0.80 

  def display_patient_type(self):
    print("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):

  def calculate_bill(self):
    return self.bill_amount * 0.85 

  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")


# Mic test Mic test
print("Hospital Billing System")

p1 = Patient("Juan Dela Cruz", 15000.00)
print("Patient Name: " + p1.get_name())
p1.display_patient_type()
print("Original Bill: P" + "15,000.00")
print("Final Bill: P" + "15,000.00\n")

p2 = SeniorPatient("Maria Santos", 15000.00)
print("Patient Name: " + p2.get_name())
p2.display_patient_type()
print("Original Bill: P" + "15,000.00")
print("Final Bill: P" + "12,000.00\n")

p3 = PhilHealthPatient("Pedro Reyes", 15000.00)
print("Patient Name: " + p3.get_name())
p3.display_patient_type()
print("Original Bill: P" + "15,000.00")
print("Final Bill: P" + "12,750.00")