import functools as f
import logging as log

log.basicConfig(level=log.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = log.getLogger(__name__)

'''Custom Exceptions'''
class NegativeBalance(Exception):
    """Exception occurs if balance is negative."""

class InsufficientBalance(Exception):
    """Exception occurs if the withdrawal amount exceeds available funds."""

class PermissionDenied(PermissionError):
    """Exception occurs if permission is denied."""


'''CLASS BANK ACCOUNT'''
class BankAccount:
    def __init__(self, amount: float = 0.0):
        self.balance = amount

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise NegativeBalance("Balance can't be negative")
        self._balance = float(amount)

    @property
    def is_overdrawn(self) -> bool:
        return self._balance == 0

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self._balance:
            raise InsufficientBalance("Sorry, the required action cannot be performed because of insufficient balance")
        self.balance -= amount
        print(f"The {amount} is withdrawn from the account. Your current Balance is {self._balance}")
        return self._balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount
        print(f"The {amount} is deposited to your account. Your current Balance is {self._balance}")
        return self._balance


'''DECORATORS & ROUTING'''
def requires_role(role: str):
    def decorator(func):
        @f.wraps(func)
        def wrapper(user, *args, **kwargs):
            print("Checking Authorization.......... ")
            if not isinstance(user, dict) or user.get('role') != role:
                log.error(f"{user.get('name')} tries to invoke {func.__name__} and is not permitted")
                raise PermissionDenied(f"{user.get('name')} is not permitted for this specific action. Thank You!")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


def audit_log(func):
    @f.wraps(func)
    def wrapper(user, *args, **kwargs):
        log.info(f"User {user.get('name')} invoked {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(user, *args, **kwargs)
    return wrapper


routes = {}

def route(path: str):
    def decorator(func):
        routes[path] = func
        @f.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


'''BUSINESS LOGIC & DRIVER CODE'''
@route('/transfer')
@audit_log
@requires_role('admin')
def transfer(user: dict, src: BankAccount, dst: BankAccount, amount: float):
    src.withdraw(amount)
    dst.deposit(amount)


admin_user = {"name": "ram", "role": "admin"}
regular_user = {"name": "sita", "role": "user"}

acc_A = BankAccount(500)
acc_B = BankAccount(1000)

# Authorized execution via dictionary lookup
try:
    routes["/transfer"](admin_user, acc_A, acc_B, amount=60)
    log.info(f"Acc A Balance: {acc_A.balance}, Acc B Balance: {acc_B.balance}")
except Exception as e:
    log.error(f"Following exception occurred: {e}")

# Unauthorized execution
try:
    transfer(regular_user, acc_A, acc_B, 50)
except PermissionDenied as e:
    log.info(f"Caught expected error: {e}")