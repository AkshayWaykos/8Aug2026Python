print("=========Zero Division Error Exception===========")

n1=10
n2=0
try:
    print(n1/n2)
except ZeroDivisionError:
    print("Division of n1 & n2 =",n1/2)
    print("ZeroDivisionError Handle")

print("==========Multiple exception way===============")
try:
    num1=10
    num2=0
    print(num1/num2)
except ValueError:
    print("Value Error Exception handled")
except NameError:
    print("Name Error Handled")
except TypeError:
    print("Type Error Handling")
except ZeroDivisionError as s1:
    print(s1)
    print(num1/5)
    print("Zero Division Error Exception")
except Exception:
    print("Generic Exception Handled")

print("==========Multiple exception way===============")


























