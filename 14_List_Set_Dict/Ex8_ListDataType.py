
L=[12,23,34,"Akshay",'A+',23.23]

L.pop()
print(L)

L.pop(2)
print(L)

L.remove('A+')
print(L)
print("---------------")
L.insert(2,"Sagar")
print(L)

L.extend([11,22,33,44,55,66])
print(L)

L.append("Shiva")
print(L)
print("-----------------")
L.reverse()
print(L)

L1=[11,"Akshay",'Sagar','Shiva',101,108,22.22]

L3=L1.copy()
print(L3)

L4=[11,55,22,77,99,]
L4.sort()
print(L4)

print(L3==L4)
print(L3.__eq__(L4))

for i in range (4):
    print(L4[i])

for i in L4:
    print(i)

L5=[1,2,3,4,5,6,7,8,8]
print(L5.count(8))






