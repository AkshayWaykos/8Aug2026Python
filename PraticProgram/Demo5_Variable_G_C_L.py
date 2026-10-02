print("===Global,Local,class with Diff Name Variables =====")

X=100                       #Global V
class Sample1:
    Y=200                  #Class V
    def method1(self):
        Z=300             #Local V
        print("Global Variable =", X)
        print("Class Variable  =", self.Y)
        print("Local Variable  =", Z)

# s1=Sample1()
# s1.method1()

print("===Global,Local,class with Same Name Variables =====")

Num=500
class Sample2:
    Num=600
    def method2(self):
        Num=700
        print("Local Variable =" , Num)
        print("Class Variable =" , self.Num)
        print("Global Variable=" , globals()['Num'])
#
# s2=Sample2()
# s2.method2()