print("================Test 1====================")
from ModulesAndPackages2 import Test1

Test1.add(20,20)
Test1.mul(30,40)

i1=Test1.Info1()
i1.method1(20,10)

print("=================Test 2===================")

from ModulesAndPackages2 import Test2

Test2.student1()
Test2.student2()

t2=Test2.Info2()
t2.xyz()

print("===============Test 3=====================")

from ModulesAndPackages2 import Test3

Test3.abc1()
Test3.abc2()
print("-------")

Test3.Info3.m1(20,20)
Test3.Info3.m2()

print("===============Test 4=====================")

from ModulesAndPackages2 import Test4

Test4.fun1()
Test4.fun2(20,20)

D2= Test4.Demo2(20,20)
D2.mul()

Test4.Demo2.div(30,3)

print("===============Functions Program=================")

from Functionsprogram import  Exp1_Function_WithoutParameter

Exp1_Function_WithoutParameter.Func1()
Exp1_Function_WithoutParameterun.Additions()
Exp1_Function_WithoutParameterun.Addition()
Exp1_Function_WithoutParameterun.multiplication()


