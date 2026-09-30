word1 = "hello"
word2 = "kaise ho "

# length 
print(len(word1))
# conactentation
print(word1 +" " + word2)
# iteration
print(word1[2])
for ch in word1:
    print(ch)

# slicing
print(word1[2:4])

s= "python"
print(s[2:-2])
print(s[:])


# format the strings 

#By the format function
a = 5
b = 6
sum = a+b
print("sum is {}".format(sum)) 

print("language is {}".format("python"))
print("value of a is {} and b is {}".format(a,b))
print("value of a is {1} and b is {0}".format(b,a))

print("values of a is  {a} and b is {b}".format(a=10,b=6))

# by the formatting  strings 
c= 18
d = 17
print(f"value of c is {c} and d is{d}")