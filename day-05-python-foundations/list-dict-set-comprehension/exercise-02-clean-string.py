#striping string around whitespace

given_list=[" hi"," bye "," yo"]


print(f'''
The list of clean string are :
{[item.strip(' ') for item in given_list]}
''')




