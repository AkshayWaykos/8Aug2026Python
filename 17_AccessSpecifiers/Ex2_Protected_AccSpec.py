
class Demo1:
    _name="Akshay"           #protected -> access specifier

    def _info(self):         #protected -> access specifier
        print("Details =",self._name)

class Demo2(Demo1):
    def show(self):
        print("Detailss=",self._name)

d2=Demo2()
d2.show()


print("===========================================")

class Father:
    _car="BMW"

    def _fatherproperty(self):
        print("Father Details =",self._car)
class son(Father):
    def showproperty(self):
        print("Son Details =",self._car)

s=son()
s.showproperty()


