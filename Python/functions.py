# Function Definition  
def hello():  
    print("hello from Prime")
hello() #function calll

# Fnx to compute sum of 2 nums  
def sum(a, b):   
    print (a + b)  
# a & b are parameters  
# 5 & 10 are arguments
# 
(sum(5, 10))  
print(sum(5, 10))   # it will gave none because sum is not returning anything


# Fnx to computer average of 3 nums  
def avg(a, b, c):  
    return (a + b + c) / 3  
print(avg(1, 2, 3))


# sum() fnx with default param 1  
# non default always comes forst otherwise it will gave error
def sum(a, b = 1): # default val of b is 1  
    return a + b  
print(sum(5)) # output: 6 


# fnx to compute x^2  
square = lambda x: x * x  
print(square(5)) 


import functools

fact = lambda f: 1 if f == 0 else f * fact(f-1)
print("factorial is", fact(4))  # Output: 24



# Factorial of N  
n = int(input("enter n: "))  
fact = 1  
for i in range (1, n+1):  
    fact *= i  
print("factorial = ", fact)

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
