'''
CLASS BOOK
'''


class BOOK:
    def __init__(self,tittle:str,author:str):
        self.info=tittle,author
    @property
    def info(self)->tuple[str,str]:
        return self._tittle,self._author
    
    @info.setter
    def info(self,data:tuple[str,str])->None:
        tittle,author=data
        self._tittle=tittle
        self._author=author

    def describe(self)->None:
        print(f"{self._tittle} BY :{self._author} ")


Book_A=BOOK("The Psychology of Money","Morgan Housel")

Book_A.describe()
print("Another Book")
Book_B=BOOK("Let us C","Yashavant kanetkar")
Book_B.describe()

