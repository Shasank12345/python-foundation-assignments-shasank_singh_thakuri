'''@classmethod'''

class Book:

    def __init__(self,title:str,author:str):
        self.title=title
        self.author=author

    
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split('|')
        return cls(title,author)


Book_1=Book.from_string('THE PSYCOLOGY OF MONEY|MORGAN HOUSEL')
print(Book_1.title," Authored By :",Book_1.author) 