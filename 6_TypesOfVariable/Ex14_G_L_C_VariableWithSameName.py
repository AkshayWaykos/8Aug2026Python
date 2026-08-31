print("===All Variable with Same Name and With Parameter ====")
x=10
y=20

class Sample5():
    x=30
    y=40
    @staticmethod
    def method(x,y):
        print("Local Variable =",x+y)
        print("Class variable=",Sample5.x + Sample5.y)
        print("Global Variable =",globals()['x']+globals()['y'])

Sample5.method(50,60)

print("======All Variable with Same Name and With Parameter ====")

a=20
b=20

class Sample6():
    a=30
    b=30
    def method1(self):
        a=40
        b=40
        print("Local Variable =",a+b)
        print("Class Variable =",self.a+self.b)
        print("Global Variable =",globals()['a']+globals()['b'])
S6=Sample6()
S6.method1()
