print("=========Ex 1:Local Variable ===============")

def add():
    num=10
    print("Local Variable =",num+num)
def sub():
    num=20
    print("Local variable =",num-num)
def mul():
    num=30
    print("Local Variable=",num*num)
def div():
    num1=20
    num2=10
    print("Local Variable=",num1/num2)

add()
sub()
mul()
div()
print("=========Ex 2:Local Variable ===============")

def student1():
    name="Akshay"
    print("Student Name =",name)
def student2():
    name="Sagar"
    print("Student2 Name =",name)

class Info():
    def student3(self):
     name="Shiva"
     print("Student3 Name =",name)
    @staticmethod
    def student4():
      name="Sakshi"
      print("Student3 Name =",name)

student1()
student2()

I1=Info()
I1.student3()

Info.student4()

print("=========End===============")





























