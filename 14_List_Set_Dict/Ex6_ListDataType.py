print("=========================")

# append(ele)          = Add data in list at end
# Insert(index, ele)   = Insert Data in list on index
# Extend([ele1,ele2…]) = Add list in extends
# pop()                = End the last data from list
# pop(index)           = Remove data from list as per index no
# remove(ele)          = Remove particulate data from list
# reverse()            = reverse the list data
# sort()               = sort the list data
# count(ele)           = check count of same data from list
# clear()              = clear data from list
#copy()                = copy data from list


L1=[10,20,"Akshay",'Sagar',"A+","B-",99.99,1,2,3,4,4,5,6,7,8,8,8,9,]
#Append
L1.append("Khatam")
print(L1)
#Insert
L1.insert(3,"Shiva")
print(L1)
#extends
L1.extend([20,30,40])
print(L1)
#POP
L1.pop()
print(L1)
#pop(index)
L1.pop(5)
print(L1)
#Remove
L1.remove("Khatam")
print(L1)
#reverse
L1.reverse()
print(L1)
#sort  = Ascending order
L2 = [88,99,3,4,4,5,1,7,8,8,8,9,99]
L2.sort()
print(L2)
L3 =["Akshay","Sagar",'A+','B+']    # A to Z
L3.sort()
print(L3)

#count(ele)
print(L2.count(99))

#clear
L2.clear()
print(L2)

#copy ==copy from onc list other
L4 = [88,99,3,4,4,5,1,7,8,8,8,9,99]
L5 = L4.copy()
print(L5)

L6=L1.copy()
print(L6)










