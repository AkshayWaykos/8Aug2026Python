print("===========Function with Parameter======================")

def function1(num1,num2):
    num3=num1+num2
    print(num3)
function1(10,20)

print("=========================")

def addition(no1,no2):
    add=no1+no2
    print("Addition of no =",add)

addition(10,10)
addition(10,20)
print("=========================")

def studentInfo(Name,Age):
   print("StudentName =",Name,"  Age =",Age)

studentInfo("Akshay",32)
studentInfo("Sagar",29)

print("=========================")

def substraction(sub1,sub2):
    sub3=sub1-sub2
    print("substraction of no =",sub3)
substraction(20,10)
substraction(30,20)
print("=========================")

def result(mark):
    if mark>=35:
        print("PASS")
    else:
        print("FAIL")
result(30)
print("=========================")

def market(shoppintAmt):
    if shoppintAmt>=5000:
        print("Free delivery")
    else:
        print("No Free Delivery")
market(2000)
market(5000)
market(1000)
market(3000)
market(8000)
print("=========================")




