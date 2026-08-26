


num=[5,10,15,20]

num1=iter(num)

while True:
    try:
        print(next(num1))

    except StopIteration:
        break

