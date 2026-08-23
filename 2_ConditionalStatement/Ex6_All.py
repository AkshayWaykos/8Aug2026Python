print("===================if statement========================")

mark = 35

if mark >= 35:
    print("PASS")

print("===================if else statement========================")

Make = 20
if mark >= 35:
    print("PASS")
else:
    print("FAIL")

print("===================elif statement========================")

marks = 20

if marks >= 60:
    print("Distinction")
elif marks >= 60 and marks < 65:
    print("Pass with A Grade")
elif marks >= 50 and marks < 55:
    print("Pass with B Grade")
elif marks < 35:
    print("Fail")

print("===================set other tpoic ========================")
fruits = {"apple", "mango", "apple", "banana", "mango"} #duplicate will not print
listww=[11,22,11,33,44,]   #duplicate will print in OP

print(listww)
print(fruits)