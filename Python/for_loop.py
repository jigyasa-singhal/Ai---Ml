s = "hello"
for i in s:
    print(i)

if "he" in s :
    print("yes")

# problem - count no's of i 
count = 0 
word = "artificial intelligence "
for ch in word:
    if (ch =='i') :
        count+=1
print(count )

#  probrlem - print vowel count in a string 
# way =01
vowel =0 
word = "hello"
s='aeiouAEIOU'
for ch in word:
   for che in s:
       if(ch==che):
           vowel+=1
print(vowel)
# way = 02
vowel1 = 0 
for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i'or ch == 'o' or ch == 'u'):
        vowel1 +=1
print(vowel1)

# range function
# single argument - start  
for i in range(5):  
    print(i)  
# output: 0, 1, 2, 3, 4  
# 2 arguments - start, stop  
for i in range(1, 6):  
    print(i)  
# output: 1, 2, 3, 4 , 5  
# 3 arguments - start, stop, step  
for i in range(1, 10, 2): 
    print(i)  
# output: 1, 3, 5, 7, 9 


# sum of firsst n natural numbers
sum = 0
for i in range(11):
    sum += i
print("sum is ",sum )