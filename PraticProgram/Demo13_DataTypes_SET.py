print("======Set Data Type==========")

set={11,11,12,13,'AA',11.10,'B+',66,77,88}
see={22,22,44,11,55,66,99}

aa={11,2,4,5,5,67,'ABC'}

print(set.__len__())  #length if set

set.pop()
print(set)

se=set.copy()
print(se)

se.remove(88)
print(se)

se.add('SSS')
print(se)

sorted_set=sorted(see)
print(sorted_set)

set=list(aa)
print(type(set))
print(set)