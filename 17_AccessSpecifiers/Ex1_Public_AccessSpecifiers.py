print("=====PUBLIC ACCESS SPECIFIERS ==================")

class Sample:
    name="Akshay"

    def info(self):
        print("Student Details =",self.name)

S=Sample()
S.info()
print(S.name)


print("====================================================")

class Sample2:
    i=10
    j=20

    def add(self):
        print("Addition =", self.i+self.j)

s2=Sample2()
s2.add()
print(s2.i)
print(s2.j)

print("====================================================")