info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]
l=[]
student=[]
print(info)
for ch in info:
    l.append(ch[1])

    if (ch[1]=="English"):
        student.append(ch[0])


    
print("list of courses is ", l)
s3 = set(l)
print("list of unique courses is ", list(s3))

print(student)

dict = {}

for name ,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)




