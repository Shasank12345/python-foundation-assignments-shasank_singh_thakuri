class InvalidAgeError(Exception):
    '''Raised when age is less than 0 or greater than 120'''
    pass

def register_user(name:str, age:int)->dict:
    if type(age) is not int:
        raise ValueError(f"Age must be an integer, not {type(age).__name__}")
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Registration of the {name} failed due to age restriction")
    return {"name": name,
            "age": age}


def try_register(name:str, age:int):
    try:
        user_dict = register_user(name, age)
        print(f'''The person named {user_dict['name']} with age {user_dict['age']} is sucessfully registered''')
    except InvalidAgeError as e:
        print(e)
    except ValueError as e:
        print(e)
    finally:
        pass




try_register("Asha",21) #sucess
try_register("Bibek",-5) #InvalidAgeError
try_register("Chandra",'a') #ValueERROR