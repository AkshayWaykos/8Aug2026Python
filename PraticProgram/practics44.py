import time
from operator import concat

print("==========If else=================")
Mark=40
if Mark>=35:
    print("PASS")
else:
    print("FAIL")
print("=========If elif==================")

shoppintAMT=1000

if shoppintAMT>=4000:
    print("50% off")
elif shoppintAMT>=3000:
    print("20% Off")
elif shoppintAMT>=2000:
    print("10% off")
else:
    print("No Off")

print("=========Nester If==================")

Username="Akshay"
Password="Waykos"
if Username =="Akshay":
    print("UserName is Proper")
    print("Enter Password plzzz...")
    #time.sleep(5)
    if Password=="Waykos":
        print("Password is Proper")
        print("Allow to login")
    else:
        print("Password is wrong")
else:
    print("UserName is invalid")
print("============Match case===============")
input=2

match input:
    case 1:
        print("Addition of two no = ", 1+2)
    case 2:
        print("Addition of two no = ",3+2)
    case _:
        print("wrong data")
print("============For loop===============")
for i in range(1 , 11):
    print(i)
print("============For loop===============")
for j in range(10 , 0, -1):
    print(j)
print("============For loop even no print===============")
for k in range(1,10):
   if k % 2 ==0:     #even no
    result= k ** 2        #square
    print(f"{k} is Even, Square = {result}")
   else:
       result = k ** 3  # cube
       print(f"{k} is Odd, Cube = {result}")

print("============while loop ===============")

i=1
while i<=10:
    print(i)
    i+=1
print("============while loop ===============")

word="Sagar"
name=0
while name<len(word):
    print(word[name])
    name=name+1
print("============while loop ===============")

list1=[11,22,33]
list2=[44,55,66]

concat = list1 + list2   #1st way to do the concat
print(concat)

list1.extend(list2)     #2nd way to do the concat
print(list1)
print("==========================================")

class Addition:
    def add(self,a,b):
        print(a + b)
obj=Addition()
obj.add(10,20)
print("==========================================")
