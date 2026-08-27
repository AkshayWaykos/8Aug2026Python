print("==========Non static Method==============")

class Student():
    def FirstMethod(self):
        print("Student Name is Akshay")
        print("Student Rollno is 101")
    def SecondMethod(self):
        mark=40
        if mark >= 35:
            print("PASS")
        else:
            print("FAIL")
S1=Student()
S1.FirstMethod()
S1.SecondMethod()

class collage():
    def All_Details(self):
        print("Collage class")

C1=collage()
C1.All_Details()

