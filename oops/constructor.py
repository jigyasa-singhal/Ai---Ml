class Student:
    def __init__(self): #default
        print("hello")
    def __init__(self,name,age): #parameterized 
        self.name = name
        self.age = age
    def get_age (self):
        return self.age
    

s1 = Student("rahul",45)
print(s1.name)
print(s1.__dict__)   # shows all attributes as a dictionary
print(s1.get_age())

print(vars(s1))
