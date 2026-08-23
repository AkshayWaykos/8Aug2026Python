for i in range(10,0,-1):
    print(i)
    #i+=1
print("=======================")
for j in range(1,11):
    print(j)
    #j+=1
print("=======================")
for k in range(2,21,2):
    print(k)
print("=======================")
i=2

while i<=10:
    print(i)
    i+=1
print("=======================")
i=5
while i>=0:
    print(i)
    i-=1
print("=======================")

prelim=300
if prelim>=250:
    print("Selected in prelim")
    print("Prepared for mains exam")
    mains=300
    if mains>=350:
        print("Selected in Mains Exam")
    else:
        print("Not selected in Mains Exam")
else:
    print("Not selected prelim")
print("=======================")
mark =31
if mark>=65:
    print("Distinction")
elif mark>=60 and mark<65:
    print("Class With A Grade")
elif mark>=50 and mark<60:
    print("Class with B grade")
elif mark>=35 and mark<50:
    print("Class with C Grade")
elif mark<35:
    print("Fail")
print("=======================")

action="sub"

match action:
    case "add":
        print("Addition of no =",20+10)
    case "sub":
        print("Subtraction of no=",20-20)
    case "Div":
        print("Division of no =",20/10)
    case _:
        print("wrong input")
print("=======================")

input=2
match input:
    case 1:
        print("Addition =",20+10)
    case 2:
        print("Substraction =",20-10)
    case _:
        print("wrong input")
print("=======================")

number=4

print(number , "is Even no" if number % 2== 0 else "odd")

print("=======================")

number=2
print(number ,"id Odd no" if number % 3==0 else "Even")

print("=======================")

input=10

match input:
    case 10:
        print("Addition =",10+20)
print("=====================")

str="Akshay"
print("Name is =",str if str=="Akshay" else "wrong name")






















