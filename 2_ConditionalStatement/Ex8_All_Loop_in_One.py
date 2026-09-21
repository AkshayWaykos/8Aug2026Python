print("=======if else=========")

str="Sagar"
if str=="Sagar":
    print("This is proper Name")
else:
    print("This is wrong name")

print("=======elif================")
makr =100

if makr>=90:
    print("Grade A")
elif mark>=75:
    print("Grade B")
elif mark >=50:
    print("Grade C")
else:
    print("Fail")
print("=======Nester If================")

num=20
if num > 0:
    if num % 2 !=0:
        print("Positive Odd=",num)
    else:
        print("Positive Even =",num)
else:
    print("Number is not positive")

print("==============================")

username=input("Enter Username=")

if username == "Ce3219":
    print("User Name proper & now enter paasword")
    password=input("Enter password=")
    if password=="1234":
        print("Login Success")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")
print("==============================")
