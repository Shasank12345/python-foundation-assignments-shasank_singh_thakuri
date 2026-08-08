'''Program to create a new list containing valid integers'''


raw_values =[100,None,250,"Invalid",300,None,450]
print(f"The original messy List : {raw_values}")


#Case I: Using Iteration Method:
clean_value=[] # empty list 
for item in raw_values :
    if not  isinstance(item,int) :
        continue
    clean_value.append(item)
print(f" The list containing only integer : {clean_value}")


#Case II: Using List Comprehension
clean_value_second=[item for item in raw_values if isinstance(item ,int)]
print(f"\nThe required clean list is : {clean_value_second}")