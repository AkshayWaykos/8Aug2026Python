
print("===Dictionary====")

dict1={"Akshay" : 1 , "Sagar" : 2 , "Shiva" : 3}
dict2={1:"Akki" , 2: "Sakshi" , 3 : "Shaggy"}
dict3={1:11 , 2:22 , 3 :"Kiaynsh" , 4 : "Trupti" }

print(type(dict))
print(len(dict1))

key=dict1.keys()
print(key)

print(dict1["Sagar"])    #get Value

print(dict2[1])         #get value

print(dict1.__contains__("Shiva"))
print("Shiva" in dict1)
print("----------------")
allKey=dict1.keys()
for singlekey in allKey:
    print(singlekey)
print("------------------")
allval=dict1.values()
for singleval in allval:
    print(singleval)

print("----------------")

allK_V=dict1.items()
for singleKV in allK_V:
    print(singleKV)







