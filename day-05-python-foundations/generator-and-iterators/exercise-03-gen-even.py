


def even_number(limit):
    for i in range(limit):
        if i==0:
            continue
        elif i%2==0:
            yield i


limit=int(input("Enter the limit up to which you want to print the evn number"))

even_num=list(even_number(limit))

print(even_num)




