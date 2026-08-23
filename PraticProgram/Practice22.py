print("=============if statement===================")
shoppingAmt=500

if shoppingAmt>=400:
    print("5% Discount")

print("=============if else statement===================")

shoppingAmt= 600

if shoppingAmt>=500:
    print("10 % Discount")
else:
    print("No discount")

print("=============if elif statement===================")

shoppingAmt=4500

if shoppingAmt>=8000:
    print("15% Discount")
elif shoppingAmt>=7000:
    print("12% Discount")
elif shoppingAmt >=4000:
    print("10% discount")
elif shoppingAmt >=3000:
    print("8% Discount")
else:
    print("No Discount")


print("=============Nested statement===================")

PRM=251

if PRM>=250:
    print("Selected for Prelim")
    print("Prepared for Mains ")

    Mains=350

    if Mains>=400:
        print("Selected for Mains")
    else:
        print("Rejected from Mains")

else:
    print("Rejected from Prelim")

print("================================")

UserName="Akshay"

if UserName=="Akshay":
    print("Username is proper")
    print("Enter Password")

    Password="Waykos"
    if Password=="Waykos":
        print("Password is Proper")
        print("Login Successfully")
    else:
        print("You Enter Wrong Password")
else:
    print("You Enter Wrong User Name")

print("==============Match  Case==================")

Num=9

match 9:
     case 1:
         print("Suday")
     case 2:
         print("Monday")
     case _:
         print("Wrong Input")