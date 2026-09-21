print("========String methods=========")

S1="Akshay"
S2="SAGAR"
S3="shiva"
s4="hi"
s5="My name is Akshay"
s6="abcaba"

print("Length of string =",len(S1))
print("Upper case = ",S1.upper())
print("Lower case = ",S1.lower())

print("----------------------------")

print("S1 equal to S2 =",S1==S2)
print("S1 equal to S2 =",S1.__eq__(S2))
print("s2.equalsIgnoreCase(s3)=",S2.lower()==S3.lower())

print("----------------------------")

print("Aks contains in s1. =","Aks" in S1)
print("Alternate of above=",S1.__contains__("Aks"))
print("String start with=",S1.startswith("Aks"))
print("String End with =",S1.endswith("hay"))

print("----------------------------")

print("Chat At(Index) =",S1[0])
print("substring      =",S1[2:5])
print("indexOf(char) =",S1.find("h"))
print("LastIndexOf(char) =",S1.rindex("y"))
print("this is for string & lists= ",S1.index("s"))

print("----------------------------")

print("s2.concat(s3)=",S1+S2)
print("Strip from both side= ",s4.strip())
print("Additional trim only left=",s4.lstrip())
print("Additional trim only right=",s4.rstrip())
print("Replace the string =",s6.replace("abc","xyz"))
print("----------------------------")
ls=s5.split(" ")
print(ls)   #output=['My', 'name', 'is', 'Akshay']

print("----------------------------")

str1="akshay"
str2="my name is sagar"
str3="Abcd"

print("Capitalizes 1st latter =",str1.capitalize())
print("Converts 1st char cap(each) =",str2.title())
print("swap case(L2H,H2L) = ",str3.swapcase())

print("----------")
str4="122"
str5="abc123"
str6="  "

str7="my name is abc my"
print(str1.isalpha())
print(str4.isdigit())
print(str5.isalnum())
print(str6.isspace())
print(str7.count("my"))
