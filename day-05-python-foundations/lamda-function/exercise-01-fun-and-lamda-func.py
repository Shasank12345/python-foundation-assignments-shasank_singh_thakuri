

#with lamda
triple=lambda n:n*3


#actual function:

def trip(n:int)->int:
    return n*3

print(f'''function : {trip(7)}
lambda function : {triple(7)}
''')


'''
Both serves diffrent engineering tradeoff
    -We use Lamda when we need a quick one-line action directly
     inside another tool, like a sorting a list ,
    -We choose function when our code need complex structure type hint 
     and we need to reuse it multiple times
'''