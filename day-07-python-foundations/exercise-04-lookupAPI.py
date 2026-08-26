import requests
OPEN_LIBRARY_API="https://openlibrary.org/search.json?"


class BookNotFound(Exception):
    ''''
    Raised when book is not found
    '''

def get_books_facts(OPEN_LIBRARY_API,tittle)->dict:
    
    BACKUP_BOOK_FACTS = {
        "Pride and Prejudice": {"author": "Jane Austen", "first_publish_year": 1813},
        "To Kill a Mockingbird": {"author": "Harper Lee", "first_publish_year": 1960},
        "The Great Gatsby": {"author": "F. Scott Fitzgerald", "first_publish_year": 1925},
        "The Catcher in the Rye": {"author": "J. D. Salinger", "first_publish_year": 1951},
        "1984": {"author": "George Orwell", "first_publish_year": 1949},
        "Brave New World": {"author": "Aldous Huxley", "first_publish_year": 1932},
        "Frankenstein": {"author": "Mary Shelley", "first_publish_year": 1818},
        "Jane Eyre": {"author": "Charlotte Bronte", "first_publish_year": 1847},
        "Moby Dick": {"author": "Herman Melville", "first_publish_year": 1851},
        "The Hobbit": {"author": "J. R. R. Tolkien", "first_publish_year": 1937},
        "War and Peace": {"author": "Leo Tolstoy", "first_publish_year": 1869},
        "Crime and Punishment": {"author": "Fyodor Dostoevsky", "first_publish_year": 1866},
    }
    response=requests.get(OPEN_LIBRARY_API,params={'q':tittle})
    data=response.json()
    docs = data.get('docs', [])
    if not docs:
        if tittle not  in BACKUP_BOOK_FACTS:
            raise BookNotFound()    
        return {BACKUP_BOOK_FACTS[tittle]}
    else:
        result=docs[0]
        return {tittle :{"author":result['author_name'],'first_publish_year':result['first_publish_year']}}

try:
    tittle=input("Enter the book you want to search\n")
    fact=get_books_facts(OPEN_LIBRARY_API,tittle)
    print(f'''Fact of book you looked for {fact}''')
except BookNotFound:
    print("The book you searched for couldnt be retrived")
    


