print("=======Methods=========")
s1="akshay"
s2="AKSHAY"
s3='0123456789'
s4="my name is akshay"
s5="abcabc"
s6="hi"

print(s1.upper())
print(s1.islower())
print(s2.lower())
print(s2.isupper())

print(s4.split())
print(s4.capitalize())
print(s2.swapcase())
print(s5.title())
print(s4.replace("akshay","Sagar"))

print(s6.strip())
print(s6.lstrip())
print(s6.rstrip())

print(s1.__eq__(s2))
print(s1.__contains__("hay"))
print(s1.__add__("101"))
print(s1.__len__())
print(s1.startswith("aksh"))
print(s1.endswith("hay"))

print(s1.index("a"))
print(s1.find("k"))
print(s1.join(s6))

print(s1.count("y"))
print(s1.rindex("s"))
print(s1.isalpha())
print(s3.isdigit())
print(s3.isdecimal())

print("===========================")

