
ss={11,33,66,77,"Akshay",'Sagar',11.34}
s1={11,33,66,77,11.34}

print(ss)

print(sorted(s1))
# add/update/remove/discard
ss.add("Shiva")
print(ss)

ss.update(["Ganesh","Rahul"])
print(ss)

ss.remove(66)
print(ss)

ss.discard(99)
print(ss)
ss.discard(33)
print(ss)

#set to list

s2={22,55,77,99,11,00,44}
print(s2)
print(type(s2))

s3=list(s2)
print(s3)
print(type(s3))

print("-------------------")

#List to set
l1=[23,45,67,34,23,77,99,00]
print(l1)
print(type(l1))

l2=set(l1)
print(l2)
print(type(l2))

l2.remove(67)
print(l2)

l4=l2.copy()
print(l4)

print(sorted(l4))
































