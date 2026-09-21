from filecmp import clear_cache

print("===List=====")

# append(ele)
# Insert(index, ele)
# Extend([ele1,ele2…])
# pop()
# pop(index)
# remove(ele)
# copy()
# reverse()
# sort()
# count(ele)
# clear()

li=[11,22,44,"Akki","O+",23,33.34,"Sagar"]

print(li)

print(type(li))

print(len(li))

li.append("Akshay")
print(li)

li.insert(2,"Akkkkk")
print(li)

li.extend([99,88,77])
print(li)

li.pop()
print(li)

li.pop(5)
print(li)

li.remove(88)
print(li)

ll=li.copy()
print(ll)

li.reverse()
print(li)

l2=[4,6,7,8,3,2,5,3,2]

l2.sort()
print(l2)

print(ll)
print(ll.count("Akshay"))

ll.clear()
print(ll)

del ll
#print(ll)

lll=[11,22,44,655,77,888,33,2]

#list to set
l22=set(lll)
print(l22)

