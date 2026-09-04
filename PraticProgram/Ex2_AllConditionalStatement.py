import time

print("==========if loop===============")
#If loop
mark=40
if mark>=35:
    print("PASS")
print("==========if else loop===============")
#if_else
mark=40
if mark>=35:
    print("PASS")
else:
    print("Fail")
print("==========if elif loop===============")
shoppingAMT=1000

if shoppingAMT>=5000:
    print("50% Off")
elif shoppingAMT>=4000:
    print("40% Off")
elif shoppingAMT>=3000:
    print("30% Off")
elif shoppingAMT>=2000:
    print("20% Off")
else:
    print("No Off")
print("==========Nester If===============")

age =25
if age >=18:
    print("your eligible for BD according to age criteria")
    print("Check weight Now")
    time.sleep(1)
    weight =60
    if weight>=50:
        print("Congratulation, your eligible for BD")
    else:
        print("According to weight your not eligible")
else:
    print("According to age Your not Eligible")
print("==========Match Case===============")

input=2

match input:
    case 1:
        print("Case 1")
    case 2:
        print("Case 2")
    case 3:
        print("Case 3")
    case _:
        print("wrong input")
print("==========END==============")


















