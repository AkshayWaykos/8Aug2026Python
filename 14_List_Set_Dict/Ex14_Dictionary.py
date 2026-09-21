
#key-String, value-float

dict1={"Akshay":75.5 , "Sagar":88.9, "Shiva" : 91.9}
print(dict1)
dict2={1:"Akshay",2:"Sagar",3:"Shiva"}
print(dict2)
dict3={1:"Akshay",2:"Sagar",  3:85.7, 4:89 }
print(dict3)

print(type(dict1))

print(len(dict1))

print("--Given Key and Print Value--")
print(dict1["Sagar"])
print(dict2[2])
print(dict3[3])

#update/modify value of any specific key

dict1["Akshay"]=55.6
print(dict1)

dict2[1]="AKSHAY"
print(dict2)

dict3[3]=88.8
print(dict3)

#check value from dict

print(dict1.__contains__("Akshay"))
print(dict2.__contains__(2))
print(dict3.__contains__(1))

#Add new key-value pair
dict1["AMOL"]=44.5
print(dict1)

dict2[4]="Suresh"
print(dict2)

dict3[5]=90.3
print(dict3)

#remove key-value pair
dict1.pop("AMOL")
print(dict1)

dict2.pop(4)
print(dict2)

dict3.pop(5)
print(dict3)

#Remove last inserted item(k-v)
dict3.popitem()
print(dict3)

print("----get all keys-----")

allkey=dict1.keys()            #keys  -->for all key
print(allkey)
for singlekey in allkey:
    print(singlekey)

print("---------------")

for singlekey in dict1.keys():
    print(singlekey)

print("----get all value-----")
allval=dict1.values()
print(allval)
for singleval in allval:
    print(singleval)

print("---------")
for singleval in dict1.values():
    print(singleval)

print("----get all Key and value-----")

allkeyval=dict1.items()
for k,v in allkeyval:
    print(k,v)

print("-----")

for k,v in dict1.items():
    print(k,v)

print("-----")

for key in allkeyval:
    print(key)

print("---clear all data in dict---")
dict1.clear()
print(dict1)

del dict1
#print(dict1) --> it will show error boz dict1 is deleted


















