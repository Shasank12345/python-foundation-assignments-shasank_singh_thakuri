


def read_chunks(path,n):
    with open(path,'r') as f:
        chunk=[]
        for line in f:
            chunk.append(line.strip("\n"))
            if len(chunk)==n:
                yield chunk
                chunk=[]
        if chunk:
            yield chunk #if number of lines is not multiple of n

n=int(input("Enter How many line you want at a time"))

read=read_chunks('day-05-python-foundations/generator-and-iterators/test.txt',n)


while True:
    try:
        item=next(read)
        for line in item:
            print(line)
        print(" ")
    except StopIteration:
        print('Reached End')
        break
