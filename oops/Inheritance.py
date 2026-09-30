class Employees:#parent class 
    start_time = "10am"
    end_time = "6pm"

    def change_time(self,new_end_time):
        self.end_time= new_end_time

# single level inheritance 
class Teacher(Employees): #child class
    def __init__(self,subject):
        self.subjet= subject

    

t1 = Teacher("Maths")
t1.change_time("5pm")
print(t1.subjet,t1.start_time,t1.end_time)


# multilevel inheritance 
class AdminStaff(Employees):
    def __init__(self,role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(25_000,"CA")

print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)


#  