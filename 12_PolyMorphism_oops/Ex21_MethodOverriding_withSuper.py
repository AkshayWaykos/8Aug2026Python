class Grandfather:
    def car(self):
        print("GrandFather car")
class Father(Grandfather):
    def car(self):
        print("Father Car")
        super().car()
class son(Father):
    def car(self):
        print("Son car")
        super().car()
s=son()
s.car()