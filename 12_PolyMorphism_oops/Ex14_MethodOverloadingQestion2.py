# Q ) Create a class Student with a method show.
# If you give 1 argument show("Aman") -> it should print Name = Aman
# If you give 2 arguments show("Aman", 20) -> it should print Name = Aman, Age = 20


class Student:
    def show(self,name="   ",Age=" "):
        print("Student Name =",name)
        print("Student Age =",Age)

s=Student()
s.show("Aman",31)

print("=================================")

class Student:
    def show(self, name, age=None):
        if age == None:
            print("Name =", name)
        else:
            print("Name =", name, ", Age =", age)

s = Student()
s.show("Aman")
s.show("Aman", 31)