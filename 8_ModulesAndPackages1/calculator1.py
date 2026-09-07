#print("===========Calculator 1============")
#Module 1

def add(num1,num2):
    addition=num1+num2
    print("Addition=",addition)

def mul(num1,num2):
    multiplication=num1*num2
    print("Multiplication=",multiplication)

class Sample1:
    def m1(self):
        print("Running m1 method from sample1 class")      #non-static method

    @staticmethod
    def m2():
        print("Running m2 method from sample2 class")     #Static method
