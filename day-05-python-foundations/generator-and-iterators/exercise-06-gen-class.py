


class Number:
    def __init__(self,limit):
        self.limit=limit
        self.current=0

    def __iter__(self):
        return self

    def __next__(self):
        value=self.current
        self.current+=1
        if self.current>self.limit:
            raise StopIteration
        return value

obj=list(Number(20))
print(f"{obj}")

'''
Behind the Scene :
obj=Number(20)
iterator=obj.__iter__()
while True :
try:
    item=iterator.__next__()
    print(item)
except StopIteration:
    break


'''