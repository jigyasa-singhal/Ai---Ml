class student:

    college = "SDCET" #class attributes
    PI = 3.1

    def __init__(self,name,cgpa):
        # instance attributes
        self.name = name
        self.cgpa = cgpa
        self.PI = 3.14

s1 = student("ram",67)
print(s1.name)
print("calling the class attributes by obj:",s1.college)
print("calling the class attributes by class:",student.college)
print(s1.PI) 


'''
So if both the class and the object define an attribute with the same name:

obj.attr → instance value wins.

Class.attr → class value.
'''