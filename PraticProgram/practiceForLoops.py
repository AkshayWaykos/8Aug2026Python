print("=============for loop ====================")
#example = 1
for i in range (1,11):
    print(i)
print("=============")
#example = 2
for i in range (10,0,-1):
    print(i)
print("=============")
#example = 3
for i in range(2,21,2):
    print(i)
print("=============")
for i in range(1,7):
    print("# "*i)
print("=============")
for i in range(6,0,-1):
    print("# "*i)
print("=============")
for i in range(1,11,2):
    print(i)
print("=============")
for i in range(1,10):
    if i % 2 == 0:
        print("Even No = ",i)
    else:
        print("Odd No = ",i)
print("=============")
for i in range (1,10):
    if i % 2 !=0:
        print("Odd no =",i)
    else:
        print("Even no=",i)
print("=============")

num = input("Enter number: ")  # "1234"
reverse_num = num[::-1]        # slicing se ulta
print("Reverse =", reverse_num)

















