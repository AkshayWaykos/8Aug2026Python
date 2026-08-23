from queue import PriorityQueue
from xml.dom.minidom import ProcessingInstruction

print("===============Addition of 2 number ============")
i=1
j=2
k=i+j
print("Total no is = ",k)

print("===============    if statement    ============")
str="akshay"
if str=="akshay":
    print(str, "Name is proper")
print("===================if statement  ===============")
salary=50000
if salary<=50000:
    print("Employee Salary=",salary)
print("===================if else======================")
BillAmt=500
if BillAmt>=500:
    print("No Delivery Fee")
else:
    print("Delivery Fee 50 Rs")
print("===================if else======================")
mark=40
if mark<=35:
    print("PASS")
else:
    print("FAIL")
print("===================if elif======================")

ShoppintAMT=3200

if ShoppintAMT>=5000:
    print("20 % off")
elif ShoppintAMT>=4000:
    print("10 % off")
elif ShoppintAMT>=3000:
    print("5% Off")
else:
    print("No Off")

print("===================if elif======================")
mark = 20
if mark >= 85:
    print("Distinction")
elif mark >= 80 and mark < 85:
    print("1st class")
elif mark >= 50 and mark <= 60:
    print("2nd class")
else:
    mark <= 35
    print("Fail")
print("===================Nester=d if======================")

PRM = 251

if PRM >= 250:
    print("Selected in Prelim")
    print("Prepared for Mains Exam")
    mains = 400
    if mains >= 450:
        print("Selected in Mains Exam")
    else:
        print("rejected from Mains Exam")
else:
    print("Rejected from Prelim exam")
print("===================Nester=d if======================")

Age = 20
if Age >= 18:
    print("Your Age Eligible for Blood donation")
    print("Check wight before Blood Donate")
    wight = 50
    if wight >=50:
        print("Your Eligible for Blood Donation")
    else:
        print("According to wight your not eligible")
else:
    print("According to Age criteria your not eligible")

print("==============Match case statement===============")

input=10

match input:
  case 1:
      print("Akshay")
  case 2:
      print("Sagar")
  case 3:
      print("Shiva")
  case 4:
      print("sakshi")
  case 5:
      print("Waykos")
  case _:
      print("Wrong Data")

print("================Match case statement================")

line=3
match line:
    case 1:
        print(1+1)
    case 2:
        print(2+3)
    case 3:
        print(3+2)
    case _:
        print("Wrong Data")

print("================ 1 2 3 4 5...10 =================")

for i in range(1,11,1):
    print(i)

print("==================2,4,6,8, ======================")

for j in range(2,10,2):
    print(j)

print("===============1,2,3,4......10  ================")

num=1
while num<=10:
    print(num)
    num+=1

print("=================2 4 6 8 ......20 ================")

i=2
while i<=20:
    print(i)
    i+=2




