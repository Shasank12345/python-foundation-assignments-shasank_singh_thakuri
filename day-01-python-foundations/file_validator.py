'''Program to Ask the user to enter a file name.
    The program  accepts following format:
        .csv
        .json
        .parquet
    The comparison workS even when the user enters uppercase letters.'''


#input
file_name=input("Enter the file name in format \"file_name.ext\"")

#Calculation
file_name=file_name.lower()
extension=file_name.strip().split(".")[-1] #returns the extension 
acceptable_extension=['csv','json','parquet']
status='Rejected'
for _ in acceptable_extension:
    if(extension==_):
        status="Accepted"
        break


#Output
print(f"Your file extension is {extension}")
print(f"Your file is {status}")

