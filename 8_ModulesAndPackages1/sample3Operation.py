print("=========Import Sample 1=============")

import sample1
import sample2

sample1.student("Akshay",31)   #function calling
sample1.info()

d1=sample1.Demo1()                #object creation
d1.method1()                      #non-static method calling

sample1.Demo1.method2()            #static method calling

print("=========Import Sample 2=============")

sample2.Employee("Sagar",29)
sample2.EmpInfo()

d1=sample2.Demo2()
d1.method3()


sample2.Demo2.method4()