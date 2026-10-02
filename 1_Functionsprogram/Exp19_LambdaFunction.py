print("========lamda Function ===========")

add=lambda P,Q:P+Q
print("Addition",add(20,20))

print("========================================")

str=lambda name,surname : name + surname
print(str("Akshay"," Waykos"))

print("========================================")

div=lambda W,X :W/X
print(div(10,5))

print("========================================")

class Demo1:
    sub=lambda self,Z,Y:Z-Y

d1=Demo1()
print("Subtraction = ",d1.sub(10,5))

print("========================================")