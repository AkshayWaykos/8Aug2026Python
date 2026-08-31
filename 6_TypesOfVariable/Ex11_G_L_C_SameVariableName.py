print("===========Same Variable Name Ex2(non static)==================")

x = 10                        # Global V
y = 10                        # Global V
class Test5():
    x = 20                      # Class V
    y = 20                      # Class V
    def fun5(self):
        x = 30                  # Local V
        y = 30                  # Local V
        print("Local Variable = ",x + y)                       # calling Local V
        print("class Variable = ",self.x + self.y)            # calling Class v
        print("Global Variable =",globals()['x'] + globals()['y'])     # calling Global V
t = Test5()
t.fun5()

print("===================================================")
a = 10  # Global V
b = 10  # Global V
class Test6():
    a = 20  # Class V
    b = 20  # Class V
    @staticmethod
    def math():
        a = 30  # Local V
        b = 30  # Local V
        print("Local Variable = ",a*b)
        print("Class Variable = ", Test6.a * Test6.b)
        print("Global Variable =",globals()['a']*globals()['b'])

Test6.math()




