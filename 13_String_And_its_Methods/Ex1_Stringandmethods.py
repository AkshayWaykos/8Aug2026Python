print("========string and its methods==========")

s1="velocity"
s2="ABCD"
s3="abcd"
s4=" hi "
s5="my name is abc"
s6="abcaba"
print(len(s1))                       #s1.length()
print(s1.upper())                    #s1.toUpperCase()
print(s2.lower())                    #s1.toLowerCase()
print("--------")
print(s2==s3)                        #s2.equals(s3)
print(s2.__eq__(s3))                 #alternate approach
print(s2.lower()==s3.lower())        #s2.equalsIgnoreCase(s3)
print("--------")
print("vel" in s1)                   #s1.contains("vel")
print(s1.__contains__("vel"))        #Alternate
print(s1.startswith("vel"))          #s1.startswith("vel")
print(s1.endswith("ty"))             #s1.endswith("ty")
print("-------------")
print(s1[0])                         #chatAt(Index)
print(s1[2:4])                       #substring
print(s6.find("b"))                  #1   indexOf(char)
print(s6.rfind("b"))                 #4   lastIndexOf(char)
print(s6.index("b"))                 #1   Alternate   -> this is for string & lists
print("----------")
print(s2+s3)                         #s2.concat(s3)
print(s4.strip())                    #s4.trim()
print(s4.lstrip())                   #Additional trim only left
print(s4.rstrip())                   #Additional trim only right
print(s5.replace("abc","xyz"))       #s5.replace("oldChar","newChar")
ls=s5.split(" ")                     #s5.split(" ")
print(ls)

print("---------------Additional Methods-----------------------")

str1="velocity"
str2="my name is abc"
str3="Abcd"

print(str1.capitalize())       #Capitalizes the first letter of the string.
print(str2.title())            #Converts the first character of each word to uppercase.
print(str3.swapcase())

print("----------")
str4="122"
str5="abc123"
str6="   "
str7="my name is abc my"
print(str1.isalpha())
print(str4.isdigit())
print(str5.isalnum())
print(str6.isspace())
print(str7.count("my"))
print(str5.partition("abc123"))
print("122".zfill(6))
print("velocity".center(3))