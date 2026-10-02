print("======String Methods==================")
# len()
# lower()
# upper()
# islower()
# isupper()
# capitalize()
# title()
# strip()
# lstrip()
# rstrip()
# split()
# isalnum()
# isalpha()
# isdigit()
#isdecimal()
# startswith()
# endswith()
# replace()
# find()
# index()
# count()
# join()


s1="AKSHAYwaykos"
s2=" my name is sagar "
s3="Akki"
s4="12"

print(len(s2))
print(s1.lower())
print(s1.upper())
print(s1.islower())
print(s1.isupper())

print(s2.capitalize())     #start latter cap
print(s2.title())         #first latter cap
print(s2.strip())         #remove space from both side
print(s2.lstrip())        #remove space from left side
print(s2.rstrip())        #remove space from right side

print(s2.split())        #split all word

print(s1.isalnum())      #if alphanumeric than PASS both will all(space not allow)
print(s1.isalpha())
print(s1.isdigit())
print(s1.isdecimal())

print(s2.startswith(" my"))
print(s2.endswith("sagar "))

print(s2.replace("sagar","akki"))

print(s2.find("sagar"))
print(s2.count("is",4))
print(s1.index("S"))        #s1="AKSHAYwaykos"

print(s1.__eq__(s2))

print(s3.join(s4))

