'''class book with the count attribute '''

class Book:
    count:int=0
    def __init__(self,author,tittle):
        self.info=(author,tittle)

    @property
    def info(self)->tuple[str,str]:
        return self._author,self._tittle,self

    @info.setter
    def info(self ,data:tuple[str,str])->None:
        author,tittle=data
        self._author=author
        self._tittle=tittle
        Book.count+=1

    def describe(self)->None:
        print(f"Book count :{Book.count},{self._tittle} by Author:{self._author}")


Book_A=Book("The Psychology of Money","Morgan Housel")
Book_A.describe()
Book_B=Book("Let us C","Yashavant kanetkar")
Book_B.describe()
Book_C=Book("Let us C++","Yashavant kanetkar")
Book_C.describe()
