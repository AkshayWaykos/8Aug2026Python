print("===Value Error Exception===")

# int('abc')
#To handle Value Error we use Value Error Exception.

try:
    int('abc')
except ValueError:
     print("Value is wrong for int")
print("===================================")

#float('xyz')
#To handle Value Error we use Value Error Exception.
try:
    float('xyz')
except ValueError:
    print("Value is wrong for flot")
print("===================================")

try:
    int('asdfghjk')
except ValueError:
    print("Value wrong for int")

