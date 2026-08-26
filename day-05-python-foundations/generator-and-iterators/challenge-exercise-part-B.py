'''
INFINITE GENERATOR WITH HELPER

'''




def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b


def take(gen,a:int)->list:
     
     count=0
     fibo_list=[]
    

     while count<a:
        fibo_list.append(next(gen))
        count+=1
    

     return fibo_list
n=int(input("Enter the limit up to which you want to print the fibonacci series"))

fibo_list=take(fibonacci(),n)
print(fibo_list)    
    