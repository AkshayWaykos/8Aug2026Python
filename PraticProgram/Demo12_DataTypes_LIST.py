#
# append(ele)
# Insert(index, ele)
# Extend([ele1,ele2…])
# pop()
# pop(index)
# remove(ele)
# copy()
# sort()
# reverse()
# count(ele)
# clear()

list=[11,11,12,13,14,15,'AAA',"BBB",12.5,]
lisss=[22,11,55,33,66,88,99]

print(list)             # print list data
print(type(list))       #data type
print(len(list))        #length os list

print(list.count(11))   #how many element in list?

list.append(22)
print(list)           #Add element in list

list.insert(1,"XYZ")         #insert data according to index
print(list)

list.extend([66,77,88])    #extend the list data
print(list)

list.pop()              #remove from last
print(list)

list.pop(1)
print(list)           # remove as per index

list.remove('BBB')     #remove data from list
print(list)

li=list.copy()        #copy list
print(li)

lisss.sort()
print(lisss)

lisss.reverse()
print(lisss)

list=set(list)   #list to set
print(list)

lisss.clear()
print(lisss)