
print("============Approach 1===================")

#Call the function and method with the help of their module name
#APPROACH 1 :--->

import clg1module
import clg2module

clg1module.student1("Akshay",31)     #func with Param
print("--------------------")
clg1module.student2("Sagar",29)     #func with Param
print("--------------------")
clg1module.Clg1.student3("Shiva",35)  #static method with param
print("--------------------")
clg1module.Clg1.student()                         #static method with Param

print("==============================================")

clg2module.student1("Rahul",35)
print("--------------------")
clg2module.student2("Pratick",33)
print("--------------------")
clg2module.Clg2.student3("Trupti",28) #static method with Param with same name in both module
print("--------------------")
clg2module.Clg2.student()    #static method without Param with same name in both module

