'''Decorator that measures and prints how long the wrapped function took to run'''

import functools as f
import time

'''Note : wraps preserve the metadata like __name and __docs__'''
def timer(func):
    @f.wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.perf_counter()
        new_args=(arg.upper() if isinstance(arg,str) else arg for arg in args)
        new_kwargs={key:val.upper() if isinstance(val,str) else val for key,val in kwargs.items()}
        print("="*40)
        result=func(*new_args,**new_kwargs)
        end_time=time.perf_counter()
        wrapper.duration=end_time-start_time
        print("="*40)
        return result
    wrapper.duration=None
    return wrapper


@timer
def greet(name):
    print(f"Hello {name}")

greet("Ram")
print(f"{greet.__name__} exceution time:{greet.duration:.6f}")
        
#without wraps greet.__name__name will return the wrapper (original name is los)