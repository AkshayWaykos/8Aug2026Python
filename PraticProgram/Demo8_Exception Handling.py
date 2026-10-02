from sys import base_exec_prefix

print("==Exception Handling==")

class sample:
    def Ex(self):
        try:
            num1=10
            num2=0
            print(num1/num2)
        except ZeroDivisionError:
            print("ZeroDivisionError Exception Handled")
s=sample()
s.Ex()
print("--------------------------------------")
class sample:
    def Ex(self):
        try:
            num1=10
            num2=0
            print(num1/num2)
        except ZeroDivisionError:
            div=num1/5
            print(div)
s=sample()
s.Ex()
print("--------------------------------------")

try:
    num=qwedfg
except NameError as s1:
    print("Handled Name Error Exception")

print("-----------------------------------------")

try:
    int('abc')
except ValueError:
    print("Handle Value Error Exception")


