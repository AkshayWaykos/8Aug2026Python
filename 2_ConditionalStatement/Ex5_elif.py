from pickletools import markobject

print("============if elif example===================")

# if condition1
# 	if body
# elif condition2
# 	body
# elif condition3
# 	body
# elif condition4
# 	body

shoppingAmt=23000

if shoppingAmt>=20000:
    print(" 20% discount")
elif shoppingAmt>=10000:
    print(" 10% discount")
elif shoppingAmt>=5000:
    print(" 5% discount")
elif shoppingAmt>=1000:
       print(" 0% discount")

print("===============================")


mark=99

if mark>=65:
    print("Distinction")

elif mark>=60 and mark<=65:
    print("Pass with A Grade")

elif mark>=50 and mark<60:
    print("Pass with B Grade")

elif mark>=35 and mark<50:
   print("Pass")
elif mark<35:
    print("Fail")

print("==========================")

EmpName="Akshay"

if EmpName == "Sagar":
    print(" Match With Employee Name")
elif EmpName == "Shiva":
    print(" Match With Employee Name")
elif EmpName == "Sakshi":
    print(" Match With Employee Name")
elif EmpName == "Kiyansh":
    print(" Match With Employee Name")
else:
    print("His not Employee from our company")

print("==========================")

Fruits = "Mango"

if Fruits == "Banana":
    print(" This Fruit is available in stock")
elif Fruits == "Sugarcane":
    print(" This Fruit is available in stock")
elif Fruits == "Pineapple":
    print(" This Fruit is available in stock")
elif Fruits == "DragonFruits":
    print(" This Fruit is available in stock")
else:
    print(" This Fruit is Not available in stock")

print("==========================")