class Demo1:
    def car(self):
        print("car method from Demo1 class")
class Demo2(Demo1):
    def car(self):
        print("car method from Demo2 class")
        super().car()
class Demo3(Demo2):
    def car(self):
        print("car method from Demo3 class")
        super().car()

d3=Demo3()
d3.car()

print("=====================================")

class Sample1:
    def add(self):
        print("Addition=",10+20)
class Sample2(Sample1):
    def add(self):
        print("multplication=",20*20)
        super().add()
class Sample3(Sample2):
    def add(self):
        print("Subtraction=",20-10)
        super().add()

s3=Sample3()
s3.add()
print("=====================================")