from Functionsprogram.Exp9_Function_WithMultipleReturnType import arithmaticoperation2

print("======Global , Local , Class Variable with Diff Name =======")

a=10                             #Global Variable
b=20                             #Global Variable

class Sample1():
    x=30                            #Class Variable
    y=40                            #Class Variable
    def arithmaticOpe1(self):
        p=50                        #Local Variable
        q=60                        #Local Variable
        print("Global Variable =", globals()['a'] + globals()['b'])
        print("Local Variable =",p+q)
        print("Class Variable =",self.x + self.y)

    @staticmethod
    def arithmatiOpe2():
        s = 70                    #Local Variable
        t = 80                    #Local Variable
        print("Global variable =", a * b)               #Calling Global Variable
        print("Local Variable =", s * t)                #Calling Local Variable
        print("Class Variable =", Sample1.x * Sample1.y)#Calling Class Variable

S1=Sample1()
S1.arithmaticOpe1()

print("----------------------")

Sample1.arithmatiOpe2()
