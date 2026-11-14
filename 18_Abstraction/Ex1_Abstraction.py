from abc import ABC,abstractmethod

class Account(ABC):

    @abstractmethod
    def cashDeposit(self):
        pass

    @abstractmethod
    def cashWithdrawal(self):
        pass

    @abstractmethod
    def balEnquiry(self):
        pass

class SavingAcc(Account):
    def cashDeposit(self):
        print("Cash Deposit Method has been completed")

    def cashWithdrawal(self):
        print("Cash Withdrawal Method has been completed")

    def balEnquiry(self):
        print("Balance Enquiry Method has been completed")


s=SavingAcc()
s.cashDeposit()
s.cashWithdrawal()
s.balEnquiry()