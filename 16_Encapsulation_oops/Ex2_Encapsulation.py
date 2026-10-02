

class Demo1:

    def __init__(self,__num1,__num2,__num3):
        self.__num1=__num1
        self.__num2=__num2
        self.__num3=__num3

    def add(self):
        addition=self.__num1+self.__num2+self.__num3
        print("Addition = ",addition)


    def mul(self):
        multiplication=self.__num1*self.__num2
        print("Multiplication =",multiplication)

    def squareOfNum(self):
        Square=self.__num1*self.__num2
        print("Square of no=",Square)

d1=Demo1(10,10,10)
d1.add()
d1.mul()
d1.squareOfNum()
