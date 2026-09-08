
print("=======Single Level Inheritance=========")

#1 super class -->1 Subclass requested--> subclass Object

class father():
    def car(self):
        print("Car : BMW")

    def money(self):
        print("money: 1L")

    def Home(self):
        print("Home : 1BHK")

class son(father):
    def mobile(self):
        print("Mobile: OnePlus")

s1=son()
s1.car()
s1.money()
s1.Home()
s1.mobile()

print("=======Single Level Inheritance=========")

class Brother1:
    def add(self):
        a=10
        b=20
        print("Addition =",a+b)

    def mul(self):
        x = 10
        y = 20
        print("Addition =", x * y)

class Brother2(Brother1):
    def sub(self):
        a = 20
        b = 10
        print("Addition =", a - b)

    def div(self):
        x = 100
        y = 20
        print("Addition =", x / y)

b2=Brother2()
b2.add()
b2.mul()
b2.sub()
b2.div()