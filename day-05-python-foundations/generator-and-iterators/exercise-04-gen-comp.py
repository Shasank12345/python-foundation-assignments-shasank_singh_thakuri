import sys


number=[x for x in range(10000)]

square_list=[x**2 for x in number]

square_gen=(x**2 for x in number)

print(f'''
The size of list is {sys.getsizeof(square_list)}
The size of generatorlist is {sys.getsizeof(square_gen)}
''')


'''
The size of list is significantly higher than that of generator 
Its is because of follwing reason:
    ->The list comprehension evaluates every item upfront and allocates 
      memory array pointers for all element at once. As the Data grows
      its memory footprint scales lineraly(O(N))
    ->The generator expression holds no actual data in RAM.The allocated
      bytes is puerly the fixed object structure required to keep track of
      the iteration. memory usage remains constant(0(1)) regardless of the iteration



'''

