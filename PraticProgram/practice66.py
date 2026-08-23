import time

print("===========DataType===================")
Age = 31                          #integer
Name = "Akki"                     #string
CTC = 8.0                         #Float
working='true'                      #boolean
FevMon=(10,11,1,4,7)                #tuple
dependency = [1, 'son']             #list
responsibility = {"mother" : "Sita", "Age": 60 }  #dict
fevnum={7,3,9,8,7,}                  #set

print(Age)
print(Name)
print(CTC)
print(working)

print(FevMon)
print(dependency)
print(responsibility)
print(fevnum)
print("===========if else===================")
Dmart=499

if Dmart>=500:
    print("AAA ")
else:
    print("BBB")
print("===========if elif===================")
shoppintAMT=2999
if shoppintAMT>=5000:
    print("50% off")
elif shoppintAMT>=4000:
    print("40% off")
elif shoppintAMT>=3000:
    print("30% Off")
else:
    print("No discount")
print("===========Nester if===================")

UserName="Akshay"

if UserName=="Akshay":
    print("User Name Proper =" , UserName)
    print("Enter Password")
    time.sleep(1)
    password="Waykos"
    if password=="Waykos":
        print("Proper Password = ", password)
        print("Welcome in Application")
    else:
        print("Wrong Password")
else:
    print("wrong user name")
print("==========Match Case statement==================")
input=1
match input:
    case 1:
        print("Addition = ", 20+20)
    case 2:
        print("Multiplication = ", 20*20)
    case 3:
        print("No Operation")
print("==========for Loop==================")

for i in range(1,11):
    print(i)
    i+=1

print("==========while Loop==================")
i=1
while i<=10:
     print(i)
     i+=1
print("==========End=================")








