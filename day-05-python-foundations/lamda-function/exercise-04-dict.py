


people=[{'name':'A','age':30},
        {'name':'B','age':25},
        {'name':'C','age':40}]

sorted_people=[sorted(people,key=lambda x:x['age'])]
youngest=min(people,key=lambda x:x['age'])['name']
oldest=max(people,key=lambda x:x['age'])['name']

print(f'''
The sorted list of people by their age is :{sorted_people}
The youngest person is {youngest}
The oldest person is {oldest}
''')