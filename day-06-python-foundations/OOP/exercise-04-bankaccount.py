'''Class BankAccount with private variable demonstrattion'''
#exceptions
class NegativeBalanceError(Exception):
    '''EXCEPTION IS RAISED IF BALANCE IS NEGATIVE'''

class InsufficentBalance(Exception): #OVERDRAFT
    '''Raises when user tries to withdraw money more that his balance'''


class BankAccount:
    def __init__(self,amount:float):
        self.balance=amount

    @property
    def balance(self)->float:
        return self._balance
    
    @balance.setter
    def balance(self,amount)->None:
        if amount<0:
            raise NegativeBalanceError("Balance can't be in Negative ")
        self._balance=amount

    def withdraw(self,amount:float)->None:
        if self._balance<amount:
            raise InsufficentBalance('Overdraft is not permitted.Insufficent Balance to perfrom certain action')
        self.balance-=amount
        print(f"{amount} is sucessfully withdrawed from your account.Your CurrentBalance is {self._balance}")
    def deposit(self,amount:float)->None:
        self.balance+=amount
        print(f"{amount} is sucessfully deposited to your account.Your CurrentBalance is {self._balance}")
        
try:
    x=float(input("Enter the Balance you want to deposit as initial Balance"))
    A1=BankAccount(x)
    y=float(input("Enter the Amount you want to Withdraw"))
    A1.withdraw(y)
    z=float(input("Enter the Amount you want to deposit"))
    A1.deposit(z)
except NegativeBalanceError as e:
    print(f"Exception Occured: {e}")
except InsufficentBalance as e:
    print(f"Exception Occured: {e}")


