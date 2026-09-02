""""
Decorator that reruns certain times ,, like marqueee
"""
import functools as f
import time
def retry(times,delay):
    def decorator(func):
        @f.wraps(func)
        def wrapper(*args,**kwargs):
            new_args=list(arg.upper() if isinstance(arg,str) else arg for arg in args)
            new_kwargs={key:(val.upper() if isinstance(val,str) else val )for key,val in kwargs.items()}
            result=None
            for i in range(times):
                print("="*40)
                result=func(*new_args,**new_kwargs)
                print("="*40)
                if i<times-1:
                    time.sleep(delay)                    
            return result
        return wrapper
    return decorator


@retry(times=3,delay=3)
def boardcast(name):
    print(f"This is {name}")


boardcast("Elon Musk")
