
print("=======1. Zero Division Error==========")

try:
    print(10/0)
except ZeroDivisionError:
    print("0 se divide nahi hota")

print("===========2. Value Error==============")

try:
    int("abc")
except ValueError:
    print("Value galat hai")

print("=========3. IndexError=============")

try:
    a = [1,2]
    print(a[5])
except IndexError:
    print("Index nahi hai")

print("=========4. KeyError============")
try:
    d = {"a":1}
    print(d["b"])
except KeyError:
    print("Key nahi mila")
print("=========5. File Not Found Error============")

try:
    open("test.txt")
except FileNotFoundError:
    print("File nahi mili")

print("===========6. TypeError ============")

try:
    print("hi" + 5)
except TypeError:
    print("Type galat hai")

print("===========7. NameError============")

try:
    print(x)
except NameError:
    print("Naam define nahi hai")

print("===========8 Ek saath sab handle karna hai to:============")

try:
    print(10/0)
except Exception as e:
    print("Error:", e)

try:
    print(10/0)
except Exception:
    print("Generic Exception")

print("========================================================")

try:
    a = 10 / 0
except:
    print("Error aaya")
finally:
    print("Ye hamesha chalega")

print("========================================================")
age = 15
if age < 18:
    raise ValueError("18+ hona chahiye")

print("========================================================")
