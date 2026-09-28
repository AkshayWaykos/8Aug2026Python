print("=========Index Error Exception Handled============")
try:
    a=[1,2,5,7,8,9]
    print(a[6])
except IndexError:
    print("Index Error Exception")
print("=========================================")
try:
    b=[2,4,5,6,7,8,'asdf']
    print(b[7])
except IndexError:
    print("Index Error Exception")
print("=========================================")
try:
    t=[11,22,33,'abc']
    print(t[4])
except IndexError:
    print("Index Error Exception")
print("=========================================")
try:
    tuple=[12,23,34,45,'xyz']
    print(tuple[5])
except IndexError:
    print("Index Error Exception")
print("=========================================")