from calendar import week
import time
from traceback import print_tb

# print("=============Data type==================")
#
# i=1
# j="Trupti"
# k=5.4
# l=[1,2,3,4,5]
# m={2,3,5,6,7,8,3,2,1}
# b=True
# dict={"Name " : "Akshay" }
#
# print(i)
# print(j)
# print(k)
# print(l)
# print(m)
# print(b)
# print(dict)
# print("==================if else statement=======================")
# i=11
# if i<=10:
#     print(i)
# else:
#     print("Wrong input")
# print("==================if elif statement=======================")
# mark=34
# if mark>65:
#     print("Disction")
# elif mark<65 and mark>55:
#     print("class A")
# elif mark<55 and mark>44:
#     print("class B")
# elif mark<44 and mark>=35:
#     print("class C")
# else:
#     print("just pass")
print("==================nester if statement=======================")
age=18
if age>=18:
    print("According to Age Your Eligible")
    print("Now check Your weight for blood donation")
    time.sleep(1)
    weight=50
    if weight>=50:
        print("According to weight Your Eligible for blood donation ")
    else:
        print("According to weight Your Not Eligible for blood donation")
else:
    print("According to Age Your Not Eligible for blood donation")
# print("==================match case statement=======================")
# input=1
# match input:
#     case 1:
#         print("Addition of two no =", 10+20)
#     case 2:
#         print("Multiplication of two no =",10*20)
#     case _:
#         print("Wrong input")
# print("==================for statement=======================")
#
# for i in range(1,11,1):
#     print(i)
# print("======")
# for j in range(1,5):
#     print(" Hi " * j )
# print("==================while loop statement=======================")
# i=1
# while i<=10:
#     print(i)
#     i+=1
#
# print("======")
# i=10
# while i>=1:
#     print(i)
#     i-=1
#
# print("==================while loop statement=======================")
#
# k=1
# while k<=5:
#     print(k)
#     k+=1