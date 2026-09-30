# list 
l = [12,34,23,78]
print(l)
print(len(l))
print(l[3])

l[3] = 67
print(l)

print(l[:2])
# list methods 
l.append(32)
l.insert(0,89)
print("l after adding 32 and 89 at 0 index  " , l)
l.sort()
print("l after sort in increasing order " , l)

l.sort(reverse=True)
print("l after sort in decreasing order" , l)

l.reverse()
print("l after reverse" , l)

idx = 0
x=32
for val in l :
    if (val == x):
        print(f"found at {idx}")
        break
    idx+=1

# tuple 
tup =(67,34,8,"hello",67)
print(type(tup))

print(tup.index(67))
print(tup.count(67))


# dictionary
d = {
    "name": "yash",
    "roll no ": "12"
}
print(d)
print(d["name"])
d["roll no "] = "43"
print(d)

print("keys are",d.keys())
print("values are",d.values())
print("keys value pairs are",d.items())
print("value of name is are",d.get("name"))
print("value of name is are",d["name"])

d.update({
    "marks": "98"
})


print(d)


# set
s= {1,2,4,5,4}

print(s)
print(type(s))
s1={}
print(type(s1))
s2 = set()
print(type(s2))
s.add(67)
s.remove(1)

print(s)
s.pop()
print(s)
s.clear()
print(s)
s1= {1,34,33,24,34}
s2 = {89,56,83}

print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))



