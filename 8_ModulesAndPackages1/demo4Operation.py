
print("====Import All Module 1 and 2 in Module 3======")
#module 3=Demo 3 Operation
import demo1
import demo2
import demo3

print("------From Demo1 Module 1------------")
demo1.add()
demo1.mul(20, 20)
print("------Sample1 class from Demo1------------")
S1=demo1.Sample1()
S1.method1()

print("------From Demo2 Module 2------------")

demo2.sub()
demo2.div(10, 5)
print("------Sample2 class from Demo2------------")
S2=demo2.Sample2()
S2.method2()
print("------From Demo3 Module 3------------")

S3=demo3.Sample3(30, 20)
S3.student()

demo3.Sample3.details("Akshay", 31)

print("------------------END-------------------")





