

'''
MINI LOG ANALYZER

'''


with open('day-05-python-foundations/list-dict-set-comprehension/logs.txt', 'r') as f:
    raw_list=[line.strip("\n") for line in f if line.strip()] #gives the list of log lines 


#split the lines into clean list 
def cleaner(line)->list:
    return line.split(' ')

#list of error
error_list=[line for line in raw_list if 'ERROR' in cleaner(line)]
print(f'''
List  of log lines Containing only Errors:
{error_list}
''')

#filter the list and return user only 
def filter_user(line):
    for words in line.split(' '):
        if words.startswith(("USER","user",'User')):
            return words.split("=",1)[1]

#set of unique users
unique_set={filter_user(line) for line in raw_list}
print(f'''
Following is the set of Unique User:
{sorted(unique_set)}
''')

#function that checks if the log line action is login or not
def login_failure(line):

    for words in line.split(' '):
        if words.startswith(('Action','ACTION','action')):
            if words.split("=",1)[1] in ['Login','login','LOGIN']:
                return message(line)
                

#function that returns the user and message as a tuple form the lsit of line containig error and whose action is login
def message(line):
    for words in line.split(' '):
        if words.startswith(('USER','User','user')):
           user =words.split("=", 1)[1]
        elif words.startswith(('msg','MSG','Msg')):
            msg=words.split("=", 1)[1]

    return (user,msg)



login_failure_list=[login_failure(line) for line in error_list]


print(f'''
List of user and message who encountered error during login
{login_failure_list}
''')

         















