print("=====Ex5_MethodOverriding===")

class Father:
    def car(self):
        print("Father car=nano")
class son1(Father):
    def car(self):
        print("Son car = BMW")

s1=son1()
s1.car()
print("=====Ex5_MethodOverriding with super()===")

class Father1:
    def car(self):
        print("Father car=nano")
class son11(Father):
    def car(self):
        print("Son car = BMW")
        super().car()

s1=son11()
s1.car()

