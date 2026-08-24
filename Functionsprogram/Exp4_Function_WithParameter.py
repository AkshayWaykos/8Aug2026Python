print("==========Function with Parameter================")

def Addition(num1,num2):
    sum=num1+num2
    print("Addtion of 2 no =" ,sum)
Addition(20,20)
Addition(30,20)
print("=============Sub of 2 no========================")

def Substraction(num1,num2):
    Sub=num1-num2
    print("Substractio od 2 no =" ,Sub)

Substraction(20,10)
Substraction(30,20)

print("=============Mul of 2 no========================")

def Multiplication(mul1,mul2):
    mul=mul1*mul2
    print("Multiplication of 2 no =",mul)
Multiplication(20,10)
Multiplication(10,10)
print("=============StudentInfo print=======================")

def StudentInfo(Name,Age,Rollno,Mobile,City):
    print("Student Name =" , Name)
    print("Student Age =" , Age)
    print("Student Rollno =" , Rollno)
    print("Student Mobile =" , Mobile)
    print("Student CityName =" , City)

StudentInfo("Akshay",31,101,7276727847,"Hyderbad")
print("-----------------------")
StudentInfo("Sagar",29,102,7276729040,"Pune")

print("=============Square print=======================")

def square(num):
    print("Square of no = ", num * num)

square(10)
square(4)
square(7)
print("=================Addition=====================")

def addno(a,b):
    print("Addition =" ,a + b)

addno(5,3)
print("===============check_even_odd(n) with Param- for=======================")

def check_even_odd(n):
    for i in range(1,n+1):
            if i % 2==0:
                print("No Is Even =" ,i)
            else:
                print("no Is Odd = ", i)
check_even_odd(5)
print("===============check_even_odd(n) with Param -while=======================")

def check_even_odd(n):
    i=1
    while i<=n:
        if i % 2 == 0:
            print("No is Even =" ,i)
        else:
            print("No is Odd =" , i)
        i+=1
check_even_odd(10)










