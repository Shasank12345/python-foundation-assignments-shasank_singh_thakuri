'''
Dispatch 
'''
class InvalidChoice(Exception):
    '''
    Raised when user enter the wrong choice outside the menu
    '''
    ...

ops={'add':lambda a,b:a+b,
     'mul':lambda a,b:a*b,
     'sub':lambda a,b:a-b}

def calc(ops:dict,a:float,b:float,choice:int):
    try:
        match choice:
            case 1:
                print(f"The addition of the given number is : {ops['add'](a,b)}")
            case 2:
                print(f"The Multiplication of the given number is :{ops['mul'](a,b)}")
            case 3:
                print(f"The Subtraction of the given number is :{ops['sub'](a,b)}")
            case _:
                raise InvalidChoice

    except ...:
        print("Invalid Choice Sorry")
    


print('''
Enter Your Choice:
    1. For addition
    3. For subtraction
    2. For multiplication
''')
choice=int(input())
a=float(input("Enter the first number \n"))
b=float(input("Enter the Second number \n"))
calc(ops,a,b,choice)



'''
The program can be more optimized , as even if the user enters the wrong choice
the value error is raised only after user input the number to perform operation
which is less optimized
'''


