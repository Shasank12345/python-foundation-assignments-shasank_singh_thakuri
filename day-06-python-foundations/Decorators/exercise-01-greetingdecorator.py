

""" A decorator that uppercases and prints "!!!" afer whatever the wrapped function prints """
def shout(func):
    def wrapper(*args,**kwargs):
        new_args=(arg.upper() if isinstance(arg,str) else arg for arg in args)
        new_kwargs={key:val.upper() if isinstance(val,str) else val for key,val in kwargs.items()}
        print("Greetings")
        result=func(*new_args,**new_kwargs)
        print("!!!")
        return result
    return wrapper
@shout
def say_hi(name):
    print(f"Hello {name}")

say_hi("Ram")


