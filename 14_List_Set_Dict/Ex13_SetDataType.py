s1={11,33,44,'akshay',"Sagar",99,'A+',4.5}

print(type(s1))

print(len(s1))

print(s1.__len__())

s1.__contains__(101)
print(101 in s1)      #False

s1.add(999)
print(s1)

s1.update([80,90,100])
print(s1)

s1.remove(100)
print(s1)

s1.discard(45)
print(s1)

s1.pop()
print(s1)

s11=s1.copy()
print(s11)

s2={1,2,3,4,5,3,2,1,3,4}
sorted(s2)
print(s2)

print(s2.__contains__(1))

for i in s2:
    print(i)

s2.clear()
print(s2)
