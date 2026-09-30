age = 18 
if(age>=18):
    print("can vote")
else:
    print("no")

# problem
age = int(input("Enter the age "))
if(age>=18):
    print("adult")
elif(age>=1 & age<13):
    print("child")
elif(age>13 & age<18):
    print("teenager")
else:
    print("input correct age ")


# problem
user = "admin"
passwo = "pass"

u = input("enter user name")
p = input("enter password")

if(u == user):
    if(p!= passwo):
         print("enter correct password ")
    else:
        print("login success")
else:
    print("enter correct user name")