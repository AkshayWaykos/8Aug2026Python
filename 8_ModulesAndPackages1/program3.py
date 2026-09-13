
print("=====Import program 1 and program 2 module here==============")

import program1

program1.fun1()                       #calling function from module 1
program1.fun2(10,10)      #calling function from module 1

d1=program1.Demo1().method1()         #create object from non-static method from module 1

program1.Demo1().method2(20,20) #calling for static method from module1

print("---------------------------------------------")

import program2

program2.function1()                          #calling function from module 2
program2.function2(30,30)         #calling function from module 2

d2=program2.Demo2().method3()                   #create object for non-static method from module 3

program2.Demo2().method4(20,30)

