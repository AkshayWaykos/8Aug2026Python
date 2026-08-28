from uuid import main

print("===========if Statement ==============")
mark=40
if mark>=35:
    print("PASS")
print("===========if else Statement ==============")
mark=20
if mark>=35:
    print("PASS")
else:
    print("FAIL")
print("===========if elif Statement ==============")
mark=25
if mark>=85:
    print("Distinction")
elif mark>=80 and mark<85:
    print("1st class")
elif mark>=70 and mark<80:
    print("2nd class")
elif mark>=60 and mark<70:
    print("3rd class")
elif mark>=35:
    print("only pass")
else:
    print("Fail")

print("===========Nested if Statement ==============")

Prelim=251

if Prelim>=250:
    print("Selected for Prelim")
    print("prepared for mains exam")
    mains=450

    if mains>400:
        print("Selected for Mains Exam")
    else:
        print("Rejected In Main Exam")
else:
    print("Rejected from prelim")
print("==========Match Case Statement ==============")

input=3

match input:
    case 1:
        print("Sachin")
    case 2:
        print("Dhoni")
    case 3:
        print("Raina")
    case 4:
        print("Jadeja")
    case 5:
        print("Bumra")
    case _:
        print("Not a Indian player")
print("==========Condition statement done==============")












