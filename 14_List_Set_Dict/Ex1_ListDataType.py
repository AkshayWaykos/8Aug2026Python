print("====List Data Type======")

s1=["Akshay",101,66.8,'O+',101]

# append = add the data in end of list
# insert = insert the data in list as per index
#extends = extends the list with new data

print(s1)
print(type(s1))
print("---------------------")
s1.append("Sagar")
print("After Append =",s1)    #data Added at the End of list
print("---------------------")
s1.insert(3,"Shiva")
print("After Insert =",s1)    #insert data as per Index
print("---------------------")
s1.extend([10,20,"Akki",'B+',101])
print("After Extend =",s1)    #Add new List in old list like extends the list

print("---------------------")
#pop = remove data
#pop(index) = as per index remove data from list
#remove(element) = Remove specific element

s1.pop()
print("After pop =",s1)      #remove Last data from list.

print("---------------------")

s1.pop(3)                     #remove Shiva data from list(3 no data removed)
print("After pop(index) =",s1)

print("----------------------")

s1.remove("Akki")              #Remove specific element
print("After Remove = ",s1)











