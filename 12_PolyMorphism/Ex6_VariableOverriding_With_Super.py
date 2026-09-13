

print("=======Variable Overriding_With_Super=================")

class student1:
    name="Akshay"

class student2(student1):
    name="AKSHAY"
    print(name)

s2=student2()


print("=======print both parent & class variable using super====")

class parent1:
    name="SAGAR"

class parent2(parent1):
    name="sagar"

    def info2(self):
        print("local variable=",self.name)
        print("Class variable=",super().name)

p2=parent2()
p2.info2()


