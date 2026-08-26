
import functools as f
num=[1,2,3,4,5]

product=f.reduce(lambda x,y:x*y,num,1)  #1 for saftey it starst multiplication with 1 (safe if list is empty)
nested=[[1,2],[3,4],[5,6]]
print(f"The product of numbers is : {product}")

flat_num=f.reduce(lambda x,y:x+y,nested,[])

print(f"The flat list is : {flat_num}")
'''
How its flatten  ,, the last argument forces
the reduce to perform the operation as a list 
ie list are flattened via list concatination
-step 1: x=[],y=[1,2],x+y=[1,2]
-step2: x=[1,2],y=[3,4],x+y=[1,2,3,4]
and so on 
'''

'''
Sum() is a built specially for addition
reduce() is a generic fold operator that delegates the combination step to whatever function we pass

'''