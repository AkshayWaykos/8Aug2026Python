print("============Dictionary===================")

Dict1={"Akshay":1 , "Sagar":2  ,"Shiva":3 }
Dict2={ 1:"Kiran" , 2:"Dinesh" , 3:"Rajesh"}
Dict3={ 1:"Rahul" , 2:"Amol"   , 3:99.9  }

print(Dict1)
print(Dict2)
print(Dict3)

print(type(Dict1))

print(len(Dict1))

Dict1["Sakshi"]=4
print(Dict1)

Dict1.popitem()
print(Dict1)

print(Dict1.__contains__("Shiva"))

#Given Key and Print Value

print(Dict1["Akshay"])
print(Dict2[1])
print(Dict3[2])

Dict2[4]="Trupti"
print(Dict2)

Dict3.pop(1)
print(Dict3)

print("----get all keys Dict 1-----")

Allkeyvalue=Dict1.keys()
for Singlekey in Allkeyvalue:
    print(Singlekey)
print("----get all value Dict1-----")

allvalue=Dict1.values()
for singleval in allvalue:
    print(singleval)
print("----get all Key & value  Dict1-----")

allKeyVal=Dict1.items()
for singelKV in allKeyVal:
    print(singelKV)
print("----------------")
allKV=Dict2.items()
for singleKV1 in allKV:
    print(singleKV1)







