print("=======================")

l1=[12,23,34,56,78,"Akki","A+",23.23]
l3=[10,20,30]

l1[5]="Akshay"
print(l1)

l2=l1.copy()
print(l2)

for i in l2:
    print(i)

for i in range (0,7):
    print(l2[i])

print(l2.__contains__("Akki"))

print(len(l1))

l1.reverse()
print(l1)

print(l1.__eq__(l3))

print(l1)
print(l2)
print(l3)



