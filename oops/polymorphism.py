
# overriding
class Employee:
    def get_designation(self):
        print("Employee designation: General Worker")

class Accountant(Employee):   # Inherits Employee
    def get_designation(self): # Overrides parent's method
        print("Employee designation: Accountant")

emp1 = Employee()
acc1 = Accountant()

emp1.get_designation()   # Employee designation: General Worker
acc1.get_designation()   # Employee designation: Accountant



# duck typinng 
class Employee:
    def get_designation(self):
        print("Employee designation: General Worker")

class Accountant:
    def get_designation(self):
        print("Employee designation: Accountant")

acc1 = Accountant()       # Correct class name
acc1.get_designation()    # Correct variable name
