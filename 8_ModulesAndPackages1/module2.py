from pydoc_data.module_docs import module_docs


def fun1():
    print("Function 1 executed form module 2")

class Abcd2:
    def __init__(self,no1,no2):
        print("Multiplication =",no1 * no2)

    def method1(self):
        print("Method 1 Executed from module2 from class")

    @staticmethod
    def method2(no3,no4):
        print("Subtraction =",no3-no4 )



