print("======All Variable with Diff Name and Without Parameter=============")

x = 10

class Sample11():
    y = 20
    def method1(self):
        z = 30

        print("Global Variable =", x)
        print("Class Variable =", self.y)  #in static use self for class
        print("Local Variable =", z)

    @staticmethod
    def method2():
        s=40
        print("Global Variable =", x)
        print("Class Variable =", Sample11.y) # in non-static use classname.variable
        print("Local Variable =", s)

S11=Sample11()
S11.method1()
print("---------")

Sample11.method2()
