print("===Method Overriding With Multi level Inheritance======")
class Father:
    def car(self):
        print("m1 method from Father class")
class son(Father):
    def car(self):
        print("m2 method from son class")
class son1(son):
    def car(self):
        print("m3 method from son1 class")

s1=son1()
s1.car()

