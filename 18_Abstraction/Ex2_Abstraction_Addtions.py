from abc import ABC,abstractmethod

class Operation(ABC):
    i=10
    j=20
    @abstractmethod
    def addition(self):
        pass

    @abstractmethod
    def multiplication(self):
        pass

class Login(Operation):
    def addition(self):
        print("Addition=",self.i+self.j)

    def multiplication(self):
        print("Multiplication=",self.i*self.j)

L=Login()
L.addition()
L.multiplication()