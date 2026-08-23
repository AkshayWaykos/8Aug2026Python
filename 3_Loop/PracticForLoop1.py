print("==============For loop=====================")
for num in range(1,21,):
    print(num) #print from 10 to 20
print("==============For loop=====================")
for i in range(1,11,1):
    print(i )      #print from 1 to 10
print("==============For loop=====================")

for j in range(10,0,-1):
    print(j )     #print from 10 to 1   and end=" " -->is use to print the number in 1 line.
print("==============For loop=====================")
for k in range(1,10,1):
    print(f"{k}+1 = ",{k+1})
print("==============For loop=====================")
fruits = ["Apple" , "Mango" , "Banan"]

for fruit in fruits:
    print(f"My favorite fruit is {fruit}")
print("==============EvenNumber print====================")

for num in range(1,21):
    if num % 2==0:
        print(f"Even number ={num}")  #from even number will print 2,4,...20

print("==============Odd Number print====================")
for num in range(1,21):
    if num % 2 !=0:
        print(f"Odd number ={num}")
print("==============Even and Odd Number print====================")

for i in range (1,21):
    if i % 2==0:
        print(f"Even number = {i}")
    else:
        print(f"Odd numner = {i}")
print("==============For loop end====================")

for i in range(1,6):
    print("*" * i )
print("==============For loop pattern====================")
for j in range(1,6):
    print(  "#" * j )
print("==============For loop Max no ====================")
nums = [10, 45, 2, 89, 33]
max_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num
print("Sabse bada:", max_num)
print("==============For loop 5 to 50====================")
for j in range(5,51,5):
    print( j )
print("==============For loop 6 to 60====================")
for j in range(1,11):
    print(j*6 )
print("==============For loop end====================")
for j in range(5,11):
    print(j*j )

print("==============For loop end====================")
for i in range(1,6):
    print("HI "*i)
print("==============For loop end====================")
for h in range(5,0,-1):
    print(h)
print("==============For loop end====================")
for A in range(1, 5 ,1):
    print("Akshay " * A)
print("==============For loop end====================")


