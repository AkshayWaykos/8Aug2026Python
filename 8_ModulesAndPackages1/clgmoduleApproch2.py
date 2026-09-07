
#Call the function and method with the help of their module name
#APPROACH 2 :--->

from clg1module import student1,student2,Clg1

student1("Kiyansh",3)
print("--------------------")
student2("Kashi",1)
print("--------------------")
Clg1.student3("Riyansh",2)
print("--------------------")
Clg1.student()
print("--------------------")

print("==============================================")

from clg2module import Clg2,student1,student2

student1("Ramesh",32)
print("--------------------")
student2("Suresh",36)
print("--------------------")
Clg2.student3("Ganesh",34)
print("--------------------")
Clg2.student()
print("==============================================")