'''Implementation of While loop
Program to allow three retry attempts using while loop'''


secret_word="python"
attempt = 1
max_attempt = 3
operation_sucessful= False
hint='''\nThis is the Programming Launguage 
This word is named after a snake 
it starts with letter "p" '''

print("Lets Play,Guess the secret word! You have 3 tries.")
print(f'''Your hint is given below :-{hint}''')


while attempt <=max_attempt:
    print(f"Attempt: {attempt}")
    guess=input(f"Guess the word .......\n")

    if guess.lower()==secret_word:
        operation_sucessful=True
    if operation_sucessful:
        break

    attempt +=1

if operation_sucessful:
    print("Operation completed Sucessfully , You guessed the word correctly")
else:
    print("Operarion failed , You ran out of attempt")




