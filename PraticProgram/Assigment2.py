

print("2: print all the even numbers from 1 to 50")
#First Way -
for i in range(2, 51, 2):
    print("Even no =",i)

print("==============================")
#Second Way -
for i in range(1, 51):
    if i % 2 == 0:
        print("Even no =",i)

print("==============================")
#3rd Way -
for i in range(1,51):
    if i % 2 == 0:
        print("Is Even No =",i)
    else:
        print("Is Odd no=",i)
print("==============================")