

num=[5,12,17,22,30]





squared_list=list(map(lambda x:x**2,num))
div_by_3=list(filter(lambda x:x%3==0,squared_list))

print(f" List of Squared number : {squared_list}")
print(f"List of Squared Number divisible by 3: {div_by_3}")


#using comprehension:

square=[x**2 for x in num]
div_by_3=[x**2 for x in num if x**2 %3==0]

print(f" List of Squared number : {squared_list}")
print(f"List of Squared Number divisible by 3: {div_by_3}")