print("==============")

# List is declared using [ ] & Set is declared using { }
# List Allow duplicate & set doesn’t allow duplicate values
# List maintain order & set doesn’t maintain order (Random order of insertion)
# List support indexing & set does not support indexing

ss={11,'Akki',11,23,34,45,"Akshay"}

print(ss)
# ------Adding Elements (add/update)----------
ss.add("Sagar")                       #it uses to add single data in set
print(ss)

ss.update(["Ganesh","Ramesh"])         #to update multiple data in set
print(ss)

# ------Removing Elements(remove/discard)----------
ss.remove('Akki')                      #remove single data from set
print(ss)

# ss.remove('shaggy')
# print(ss)             #If data are not in set than it will show KeyError: 'shaggy' , to avoid error use decart

ss.discard('Shaggy')
print(ss)               #even data are not in set still system will not show the error.

ss.pop()
print(ss)               #remove any random data from set

#copy set
ss1=ss.copy()
print(ss1)

#sorting                   #for sorting set we used SORTED
s1={11,44,66,88,22}
print(sorted(s1))

s1=sorted(s1)            #reinitialization
print(s1)

#delete/clear all data from set obj
s2={11,'Akki',11,23,34,45,"Akshay"}

s2.clear()
print(s2)

del s2


print("------Print all data using for each loop-----")
s3={55,'Sagar',00,23,11,45,"Shiva"}
for i in s3:
    print(i)





























