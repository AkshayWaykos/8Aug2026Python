
print("=============import calculator1================")

import calculator1                 #import calculator 1 and calculator
import calculator2

calculator1.add(10,20)        #calling function
calculator1.mul(20,20)

C1=calculator1.Sample1()                  #objectName=moduleName.classname
C1.m1()

calculator1.Sample1.m2()

print("=============import calculator2================")

calculator2.fun1()
calculator2.func2()

C2 = calculator2.Sample2()
C2.m3()

calculator2.Sample2.m4()

print("=============End================")