
logs = [
    "2026-08-21 08:00:12 INFO [auth] User login successful",
    "2026-08-21 08:01:03 WARN [rate_limit] IP exceeded threshold",
    "2026-08-21 08:01:45 ERROR [db] Connection timeout",
    "2026-08-21 08:02:10 CRITICAL [system] OOM killer invoked",
    "2026-08-21 08:03:22 ERROR [auth] Invalid JWT signature"
]
levels=['INFO','ERROR','WARN','CRITICAL']




def cleaner_lines(lines)->list:
    return lines.split(" ") #returns the list of words present in the lines of logs list by splitting them wheneve whitespace is encountered

required_dict={lvl:len(line) for line in logs  for lvl in cleaner_lines(line) if lvl in levels}

print(f'''
The required Dictionary map with level and the lenght of logs is below:
{required_dict}
''')
'''
IF THE LEVELS ARE KEY OF THE DICTIONARY
IT WILL OVERWRITE THE PREVIOUS KEY WITH THE LATEST ENCOUNTER,, 
SO WE SHOULD USE LENGHT AS A KEY 
'''


#Better version
another_dict={len(line):lvl for line in logs for lvl in cleaner_lines(line) if lvl in levels}
print(f'''
The required Dictionary with key as lenght is :
{another_dict}
''')