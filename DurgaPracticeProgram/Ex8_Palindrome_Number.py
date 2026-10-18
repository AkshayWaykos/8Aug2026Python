#First Way

num = 121
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome hai")
else:
    print("Palindrome nahi hai")


print("======================================")
#second Way

num=input("Enter Number =")

if num==num[::-1]:
    print("This is Palindrome No")
else:
    print("This not Palindrome No")

print("=========================================")

num1=input("Enter Number =")

if num1==num1[::-1]:
    print("This is Palindrome No")
else:
    print("This is Not Palindrome No")
print("===========================================")
























