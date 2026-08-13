
#NUMBER ANALYZING USING FUNCTON

def analyze_numbers(numbers:list):

    return min(numbers),max(numbers),sum(numbers),sorted(numbers,reverse=True)




smallest,largest,total,descending=analyze_numbers([4,9,1,7,3])

print(f'''The smallest is : {smallest}
The largest number  is : {largest}
The sum of numbers is :{total}
The descending order sorted list os :{descending}
''')