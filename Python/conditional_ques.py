n = int(input("Enter the number"))

if  (n%2 ==0):
    print("even")
else:
    print("odd")


# match case
num = int(input("enter the number "))
match (num):
    case 1 :
        print("yes")
    case 2:
        print("no")
    case _:
        print("Wrong")


