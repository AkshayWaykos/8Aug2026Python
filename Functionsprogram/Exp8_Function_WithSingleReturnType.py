print("================Function with single value return type====================")

def addition(num1,num2):
    num3=num1+num2
    return num3

num4=addition(20,10)
print("Addition of no =",num4)

print("==============================================")

def multiplication(no1,no2):
    mul=no1*no2
    return mul
mul1=multiplication(10,10)
mul2=multiplication(20,20)
mul3=multiplication(10,5)

print("Multiplication of no = ",mul1)
print("Multiplication of no = ",mul2)
print("Multiplication of no = ",mul3)

print("==============================================")

def StudentDetails(Name,Age,Contactno):
    Details =Name,Age,Contactno
    return Details
Info1 =StudentDetails("Akshay",31,7276727847)
Info2 =StudentDetails("Sagar",29,9988776655)
Info3 =StudentDetails("Shiva",35,7788990055)
print(Info1)
print(Info2)
print(Info3)








