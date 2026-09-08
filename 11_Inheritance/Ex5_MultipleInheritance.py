
print("============Multiple Inheritance===================")

#Multiple super class and 1 Subclass

class Father:
    def money(self):
        print("Money = 2 L")
    def car(self):
        print("Car = BMW")
    def Home(self):
        print("Home = 2 BHK")

class Mother():
    def money(self):
        print("Money= 1 L")
    def flat(self):
        print("Flat = 1 BHK")

class son(Father,Mother):
    def bike(self):
        print("Bike = KTM")

s1=son()
print("-Father Property------")
s1.money()
s1.car()
s1.Home()
print("-Mother Property------")
s1.money()
s1.flat()
print("-Son Property------")
s1.bike()



