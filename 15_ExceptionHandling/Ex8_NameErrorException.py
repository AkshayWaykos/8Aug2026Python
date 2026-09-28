print("======Name Error Exception========")
str(2345)
#bool=true
#To handle this above Name Error we use Name Error Exception.
try:
    bool=true
    print(bool)
except NameError:
    print("boolean value is wrong==>true not define")

print("==================================")
#print(x)   <--- for this we use Name Error Exception
try:
    print(x)
except NameError:
    print("Name error Exception==>x not define")
print("=====================================")

try:
    print(st)
except NameError:
    print("Name error Exception Handled ==> st not define")
print("=====================================")