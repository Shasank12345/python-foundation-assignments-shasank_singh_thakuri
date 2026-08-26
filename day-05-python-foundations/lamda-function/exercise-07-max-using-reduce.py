
import functools as f

people=[{'name':'A','age':30},
        {'name':'B','age':25},
        {'name':'C','age':40}]


def my_max(items,key=...):
    return f.reduce(lambda x,y:x if x[key]>y[key] else y,items)


oldest=my_max(people,key="age")
print(f"The oldest person is {oldest["name"]}")

''''
BEHIND THE SCENE
case 1: x={'name':'A','age':30}
        y={'name':'B','age':25}
        x['age']>y['age] True so x={'name':'A','age':30}
case 2: x={'name':'A','age':30}
        y={'name':'C','age':40}
        x['age']>y['age'] False so x={'name':'C','age':40}
'''