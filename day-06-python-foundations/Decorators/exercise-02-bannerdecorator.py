"""Banner decoratoe that prints a line of = with lenght 40 before and after the wr[apped functions output"""

def Banner(func):
    def wrapper(*args,**kwargs):
        print("="*40)
        result=func(*args,*kwargs)
        print("="*40)
        return result
    
    return wrapper



@Banner
def boardcast(name):
    print(f"........This is {name}........")


boardcast("Elon Musk")