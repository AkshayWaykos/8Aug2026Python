#Module 2= Demo2

def sub():                      #function without Parameter
    p=20
    q=10
    sub=p-q
    print("Subtraction =",sub)

def div(no1,no2):               #function with Parameter
    division=no1/no2
    print("Division =",division)

#print("----------Global,local,class Variable with Same name --------")

x=80
class Sample2:
    x=70
    def method2(self):
        x=60
        print("Local Variable=",x)
        print("Global Variable=",globals()['x'])
        print("Class Variable=",self.x)
#print("--------------------------------------------")


