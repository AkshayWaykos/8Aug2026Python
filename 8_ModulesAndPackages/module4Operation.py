
import module1
import module2
import module3
print("------------------Module 1 Executed------------------------------")

module1.studentinfo("Akshay","Waykos")      #function calling(with param)
module1.addition(20,20)                       #function calling(with param)
module1.loop()                                            #function calling(without param)

A1=module1.Abcd1()                                        #object=module1.className
A1.mul()                                                  #object.methodName(non-static method)

module1.Abcd1.addition()                                  #static method calling
print("------------------Module 2 Executed------------------------------")

module2.fun1()                                           #function calling(without Param)

A2=module2.Abcd2(22,33)                        #parameter pass for Constructor
A2.method1()                                            #object.methodName(non-static method)

module2.Abcd2.method2(40,10)                #moduleName.className,methodName

print("------------------Module 3 Executed------------------------------")

module3.fun2()                                          #function without Parameter

V1=module3.Vari()                                       #object=moduleName.className
V1.fun3()                                               #object.MethodName
V1.method3()                                            #object.MethodName

print("------Module 1,2,3,proper Import in Module 4----------------------")