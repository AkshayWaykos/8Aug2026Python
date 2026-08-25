from PraticProgram.Nestedif11 import password

print("======================")

mark=40
if mark>=35:
    print("Pass")
print("===========")

mark=34
if mark>=35:
    print("PASS")
else:
    print("Fail")
print("===========")

shoppointAmt=1000

if shoppointAmt>=5000:
    print("40% Off")
elif shoppointAmt>=4000:
    print("30% Off")
elif shoppointAmt>=3000:
    print("20% Off")
else:
    print("No Off")
print("===========")

username="Akshay"
password="Waykos"

if username=="Akshay":
    if password=="Waykos":
        print("Username & Passw is proper")
    else:
        print("Password id wrong")
else:
    print("User Name is wrong")
print("===========")
input =99
match input:
    case 11:
        print("PLAYER no 11")
    case 10:
        print("PLAYER no 10")
    case 9:
        print("PLAYER no 09")
    case 8:
        print("PLAYER no 08")
    case _:
        print("WRING PLAYER no")
print("===========")








