
#calculate simple interest (default argument concept)
def calculate_simple_interest(principal,rate=5,time=1):
    return (principal*rate*time)/100


print(f'''
The Simple interest with all argument given is {calculate_simple_interest(1000,10,2):.3f} 
The Simple interest with principal only given using default rate and time is {calculate_simple_interest(1000):.3f}  
The Simple interest with deafult rate is {calculate_simple_interest(2000,time=3):.3f} 
''') 