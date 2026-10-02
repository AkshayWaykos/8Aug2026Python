import time

print("=======if==========")
mark=40
if mark>=35:
    print("Result = Pass")

print("=======if else==========")
mark=20
if mark>=35:
    print("Result=PASS")
else:
    print("Result= FAIL")
print("=======elif if==========")

shoppingAmt=1000
if shoppingAmt>=5000:
    print("50% Off")
elif shoppingAmt>=4000:
    print("40% Off")
elif shoppingAmt>=3000:
    print("30% Off")
else:
    print("No Off")
print("=======Nested if==========")

age=int(input("Enter Age ="))

if age>=18:
    print("According to Age U R Eligible for BD")
    time.sleep(3)
    print("Check Body weight")

    weight=int(input("Enter weight="))
    if weight>=50:
        print("Congratulation U R Eligible for BD")
    else:
        print("According to weight U R not Eligible for BD")
else:
    print("According to Age U R not eligible")

print("=======Match Case==========")

inpute=2

match inpute:
    case 1:
        print("First Class")
    case 2:
        print("Second Class")
    case 3:
        print("3rd class")
    case _:
        print("wrong Inpute")















