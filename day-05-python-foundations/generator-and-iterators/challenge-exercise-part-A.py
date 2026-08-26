
''''
 MENU DRIVEN STREAMING LOG PROCESSOR 
 WITH CHOICE :
    "1" TO READ ALL LINES IN THE LOG FILE
     "2" TO PARSE THE  LOG
     "3" TO SHOW THE ERROR RECORD ONLY
'''
import re

#Generator to read lines 
def read_lines(path):
    with open(path,'r') as f:
        for line in f:
            yield line.strip('\n')
path='day-05-python-foundations/generator-and-iterators/logs.txt'
#print generator
def read_file(generator):
    print("PROCESSING FILE.............")
    while True:
        try:
            print(next(generator))
        except StopIteration:
            print("NOTHING TO PROCESS..............")
            break
#generator to parse file
def parse_file(path):
    level=['INFO','ERROR','CRITICAL','WARN','DEBUG']
    with open(path,'r') as f:
        log_list=[line.strip('\n') for line in f if line.strip()]
        for item in log_list:
                for field in item.split(' '):
                    if field in level:
                        levels=field
                    elif field.startswith(('USER','user','User')):
                        user=field.split("=",1)[1]
                    elif field.startswith(("ACTION",'action','Action')):
                        action=field.split("=",1)[1]
                    elif re.search(r'\d{4}-\d{2}-\d{2}',field):
                        date=field if field else None
                    elif re.search(r'\d{2}:\d{2}',field):
                        time=field if field else None
                yield {'Date':date,'Time':time,'User':user,'Level':levels,'Action':action}
#generator for error only
def error_only(path):

    errors=[]
    with open(path,'r') as f:
            error=[line.strip('\n') for line in f if line.strip()]
            for item in error:
                if "ERROR" in item.split(' '):
                    errors.append(item)
    yield errors


n=input(''''
ENTER YOUR CHOICE :
    "1" TO READ ALL LINES IN THE LOG FILE
    "2" TO PARSE THE  LOG
    "3" TO SHOW THE ERROR RECORD ONLY
''')

match int(n):
    case 1:
        read=read_lines(path)
        print("CONTENT OF LOG FILE ")
        read_file(read)

    case 2:
        parse=parse_file(path)
        print("THE PARSED RECORD LOOKS LIKE THIS :")
        read_file(parse)
    case 3:
       error=error_only(path)
       print("THE  RECORD  WITH ONLY ERROR :")
       read_file(error)
