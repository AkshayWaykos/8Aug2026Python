
studentName= "Akshay"
age=31

class StudentDetails():
    studentName="Sagar"
    age=29

    def student1(self):
        studentName="Shiva"
        age=34

        print("local Student Details =",studentName,age)
        print("class Student Details =",self.studentName,self.age)
        print("global Student Details =",globals()['studentName'],globals()['age'])

    @staticmethod
    def student2():
        studentName="Sakshi"
        age=26

        print("local Student Details =", studentName, age)
        print("class Student Details =", StudentDetails.studentName, StudentDetails.age)
        print("global Student Details =", globals()['studentName'], globals()['age'])


SD=StudentDetails()
SD.student1()
print("-------------------------")

StudentDetails.student2()