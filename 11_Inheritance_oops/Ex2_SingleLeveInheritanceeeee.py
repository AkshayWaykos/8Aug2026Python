print("===Single Level Inheritance==========")

class Student1:
    def science(self):
        print("Science Subject")
    def match(self):
        print("Match Subject")
    def history(self):
        print("History subject")

class Student2(Student1):
    def geography(self):
        print("Geography Subject")
    def english(self):
        print("English Subject")

    @staticmethod
    def subject():
        print("==Subject Details==")

s2=Student2()
s2.science()
s2.match()
s2.history()
print("-------------")
s2.geography()
s2.english()
