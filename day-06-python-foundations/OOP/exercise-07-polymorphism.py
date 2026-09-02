''' ABstract class'''
from abc import ABC ,abstractmethod

#custom defined exceptions
class AbstractClassError(Exception):
    '''Exception raised when abstract base class is instantiate'''
class NegativeBalanceError(Exception):
    '''Exceptiom raised for negative balance '''
class InsufficentBalance(Exception):
    '''Raised if balance is not Enough'''


class PaymentMethod(ABC):
    '''Abstract base class'''
    def __init__(self,amount):
        self.amount=amount
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,amount):
        if amount<0:
            raise NegativeBalanceError("Balance can't be negative")
        self._amount=amount
    @abstractmethod
    def pay(self,amount):
        ''' Abstract method'''
    


class Esewa(PaymentMethod):
    def pay(self,amount):
        if amount>self.amount:
            raise InsufficentBalance("You don't have sufficent balance to procced ")
        self.amount-=amount
        print(f"Following amount :{amount} is paid from your account.Your Current Balance is {self.amount}")

class MobileBanking(PaymentMethod):
    
    def pay(self,amount):
        if amount>self.amount:
            raise InsufficentBalance("You don't have sufficent balance to procced ")
        self.amount-=amount
        print(f"Following amount :{amount} is paid from your account.Your Current Balance is {self.amount}")


try:
 
 
 esewa=Esewa(500)
 esewa.pay(200)

 mobile=MobileBanking(1000)
 mobile.pay(300)

except InsufficentBalance as e:
    print(f"Exceptiom Occured :{e}")

except NegativeBalanceError as e:
    print(f"Exception Occured :{e}")


try:
    payment = PaymentMethod(100)
    payment.pay(200)
except TypeError as e:
    print(f"Exception Occurred:({e})")
