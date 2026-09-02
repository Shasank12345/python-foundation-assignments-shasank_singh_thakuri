'''Stacking in Decorator'''

import functools as f
import time
import logging 
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
def timer(func):
    @f.wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.perf_counter()
        result=func(*args,**kwargs)
        end_time=time.perf_counter()
        duration=end_time-start_time
        logger.info(f"{func.__name__} took {duration:.6f}")
        return result
    return wrapper 

def log_calls(func):
    @f.wraps(func)
    def wrapper(*args,**kwargs):
        logger.info(f"Calling {func.__name__} with args :{args} and kwargs :{kwargs}")
        return func(*args,*kwargs)
    return wrapper
# case I
"""timer wrapper exceutes first
    then log_calls wrapper starts
    log_calls wrapper ends 
    timer wrapper ends
"""
@timer
@log_calls
def greet(name):
    print(f"Hello {name}")

greet("Elon Mask")


# CASE II
print('CASE II .................')

'''Log call wrapper starts
    timer wrapper starts,
    timer wrapper ends,
    log_call wrapper starts'''
@log_calls
@timer
def greet(name):
    print(f"Hello {name}")

greet("Elon Mask")


'''
note : decorator is just like passing function inside the function
in case II
its like
log_calls(timer(greet))
in case I
its like 
timer(log_calls(greet))
IN CASE II the timer ends when log_calls ends
Thats why its exceution time is more for case ii
'''