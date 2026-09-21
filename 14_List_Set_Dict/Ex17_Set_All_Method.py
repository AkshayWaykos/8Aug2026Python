print("==========Set==========")

se1={11,22,"Akshay",11,22,44,66,"Sagar",'shiva'}

se2={99,77,55,33,11,22,44,66,88,99}

print(se1)

print(se2)

print(len(se1))

print(type(se2))

se1.update(["Amol","Sham"])
print(se1)

se1.remove(22)
print(se1)

se3=se1.copy()
print(se3)

se3.discard(88)
print(se3)

se3.add("Kiaynsh")
print(se3)

print(se3.__contains__("Shiva"))
print(se2.__contains__(99))

se4=list(se2)
print(sorted(se4))



