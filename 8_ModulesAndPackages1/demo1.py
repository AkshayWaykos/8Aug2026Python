#Module 1=Demo1

def add():            #function without Parameter
    a=10
    b=20
    print("Addition =", a+b)

def mul(num1,num2): #function with Parameter
    print("Multiplication=",num1*num2)

#print("--------Global,local,class Variable with Diff name -------------")
A=10                                 #Global Variable
class Sample1:
    B=20                             #Class Variable
    def method1(self):
        C=30                        #Local Variable
        print("Local Variable =",C)
        print("Global Variable =",A)
        print("Class Variable =",self.B)

#print("--------------------------------------------")



