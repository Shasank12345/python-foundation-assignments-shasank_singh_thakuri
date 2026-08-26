 

#Generator function
def count_up(n):
    for i in range(1,n+1):
        yield i
n=int(input("Enter the number up to which you want to print \n"))

gen=count_up(n)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
        



