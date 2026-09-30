class Teacher:
    def __init__(self,salary,subject):
        self.salary = salary

        self.subject = subject


class Student:
    def __init__(self,year,fee):
        self.year = year

        self.fee=fee


class TA(Teacher,Student):
    def __init__(self,salary,subject,year,fee,name):

        Teacher.__init__(self, salary, subject)   # direct call
        Student.__init__(self, year, fee)         # direct call
        self.name = name

# t1 = TA("6000", "maths", "2nd", 90, "rahul")
t1 = TA(salary=6000, subject="maths", year="2nd", fee=90, name="rahul")
print(t1.salary)   # 6000
print(t1.subject)  # maths
print(t1.year)     # 2nd
print(t1.fee)      # 90
print(t1.name)     # rahul

print(TA.mro()) # gaves which parent class will runs first

#  or done by super().__init__(**kwargs)


'''
class Teacher:
    def __init__(self, subject, salary, **kwargs):
        super().__init__(**kwargs)   # pass along
        self.subject = subject
        self.salary = salary
/
class Student:
    def __init__(self, fee, year, **kwargs):
        super().__init__(**kwargs)   # pass along
        self.fee = fee
        self.year = year

class TA(Teacher, Student):
    def __init__(self, name, subject, salary, fee, year):
        super().__init__(subject=subject, salary=salary, fee=fee, year=year)
        self.name = name

t1 = TA("Rahul", "Maths", 6000, 90, "2nd")
print(t1.subject, t1.salary, t1.fee, t1.year, t1.name)

'''