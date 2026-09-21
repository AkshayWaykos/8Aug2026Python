L1=[11,22,33,3.4,'Akki',"Sagar",'A+']
L2=[3,2,2,4,1,5]
print("Check type = ",type(L1))

print("Count lent of List =",len(L1))

print("check index of data =",L1.index(33))

L1.append("Shiva")
print(L1)

L1.remove("Shiva")
print(L1)

L1.pop()
print(L1)

L1.count(33)
print(L1)

L1.insert(2,"Akshay")
print(L1)

L1.reverse()
print(L1)

L1.extend([10,20,30,30,40])
print(L1)

L1.pop(2)
print(L1)

print(L1.__eq__(L2))

L3=L1.copy()
print(L3)

L4=set(L3)
print(type(L4))
print(L4)

L2.sort()
print(L2)

print(L2.__contains__("Akshay"))

L2.clear()
print(L2)



