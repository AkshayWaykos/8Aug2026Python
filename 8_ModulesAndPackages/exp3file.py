
print("=============Same Function in Multiple Module ==========")
#Module 1 Call
from exp1file import *               #Approach 2
from exp1file import animal,fly      #Approach 1

animal()
fly()

print("=========================================")
#Module 2 Call

from exp2file import animal,fly
animal()
fly()
