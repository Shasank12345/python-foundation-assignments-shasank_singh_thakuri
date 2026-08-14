



import json as j


books = [
    {"title": "Deep Learning with Python", "author": "F. Chollet", "year": 2017, "available": True},
    {"title": "Fluent Python", "author": "L. Ramalho", "year": 2022, "available": True},
    {"title": "Automate the Boring Stuff", "author": "A. Sweigart", "year": 2015, "available": True},
    {"title": "Old Python Book", "author": "Someone", "year": 2010, "available": True},
    {"title": "Unavailable New Book", "author": "Someone Else", "year": 2020, "available": False},
]

with open("day-04-python-foundations/library.json", "w") as f:
    j.dump(books, f, indent=2)

print("library.json created.")

def available_books_after(json_path,year,output_path=[])->list:
    with open(json_path,'r') as f:
        output_path=[
            book['title'] 
            for book in j.load(f)
            if book['available']==True and book['year']>year
        ]
    return output_path

books=available_books_after("day-04-python-foundations/library.json",2010)


for title in books:
    print(title)


