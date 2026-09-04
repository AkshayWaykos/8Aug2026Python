print("======Global , local ,class variable with Diff Name ===========")

i=20

class Sample1:
    j=30
    def method1(self):
        k=40
        print("Local Variable =",k)
        print("Global Variable=",i)
        print("class Variable =",self.j)
s1=Sample1()
s1.method1()

print("======Global , local ,class variable with Same Name ===========")

a=10
class Sample2:
    a=20
    def method2(self):
        a=30
        print("Local Variable =",a)
        print("Class Variable =",self.a)
        print("global variable =",globals()['a'])
s2=Sample2()
s2.method2()

print("======END===========")