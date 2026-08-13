

#CALCULATING CLASS AVERAGE USING ARBITARY ARGUMENT *ARGS

def class_average(*scores):

    if not scores:   #we can also check scores==() however not is the best practice
        return 0
    else :
        total=sum(scores)
        average=total/len(scores)
        return average



print(f'''
The average of class with 3 student in class is : {class_average(80,90,70)}
The average of class with 5 student is : {class_average(55,60,65,70,75)}
The average of class with no student is : {class_average()} 
''')
