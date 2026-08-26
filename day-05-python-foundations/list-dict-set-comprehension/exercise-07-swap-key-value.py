

given={"a":1,"b":2,"c":2,"d":1}


swapped={v:k for k,v  in given.items()}

print(f"{swapped}")

'''
Note:About the Duplicate key value 2 
if while swapping we encounter with duplicate key , 
which is already present in the dictionary,
it will be overwritten by the latest encounter based on our iteration
'''