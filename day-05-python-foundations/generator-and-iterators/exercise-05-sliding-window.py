

number=[1,2,3,4,5,6,7,8,9,10]
def my_generator(number:list):
    for i in number:
        yield i



prev_value=None
gen=my_generator(number)
current_value=next(gen)
while True:
    try:
        next_value=next(gen)
        print(f'''
        Previous Vlaue is {prev_value}  
        Current value is {current_value}
        Next Value is {next_value}
        ''')
        prev_value=current_value
        current_value=next_value
    except StopIteration:
        print(f"Reached end. Last value was {current_value}")
        break
