import time

print("=======if statement=======")
mark=40
if mark>=35:
    print("PASS")
print("=====if else statement===")
mark=30
if mark>=35:
    print("PASS")
else:
    print("FAIL")
print("=====if elif statement===")
shoppingAMT=5000
if shoppingAMT>=5000:
    print("50% off")
elif shoppingAMT>=4000:
    print("40% off")
elif shoppingAMT>=3000:
    print("30% off")
elif shoppingAMT>=2000:
    print("20% off")
else:
    print("No Off")
print("=====Nester If statement===")

age=20
if age>=18:
    print("Age is Eligible for BD")
    print("Please check the wight")
    time.sleep(2)
    weight=80
    if weight>=50:
        print("Congratulation U R Eligible for blood donation")
    else:
        print("According to weight your not Eligible for BD")
else:
    print("According to Age your not Eligible for BD")

print("=====match case statement===")

input=2

match input:
    case 1:
        print("Case 1 Executed")
    case 2:
        print("Case 2 Executed")
    case 3:
        print("Case 3 Executed")
    case _:
        print("Wrong input")

print("===Conditional statement End ===")


