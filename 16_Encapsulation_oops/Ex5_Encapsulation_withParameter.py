class Sample:
    def __init__(self,__num1,__num2,__num3):
        self.__num1=__num1
        self.__num2=__num2
        self.__num3=__num3

    def addition(self):
        add=self.__num1+self.__num2+self.__num3
        print("Addition = ",add)

    def multiplication(self):
        mul = self.__num1 * self.__num2 * self.__num3
        print("Multiplication = ", mul)

S=Sample(20,20,20)
S.addition()
S.multiplication()