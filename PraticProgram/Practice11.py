
print("=====Msg display===========")

print("Hi and hello")

print("=====Variable & Data type===========")
# 8 data type
int = 1
str = "Akki"
floo = 2.4
bool = True
dict = {"Name": "Akshay"}
set = {1, 2, 3, "a", 4, 2}  # automatically remove duplicate value in output.
list = [1, 5, 2, 6, 3, 7, 4, 8, 8, 1, ]
tuple = (10, 20)

print(int, str, float, bool, dict, set, list, tuple)

print("=====Data type print in OUTPUT===========")
# Datatype print
amount = 1000
print(amount)
print(type(amount))

print("=====if statement===========")
mark = 40
if mark > 35:
    print("PASS")

print("=====if else statement===========")

mark = 30
if mark >= 35:
    print("PASS")
else:
    print("FAIL")
print("=====if elif else statement===========")

mark = 89
if mark >= 80:
    print("Distiction")
elif mark >= 70 and mark <= 80:
    print("Pass with A Grade")
elif mark >= 60 and mark <= 50:
    print("Pass with B Grade")
elif mark >= 55 and mark <= 60:
    print("Pass with C Grade")
else:
    print("FAIL")

print("=====arithmatic Operation===========")

i = 40
j = 10

k = i + j

print("Addition of 2 no=", k)

k = i * j
print("Multiplication of 2 no=", k)

k = i / j
print("Division of 2 no=", k)

k = i - j
print("Subtraction of 2 no=", k)

print("=====Done===========")
