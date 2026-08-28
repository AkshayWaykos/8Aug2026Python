
print("==== Q . How can you Concatenate two list in python?====")
print ("First Way Using +")

# Using +

list1 = [1,2,3]
list2 = [4,5,6]

concatenation = list1 + list2
print(concatenation)

print("========================================")

print("===#Using .extends===")
# Using .extends

list3 = [1,2,3,4,5]
list4 = [4,5,6,7,8]

list3.extend(list4)
print("After extending list", list3)
print("========================================")

col1=[11,22,33,44]
col2=[55,66,77,88]

collection = col1+ col2
print(collection)

print(type(collection))

print("===============================")

emp2026=[3218,3219,3220]
emp2027=[4218,4219,4220]

emp2026.extend(emp2027)
print(emp2026)

print("===============================")