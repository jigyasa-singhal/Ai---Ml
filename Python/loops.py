# while loop - runs till the condition is true 
n = 1
while(n<5):
    print("hello")
    n+=1

# for loop 
for i in range(5):
    print("for loop")

# use of break and continue
num = int(input("Enter the number"))
for i in range(1,11):
    if(i==5):
        continue
    if(i==7):
        break
    print(num*i)

print("out of loop")




    

