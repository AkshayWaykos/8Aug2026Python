#Module

def add():
    a=10
    b=20
    print("Addition =",a+b)

class Sample11:
    def method(self):
        print("Non-Static method 11 run from Sample 11 (module1)")

    @staticmethod
    def method22():
        print("Static method 22 run from Sample 11 (module1)")

