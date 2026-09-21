print("=====================================")

# Append = add the data in end of list
# Insert = insert the data in list as per index
# Extends = extends the list with new data

l1=[12,"Kiyansh",201,33.2,'O+',"abcd"]

l1.append("Sagar")
print("Append = ",l1)    #add data in list on last

l1.insert(2,"Shiva")
print("Insert =",l1)    #on 2 position adding shiva data

l1.extend([20,30,40,50,60])
print("Extends = ",l1)

print("=====================================")
#pop = remove data
#pop(index) = as per index remove data from list
#remove(element) = Remove specific element

l1.pop()
print("Pop = ",l1)    #remove last data from list

l1.pop(2)
print("pop(index=",l1)    #remove 2 no data from list

l1.remove(40)
print("Remove data = ",l1)  #remove 40 data from list

print("=====================================")




