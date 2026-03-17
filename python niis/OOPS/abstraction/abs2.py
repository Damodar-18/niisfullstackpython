from abc import *

class Bank(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def interest(self):
        pass


class SBI(Bank):
    def interest(self):
        print("SBI Interest Rate: 6%")


class HDFC(Bank):
    def interest(self):
        print("HDFC Interest Rate: 7%")


b1 = SBI("State Bank")
b1.interest()

b2 = HDFC("HDFC Bank")
b2.interest()